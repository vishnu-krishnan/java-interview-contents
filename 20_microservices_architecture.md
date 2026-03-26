<!-- Part of Java Learning Roadmap — Section 20 -->

# 🌐 20. Microservices Architecture

---

## 1. Definition

**Microservices Architecture** is an approach to software development where a large application is built as a suite of small, independently deployable services. 
*   Unlike a **Monolith**, where the UI, Business Logic, and Database access are all compiled together into one massive `.jar`/`.war` file running on one server, Microservices break these out. 
*   Each service handles a specific business domain (e.g., `UserService`, `OrderService`, `PaymentService`), runs in its own JVM (often its own Docker container), has its own database, and communicates with other services over a network (HTTP/REST or message queues).

---

## 2. Why It Exists

*   **Independent Scaling:** In a monolithic E-commerce app on Black Friday, the `Payment` logic might need 100 servers to handle the load, but the `UserProfile` logic only needs 2. In a monolith, you must deploy 100 copies of the *entire massive application*. With microservices, you just scale up the `PaymentService` container independently.
*   **Independent Deployment:** A team can deploy an update to the `OrderService` on Tuesday at 2 PM without having to recompile, test, and reboot the `UserService`, meaning zero downtime for the rest of the company.
*   **Technology Diversity:** The `UserService` can be written in Java with PostgreSQL, while the `AI-RecommendationService` is written in Python with MongoDB.

---

## 3. How It Works Internally

Because microservices communicate over a hostile network instead of safe in-memory method calls, new architectural infrastructure is required:

### 3.1 Service Discovery (Eureka / Consul)
If `OrderService` needs to call `UserService`, it cannot hardcode `http://192.168.1.5:8080`, because that IP changes every time Kubernetes restarts the `UserService` pod.
*   **Solution:** When `UserService` boots up, it registers its dynamic IP with a central server (e.g., Netflix Eureka). `OrderService` asks Eureka, "Where is the User Service right now?" Eureka replies with the live IP.

### 3.2 API Gateway (Spring Cloud Gateway)
Mobile apps shouldn't have to know the IP addresses of 50 different microservices.
*   **Solution:** The API Gateway is the single public entry point (`api.mycompany.com`). The mobile app asks the Gateway for `/orders`. The Gateway routes the traffic to the internal, hidden `OrderService`. It also handles global tasks like checking JWT Authentication and Rate Limiting.

### 3.3 The Saga Pattern (Distributed Transactions)
In a monolith, saving an Order and charging a User happens in one ACID Database Transaction. If charging fails, the Order rolls back automatically.
In Microservices, the databases are physically separated. 
*   **Solution:** A **Saga** is a sequence of local transactions. `OrderService` creates the order -> Publishes an Event -> `PaymentService` listens, tries to charge. If `PaymentService` fails, it publishes a `PaymentFailedEvent`. `OrderService` listens, and executes a **Compensating Transaction** (a deliberate `UPDATE orders SET status='CANCELLED'`) to undo the initial local commit.

---

## 4. Code Examples

### 4.1 Declarative REST Clients (`OpenFeign`)
Instead of writing complex `RestTemplate` or `HttpClient` code to talk to Service B, Spring Cloud lets you define an interface.
```java
// Spring automatically generates the implementation at runtime!
@FeignClient(name = "user-service") 
public interface UserClient {
    
    @GetMapping("/api/users/{id}")
    UserDto getUserById(@PathVariable("id") Long id);
}

// Inside OrderService:
UserDto user = userClient.getUserById(order.getUserId());
```

