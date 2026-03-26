<!-- Part of Java Learning Roadmap — Section 14 -->

# 🚀 14. Spring Boot

---

## 1. Definition

**Spring Boot** is not a replacement for the Spring Framework; it is a higher-level abstraction (a wrapper) built *on top of* Spring. Its primary goal is to make it easy to create stand-alone, production-grade Spring-based applications with zero code effort.

It follows an **"Opinionated Defaults"** approach: it assumes you want a REST API with Tomcat, Jackson for JSON, and HikariCP for database pooling, and configures them automatically based on the `.jar` files it finds on your classpath.

---

## 2. Why It Exists

*   **No XML / No Boilerplate:** Before Spring Boot, configuring a Spring MVC Web App required editing massive `web.xml` and `dispatcher-servlet.xml` files. Boot eliminates this.
*   **Embedded Servers:** You used to have to compile a `.war` file, download Apache Tomcat separately, install it on a server, and deploy the `.war` into it. Spring Boot embeds Tomcat directly inside a single executable "Fat `.jar`". You just run `java -jar app.jar`.
*   **Starters:** Instead of hunting down 15 compatible library versions for Hibernate, JDBC, and HikariCP, you just import ONE dependency: `spring-boot-starter-data-jpa`, and it pulls everything in harmoniously.

---

## 3. How It Works Internally

### 3.1 The `@SpringBootApplication` Annotation
This single annotation placed on your `main` method class is actually a combination of three critical annotations:
1.  `@SpringBootConfiguration`: Marks this class as a Spring configuration class.
2.  `@ComponentScan`: Tells Spring to automatically scan the *current package* and all *sub-packages* to find `@Controller`, `@Service`, and `@Component` beans.
3.  `@EnableAutoConfiguration`: The real magic of Spring Boot.

### 3.2 Auto-Configuration Magic
When Spring Boot sees `@EnableAutoConfiguration`, it looks at the `spring.factories` (or in Boot 3.0+, `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`) file inside its own JARs. 
It finds hundreds of configuration classes and evaluates **Conditionals**:
*   `@ConditionalOnClass(DataSource.class)`: "Is the H2 or PostgreSQL driver in the `pom.xml`? If yes, create a Database Connection Pool bean automatically."
*   `@ConditionalOnMissingBean`: "Did the developer create their own custom Connection Pool? If yes, back off and don't create the default one."

---

## 4. Code Examples

### 4.1 The Entry Point
```java
package com.myapp; // Putting this at the root package is critical!

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        // Launches the embedded Tomcat server and starts the IoC container
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### 4.2 Profiles in `application.yml`
Profiles allow you to swap configurations based on the environment without changing code.
```yaml
# application.yml (Default)
spring:
  profiles:
    active: dev

---
# application-dev.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb

---
# application-prod.yml
spring:
  datasource:
    url: jdbc:postgresql://production-db:5432/myapp
```

### 4.3 Custom Conditional Bean
```java
@Configuration
public class EmailConfig {

    // This bean is ONLY created if application.yml contains `email.feature.enabled=true`
    @Bean
    @ConditionalOnProperty(name = "email.feature.enabled", havingValue = "true")
    public EmailSender emailSender() {
        return new SmtpEmailSender();
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between Spring and Spring Boot? | Spring is an IoC and DI framework. Spring Boot is an opinionated rapid-application-development wrapper around Spring that provides Auto-Configuration, Starters, and Embedded Servers. |
| What is a Spring Boot Starter? | A pre-configured Maven/Gradle dependency descriptor that groups related libraries together (e.g., `spring-boot-starter-web` brings in Spring MVC, Jackson, Tomcat, and Validation). |
| What is Spring Boot Actuator? | A library that exposes production-ready operational endpoints (like `/actuator/health`, `/actuator/metrics`, `/actuator/env`) to monitor the app's CPU, DB connections, and health status. |
| How do you disable a specific Auto-Configuration? | Using the exclude attribute: `@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})`. |
| Embedded Tomcat vs External Tomcat? | Embedded wraps Tomcat inside the application's executable jar (`java -jar`). External means packaging as a `.war` and dropping it into an already-running Tomcat server installation. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Putting the Main class in the wrong package | If `MyApplication.java` is in `com.app.main` and your controllers are in `com.app.web`, the `@ComponentScan` won't find the controllers because they aren't in a sub-package. | Always put the `@SpringBootApplication` annotated class in the root/base package (e.g., `com.app`). |
| Ignoring `application.properties/yml` overrides | Hardcoding configuration URLs into `@Value` fields or beans instead of using externalized configuration limits deployment flexibility. | ALWAYS use the `application.yml` files and Spring Profiles to manage environmental differences. |
| Exposing Actuator completely | If `/actuator/env` is public, hackers can hit it to read database passwords and AWS Secret Keys in plain text. | Secure Actuator endpoints using Spring Security, leaving only `/health` public. |

---

## 7. Real-World Usage

| Tool | Where it shows up |
|---|---|
| **Fat JARs in Docker** | Because Spring Boot embeds Tomcat, packaging a Java web app into a Docker container is incredibly easy. `FROM openjdk:21`, then `COPY app.jar`, then `ENTRYPOINT ["java", "-jar", "app.jar"]`. |
| **Kubernetes Liveness Probes** | Kubernetes hits the Spring Boot `/actuator/health/liveness` endpoint every 10 seconds. If Spring Boot returns HTTP 500 (meaning Deadlock or OOM), K8s shoots the pod and spins up a fresh one automatically. |
| **Externalized Config Server** | In Microservices, instead of 50 `application.yml` files, apps use Spring Cloud Config to pull their properties from a centralized GitHub repository on startup. |

---

## 8. Practice Tasks

1.  **Zero to API:** Go to `start.spring.io`. Select Web and Actuator. Unzip, open in IDE, write a 5-line `@RestController` that returns a String. Run the `main` method and hit `localhost:8080` in your browser. (Notice how you didn't configure a server).
2.  **Actuator Exploration:** Add `management.endpoints.web.exposure.include=*` to your `application.properties`. Hit `localhost:8080/actuator/beans` to see every single object Spring Boot Auto-Configured for you behind the scenes.
3.  **Profile Swapping:** Create a `@Value("${app.message}") String msg` in your controller. Define different values for `app.message` in `application-dev.properties` and `application-prod.properties`. Change the active profile in your run configuration and observe the output change.

---

## 9. Quick Revision

### The 3 Pillars of Spring Boot
1.  **Starters:** Curated dependency groupings.
2.  **Auto-Configuration:** Conditional bean creation based on classpath contents.
3.  **Actuator:** Production monitoring and metrics.

### Key Annotations
*   `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.
*   `@ConditionalOn...` drives the Auto-Configuration intelligence.
*   `@Profile("dev")` ensures a bean/config is only loaded in the DEV environment.

### Deployment Paradigm Shift
*   **Old:** Code -> `.war` -> Deploy to App Server.
*   **New:** Code -> `.jar` (with embedded server) -> Run as standalone process on Linux/Docker.
