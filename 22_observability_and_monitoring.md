<!-- Part of Java Learning Roadmap — Section 22 -->

# 🔭 22. Observability & Monitoring

---

## 1. Definition

**Observability** is the ability to understand the internal state of a complex software system just by looking at the data it emits on the outside. In a modern Microservices environment where a single user click might traverse 8 different Docker containers, you cannot simply "read the console" if something goes wrong.

It is universally built on **The Three Pillars**:
1.  **Logging:** A chronological timeline of discrete events (`INFO User 123 logged in`).
2.  **Metrics:** Aggregated numerical data measured over time (`CPU Usage is 85%`, `Requests per second: 400`).
3.  **Distributed Tracing:** Tracking the entire lifecycle of a single request identically across multiple microservices.

---

## 2. Why It Exists

*   **No SSH Access:** In Kubernetes, containers are destroyed and recreated constantly. If you try to SSH into a server to read a log file, the server might not even exist anymore. Logs must be streamed off the server instantly.
*   **Proactive Alerting:** You don't want to find out the database is down because angry users complain on Twitter. Metrics tools (like Prometheus) monitor the database and page the on-call engineer at 3:00 AM automatically if query latency spikes.
*   **Performance Debugging:** If Checkout takes 5 seconds, how do you know if the bottleneck is the Payment Gateway, the Database, or the User Service? Distributed Tracing answers this instantly with a visual waterfall chart.

---

## 3. How It Works Internally

### 3.1 SLF4J and Logback
`SLF4J` is just an interface (a facade). It prevents you from hardcoding your app to a specific logging library. `Logback` is the actual engine (the default in Spring Boot) that writes the text to the hard drive or console. 

### 3.2 ThreadLocals and MDC
How do you track one user's request across 50 different log lines in the same service? 
**MDC (Mapped Diagnostic Context)** uses Java `ThreadLocal` variables. You generate a unique `requestId` when the HTTP request starts, put it in the MDC, and Logback automatically appends that `requestId` to every single `logger.info()` call made by that specific Tomcat thread. 

### 3.3 Prometheus Pull Model
Most monitoring tools (like New Relic) run an agent that *pushes* data up to the cloud. Prometheus works backward: It is a Time-Series Database that actively scrapes (pulls) the `/actuator/prometheus` JSON endpoint of your Spring Boot apps every 15 seconds, storing the CPU and memory numbers in its own database.

### 3.4 Telemetry and W3C Trace Context
To achieve Distributed Tracing, Service A generates a `trace-id`. When Service A makes an HTTP REST call to Service B, it explicitly adds a standard HTTP Header: `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`. Service B reads this header, adopts the same `trace-id`, generates its own `span-id`, and continues the chain.

---

## 4. Code Examples

### 4.1 Proper Java Logging
```java
@Service
public class PaymentService {
    // 1. Always use SLF4J. Make the logger private static final.
    private static final Logger log = LoggerFactory.getLogger(PaymentService.class);

    public void processPayment(String userId, double amount) {
        // 2. Put context in MDC
        MDC.put("userId", userId);
        
        try {
            // 3. Use parameterization {} to avoid expensive string concatenation
            log.info("Processing payment of ${}", amount); 
            chargeApi(amount);
        } catch (Exception e) {
            // 4. ALWAYS pass the exception 'e' as the LAST argument to print the stack trace!
            log.error("Payment failed for user {}", userId, e);
        } finally {
            // 5. ALWAYS clear the MDC to prevent context leaking to the next HTTP request!
            MDC.clear();
        }
    }
}
```