### 4.2 Circuit Breaker (`Resilience4j`)
If `PaymentService` is dead, `OrderService` will hang for 30 seconds waiting for a reply. If 10,000 users try to checkout, `OrderService`'s Tomcat thread pool fills up and `OrderService` crashes too (Cascading Failure).
```java
@Service
public class OrderService {

    // If Payment fails 5 times in a row, the Circuit "OPENS". 
    // Future calls instantly return the fallbackMethod without waiting to timeout.
    @CircuitBreaker(name = "paymentService", fallbackMethod = "fallbackPayment")
    public String processPayment(Order order) {
        return restTemplate.postForObject("http://payment-service/charge", order, String.class);
    }

    // The fast-failure alternative response
    public String fallbackPayment(Order order, Exception e) {
        return "Payment Service is currently down. Your order is saved and will be processed later.";
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Monolith vs Microservices? | Monolith is one deployable unit, easy to start, hard to scale. Microservices are independent units, easy to scale/deploy, but extremely complex to orchestrate, monitor, and debug due to network unreliability. |
| What are the 3 states of a Circuit Breaker? | 1. **CLOSED**: Everything is healthy. Traffic flows. 2. **OPEN**: Threshold of failures reached. Traffic is instantly rejected. 3. **HALF-OPEN**: After a timeout, it lets *one* test request through to see if the downstream service recovered. If success -> CLOSED. If failure -> OPEN. |
| Choreography vs Orchestration in Sagas? | **Choreography:** Services publish and listen to events (RabbitMQ/Kafka) independently without a central boss. **Orchestration:** One central "Commander" service explicitly tells all other services what exactly to do and when to rollback. |
| What is the Two-Database Problem? | One service should NEVER connect to another service's database directly. It creates massive coupling. Service A must always call Service B's REST/GRPC API to get data. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| The Distributed Monolith | Breaking an app into 20 microservices, but they all share the exact same Oracle Database, and calling Service A requires a synchronous REST chain to B -> C -> D to finish. | Microservices must be completely decoupled. Give each service its own dedicated Database schema. Use asynchronous messaging (Kafka) instead of deep REST chains. |
| Ignoring Log Tracing | When an order fails, you have to look through 5 different server log files to figure out which microservice threw the exception. | Implement Distributed Tracing (Sleuth/Zipkin). Every HTTP request gets a unique `trace-id` header that is passed between all microservices. |
| Premature Optimization | A startup with 2 developers decides to build a 15-microservice Kubernetes architecture on day one. They spend 90% of their time fixing deployment bugs instead of coding features. | Start with a Modular Monolith. Break it into microservices *only* when the team size or scaling bottlenecks force you to. |

---

## 7. Real-World Usage

| Pattern | Where it shows up |
|---|---|
| **Spring Cloud Gateway** | Used at the edge of the company network. It intercepts the HTTP request, validates the JWT Authentication Token, and passes the parsed User ID header downstream to the microservices, so individual microservices don't have to write authentication code. |
| **Netflix Eureka** | The canonical Service Registry. When a new instance of an Inventory-Microservice boots up on AWS, it pings the Eureka server to announce "I am alive at IP 10.0.4.55". |
| **Config Server** | In a cluster of 50 microservices, if a database password changes, you don't rebuild 50 JARs. Services pull their `application.yml` from a central Git repository via Spring Cloud Config on startup. |

---

## 8. Practice Tasks

1.  **Monolith Decomposition:** Look at a massive E-commerce app. Draw boxes on paper showing how you would split it into 4 microservices. Define exactly what Database tables each service is allowed to own.
2.  **Circuit Breaker Config:** Add `resilience4j-spring-boot3` to a project. Write a dummy REST call to `http://localhost:9999/fake` (which will fail). Configure the circuit breaker in `application.yml` to `sliding-window-size: 5` and `failure-rate-threshold: 50`. Write a loop calling the service 10 times and watch the logs suddenly switch from "Connection Refused" to "CircuitBreaker Open".
3.  **Gateway Routing:** Spin up two basic Spring Boot apps on ports 8081 and 8082. Spin up a Spring Cloud Gateway on 8080. Configure the YAML routing rules so that hitting `localhost:8080/users/**` routes to 8081, and `localhost:8080/orders/**` routes to 8082.

---

## 9. Quick Revision

### Core Microservice Patterns
| Problem | Microservice Solution Pattern | Spring Cloud Tool |
|---|---|---|
| Need a single public entry point | **API Gateway** | Spring Cloud Gateway |
| Finding dynamic IP addresses | **Service Discovery** | Netflix Eureka |
| Hardcoded REST URLs | **Declarative Clients** | OpenFeign |
| Cascading Network Failures | **Circuit Breaker** | Resilience4j |
| Centralized text configs | **Externalized Configuration**| Spring Cloud Config |
| Multi-server logging | **Distributed Tracing** | Micrometer Tracing / Zipkin |
| Multi-server transactions | **Saga / Outbox Pattern** | Kafka / RabbitMQ |