### 4.2 Custom Micrometer Metrics (Spring Boot)
```java
@RestController
public class OrderController {
    
    private final Counter orderCounter;

    // Micrometer acts as an SLF4J for metrics (vendor neutral)
    public OrderController(MeterRegistry registry) {
        this.orderCounter = registry.counter("orders.created.total");
    }

    @PostMapping("/api/orders")
    public void createOrder() {
        // Business logic...
        
        // Increment the metric. Prometheus will scrape this shortly.
        orderCounter.increment(); 
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between a Trace ID and a Span ID? | A **Trace ID** represents the entire architectural journey (e.g., clicking "Checkout", traversing 5 microservices). It stays the exact same. A **Span ID** represents a single hop/operation (e.g., the specific time spent executing the Database Query inside Service C). |
| What is the ELK Stack? | **E**lasticsearch (The NoSQL database holding the logs), **L**ogstash (The pipeline tool that reads logs from Docker, extracts the timestamp/JSON, and saves to Elastic), **K**ibana (The Web UI you log into to search for `level: ERROR "payment failed"`). |
| Why never use `System.out.println`? | 1. It is blocking and synchronized (slow). 2. It doesn't print timestamps or severity levels (INFO vs ERROR). 3. You cannot turn it off in Production without recompiling the code. You can turn off Logback via `application.yml` instantly. |
| Explain structured logging. | Logging as JSON: `{"time":"12:00", "level":"INFO", "msg":"Started"}` instead of plain text string `[INFO] 12:00 - Started`. JSON allows ELK/Splunk to instantly parse, index, and query specific nested fields without complex regex. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Logging Sensitive PII | You write `log.info("User created: {}", userObject);`. The `userObject.toString()` prints their credit card number and password blindly into the production logs. A massive GDPR/security violation. | Use libraries like Logbook, annotate sensitive fields with `@ToString.Exclude` (Lombok), or configure Logback masking rules to overwrite `password=***`. |
| Leaving `DEBUG` or `TRACE` logging active in Production | Generates terabytes of useless data. Will physically fill up the Linux hard drive in a matter of hours, causing Kubernetes to crash the node. | Default Spring Boot root logging to `INFO`. Only enable `DEBUG` temporarily via Spring Boot Actuator when actively investigating an ongoing production fire. |
| Forgetting to `.clear()` the MDC | Tomcat reuses the same thread for a new user request. If you don't clear the MDC, "User B" will execute his logic, but his logs will still say `userId: User_A`. | Write a robust Servlet `Filter` that automatically sets the MDC before the controller, and uses a `finally` block to clear it after the HTTP response is sent. |

---

## 7. Real-World Usage

| Tool / Stack | Architecture Scenario |
|---|---|
| **Prometheus + Grafana** | Prometheus hits Spring Boot's `/actuator/prometheus` endpoint, pulling JVM heap metrics. Grafana is a dashboard UI linked to Prometheus that displays a massive TV graphic showing Memory Usage. If it hits 90%, it triggers a Slack webhook alert to the DevOps channel. |
| **OpenTelemetry (OTel)** | The new industry standard. Instead of importing specific Zipkin or Jaeger agents, you use the OTel Java Agent. It instruments Spring, JDBC, and Hibernate automatically without code changes, shooting Traces, Metrics, and Logs to an OTel Collector. |
| **MDC Trace Logs** | When a customer complains Order #991 failed, customer service gives you that ID. You open Kibana, type `mdc.orderId: 991`. You instantly see the exact 15 log lines across 3 different microservices that executed for that specific order. |

---

## 8. Practice Tasks

1.  **JSON Logs Verification:** Open a Spring Boot `application.yml`. Add `logging.level.root=INFO`. Write a Controller with an `INFO` log. Run it and note the console output. Now, research how to add the `logstash-logback-encoder` dependency and configure `logback-spring.xml` to output pure JSON. Restart and observe the structural difference.
2.  **Actuator Exploration:** Add `spring-boot-starter-actuator` to a project. Expose all endpoints (`management.endpoints.web.exposure.include=*`). Hit `http://localhost:8080/actuator/metrics`. Copy one of the metric names (e.g., `jvm.memory.used`) and hit `/actuator/metrics/jvm.memory.used` to see the live numerical metric data the JVM exposes automatically.

---

## 9. Quick Revision

### The Three Pillars
*   **Logs:** Deep debugging text details. (Tool: ELK, Splunk, Datadog)
*   **Metrics:** High-level numbers indicating system health. (Tool: Prometheus, Grafana)
*   **Traces:** Request lifecycle waterfall diagram. (Tool: Jaeger, Zipkin)

### Logging Levels (Standard)
1.  `ERROR`: A feature is completely broken, requires developer intervention.
2.  `WARN`: Something weird happened, but the app recovered/used a fallback.
3.  `INFO`: High-level business milestones (App started, User Registered).
4.  `DEBUG`: High-traffic developer info for bug chasing (SQL queries executed).
5.  `TRACE`: Extreme detail (entering method X with arguments Y). Never use in Prod.
