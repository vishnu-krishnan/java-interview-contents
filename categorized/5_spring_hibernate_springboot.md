## Java Interviews are not always about Java… sometimes it’s about Java + Vibes 😅

After attending multiple interviews, I realized something interesting.

Senior Java interviews are not just about remembering every concept of Java, Spring Boot, Microservices, Collections, Concurrency, etc.

Sometimes… it’s also about how you deal with the interviewer and what mood they are in that day.

Example 1️⃣
Interviewer: “Explain HashMap internal working.”
You: Explain hashing, buckets, collisions, load factor, resizing, time complexity… basically a mini lecture.
Interviewer: “Okay… we’ll get back to you.”
Result: ❌ Rejected

Example 2️⃣
Interviewer: “Explain HashMap.”
You: “It stores key-value pairs… uses hashing… average O(1) lookup.”
Interviewer: “Nice. Let’s move to next round.”
Result: ✅ Selected

Sometimes you answer all the questions perfectly but still don’t move forward.

And sometimes you answer half the questions, but the interviewer likes your approach, communication, or problem-solving style… and you get selected.

Lesson learned 👇
Interviews are not only about knowledge, they are also about:

- Communication
- Confidence
- Thought process
- And sometimes… interviewer mood 😄

So if you ever get rejected after a good interview, don’t doubt your skills.

Maybe it wasn’t about Java…
Maybe it was just about the vibes.
---
## 1️⃣ Tell me about yourself.

2️⃣ Explain your project architecture.
Which technologies and versions did you use for building the application?
3️⃣ What is the difference between Spring and Spring Boot?
4️⃣ What is the difference between HashMap and ConcurrentHashMap?
5️⃣ How do you perform load testing for your application?
6️⃣ What is a Load Balancer and why is it used?
7️⃣ How do you resolve production bugs in a live system?
8️⃣ How would you handle a system processing 1 million transactions?
9️⃣ If an API works in the local environment but fails in production, how would you investigate and fix it?
🔟 What is Docker?
How do you create a Docker image for your application?
1️⃣1️⃣ What is Redis Cache and how does it work?
1️⃣2️⃣ If data is not updated in Redis cache, how would you troubleshoot and resolve it?
1️⃣3️⃣ What is Kafka Server and why is it used?
1️⃣4️⃣ If duplicate messages are received in Kafka, how do you prevent or handle them?
1️⃣5️⃣ How do you send messages using Kafka in your application?
1️⃣6️⃣ What is Jenkins and how do you deploy code using Jenkins?

17.What is the difference between PUT and PATCH in REST APIs?
PUT is used to update the entire resource. It replaces the full object.
PATCH is used to update only specific fields of a resource (partial update).
Example: Updating only a user's email instead of the entire user object.

18.How do you add an index in a database?
Indexes improve query performance by allowing the database to find rows faster.
Example SQL query:
CREATE INDEX idx_user_email ON users(email);
3️⃣ How do you optimize a slow API? What steps do you follow for analysis?
When an API response time is slow, the typical investigation steps are:
🔹 Step 1 – Check Logs
Review application logs to identify errors or slow operations.
🔹 Step 2 – Measure API Response Time
Use tools like Postman, monitoring tools, or APM tools to identify the latency.
🔹 Step 3 – Analyze Database Queries
Check if queries are slow. Use EXPLAIN to analyze query performance and add indexes if required.
🔹 Step 4 – Check External API Calls
If the API calls third-party services, verify their response time.
🔹 Step 5 – Use Caching
Implement caching mechanisms such as Redis to reduce database calls.
🔹 Step 6 – Optimize Code Logic
Check for unnecessary loops, heavy computations, or inefficient algorithms.
🔹 Step 7 – Load Testing
Use tools like JMeter or Gatling to simulate concurrent users and analyze performance.
🔹 Step 8 – Horizontal Scaling
Use load balancers and multiple instances of the service to handle high traffic.

💡 These questions are very common in startup backend interviews, especially for developers working with Java, Spring Boot, Microservices, Kafka, Redis, and Docker.
---
## SOLID Principles in Java – Explained Simply

When building scalable and maintainable software, following good design principles is essential. One of the most important concepts in Object-Oriented Programming is SOLID Principles.

SOLID is a set of five design principles that help developers write clean, flexible, and maintainable code.

Let’s understand them in a simple way.

1️⃣ Single Responsibility Principle (SRP)

A class should have only one responsibility or one reason to change.

Bad example:
 A class that handles database operations + business logic + logging.

Good approach:
 Split them into separate classes.

Example:
OrderService → Business logic
OrderRepository → Database operations
LoggerService → Logging

This makes the code easier to maintain and test.

2️⃣ Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification.

Instead of modifying existing code, we should extend it using new classes.

Example:
 Add a new payment method by creating a new class rather than modifying existing logic.

3️⃣ Liskov Substitution Principle (LSP)

Objects of a superclass should be replaceable with objects of its subclass without breaking the application.

Example:
 If Bird is a parent class, any subclass like Sparrow should work correctly wherever Bird is used.

4️⃣ Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use.

Instead of creating large interfaces, split them into smaller, specific ones.

Example:
 Vehicle
 Driveable
 Flyable

This keeps interfaces clean and focused.

5️⃣ Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).

In Spring Boot, this is achieved using Dependency Injection.

Example:
@Autowired
private PaymentService paymentService;

This makes the system loosely coupled and easier to maintain.

Why SOLID Principles Matter
Following SOLID principles helps to:
✔ Improve code readability
 ✔ Reduce tight coupling
 ✔ Make applications easier to scale
 ✔ Improve maintainability

These principles are widely used in Java, Spring Boot, and enterprise applications.

Tech Stack I work with:
 Java | Spring Boot | REST APIs | PostgreSQL | React
---
## Recently attended an #interview with #EY and wanted to share the questions that were discussed. The interview covered Java fundamentals, Spring Boot, Microservices, AWS, and DevOps related topics.

The round started with basic discussion about my background.

Introduction and #Project Discussion:

Explanation of my current and past projects
Tech stack used and responsibilities in the project

Difference between #Spring and Spring Boot?
How security works in your project?
What is #Authentication and #Authorization?
What is @SpringBootApplication annotation
How @EnableAutoConfiguration works internally?
What is @Component?
How beans are created when we use @Component annotation in a class
Difference between @Component, @Service, and @Repository?
How @Transactional works?
How microservices communicate with each other?

What is the #volatile keyword?
What is the use of volatile?
What is #abstraction and polymorphism?
Difference between #encapsulation and abstraction?
What is the difference between Spring, #SpringBoot, JPA, and #Hibernate?

How do you #deploy your service in a serverless #environment?
What is EC2 and how do you create an EC2 instance?
How to connect #EC2 with #S3?
What is load balancing and how it is configured?
What is auto scaling and how it is configured?
How your applications are deployed in #AWS?
How do you configure a Dockerfile?
Have you written Jenkins pipelines?
How do you configure SonarQube?

What is your strength?
What is your weakness?

Overall, the interview covered a wide range of topics including Java fundamentals, Spring ecosystem, cloud deployment, and DevOps practices.

All the best to everyone preparing.
---
## 🚀 Java Exception Handling – Top Interview Questions (Experienced Developers)

Exception handling is not just about try-catch.
At senior levels, interviewers evaluate design maturity, JVM understanding, performance impact, and real production handling.

If you have 2+ years of experience, expect questions like these 👇

💡 Most Asked Java Exception Handling Interview Questions

🔹 1. Difference between Checked vs Unchecked Exceptions — and why Java supports both
🔹 2. Why is RuntimeException not mandatory to handle? When should you create a custom RuntimeException?
🔹 3. Can a finally block be skipped? Real-world scenarios
🔹 4. Difference between throw vs throws with use cases
🔹 5. What happens if an exception is thrown in finally? Which exception survives?
🔹 6. Why is exception handling expensive? How to optimize for high-performance systems
🔹 7. How does exception propagation work internally in the JVM?
🔹 8. Difference between Error vs Exception — why catching Error is dangerous
🔹 9. What is exception chaining and why it’s critical in microservices & debugging
🔹 10. How to design global exception handling in Spring Boot (real project approach)
🔹 11. Why exceptions should never be used for normal flow control
🔹 12. try-with-resources vs finally — which is safer and why?
🔹 13. How to separate business exceptions vs technical exceptions in enterprise apps
🔹 14. Multiple catch blocks — ordering rules & pitfalls
🔹 15. Exception handling in async code (CompletableFuture, threads, executors)

🎯 Why this matters

✔ Cleaner APIs
✔ Better debugging & observability
✔ Stable production systems
✔ Stronger interview confidence

💬 If you can explain these clearly, you’re operating at a Senior Java Developer level.
---
## JWT Authentication & Authorization in Spring Boot – Simplified!
Understanding how security works in modern applications is crucial for every developer. Here’s a quick breakdown of how JWT (JSON Web Token) works in a Spring Boot application:
➡️ User logs in via API
➡️ Server validates credentials
➡️ JWT token is generated & signed
➡️ Token is sent back to the client
➡️ Client sends token with every request
➡️ JWT filter validates the token
➡️ Security context is set with user roles
➡️ Authorization check grants or denies access
💡 This approach ensures:
✔️ Stateless authentication
✔️ Secure API communication
✔️ Scalable system design
As a Java Full Stack Developer, mastering JWT with Spring Boot is a must for building secure applications.
---
## One of the most common errors in Java is NullPointerException. Even experienced developers still run into it.

While Java is slowly improving with Project Valhalla, frameworks like Spring already give us tools to write safer code today.

In Spring Boot 4, you can use JSpecify annotations to mark which values can be null and which cannot:
- @NullMarked – everything is non-null by default
- @Nullable – this value can be null
- @NonNull – explicitly non-null
- @NullUnmarked – turns off default non-null
For example, if you mark a package with @NullMarked, all reference types are assumed non-null unless you mark them as @Nullable. IDEs and tools can then warn you before a NullPointerException happens. This is a small change, but it makes your code safer, easier to understand, and more predictable.

Special thanks to Dan Vega, his YouTube videos help to understand not only these annotations, but he also has many great videos about Spring and the new features in Spring Boot 4.

Have you tried JSpecify annotations in your projects?
---
## 🔹 1. JVM starts the application

The JVM creates the main thread and executes the "main()" method.

@SpringBootApplication
public class Application {
 public static void main(String[] args) {
 SpringApplication.run(Application.class, args);
 }
}
---
## If you're a Java/Spring developer looking to add AI to your application, you’ve probably noticed one thing: making a single LLM call is easy. Turning it into a scalable, production-ready feature? That’s where things get tricky.
That’s exactly why Spring AI was created. Built by the team behind the Spring Framework, it helps you integrate AI into your apps using the same familiar Spring concepts—dependency injection, clean configuration, and well-structured architecture.
And it’s more than just an API wrapper:
🔹 Connects to multiple AI providers (OpenAI, Azure OpenAI, and others) through a unified API
🔹 Includes built-in support for prompt templates
🔹 Simplifies working with embeddings and vector databases
🔹 Makes implementing Retrieval-Augmented Generation (RAG) much easier
🔹 Comes with production-ready configuration and observability support
No more stitching together SDKs or writing custom glue code.
With Spring AI, you can build AI-powered features the Spring way—clean, maintainable, and ready to scale.
AI in real Java applications. Built properly
---
## Great time to be a Java developer! Benchmarking Model Context Protocol (MCP) server implementations across #Java, #Python, #JavaScript, and #Go shows the MCP Java SDK with #SpringAI leading the pack: sub-milliseconds latency, highest throughput, and best CPU efficiency.
Kudos to Thiago Mendes
---
## Most Java developers think AI integration is complex.
It’s actually much simpler than it looks.
Here’s a minimal example using Spring AI to call an LLM from a Java application:

ChatClient chatClient = ChatClient.create(openAiChatModel);
String response = chatClient
 .prompt("Explain microservices in simple terms")
 .call()
 .content();
System.out.println(response);

That’s it.
You’re calling an LLM directly from your Java code.
Now imagine extending this:
→ Add user input
→ Add database context (RAG)
→ Wrap it inside a REST API
→ Add caching + retries
Suddenly, you’re not building a demo.
You’re building a production-ready AI system.
This is the shift happening right now:
AI is no longer just for ML engineers.
It’s becoming part of backend engineering.
And Java developers are perfectly positioned for this.
Making the world AI-ready with Java — one developer at a time.
If you’re exploring this, what are you building?
---
## Java Backend Developer - 1st Round Interview

These 20 questions are being asked in interviews right now.

1. How does HashMap work internally? Explain buckets, hashing mechanism, and resizing process.
2. What is the difference between HashMap and ConcurrentHashMap?
3. Explain the JVM memory architecture (Heap, Stack, Metaspace).
4. What are common causes of OutOfMemoryError in production? How would you troubleshoot it?
5. How do you make a class thread-safe? Provide a practical example.
6. Describe the complete lifecycle of a Spring Bean.
7. How does Dependency Injection function internally in Spring?
8. What happens internally when you use @Transactional?
9. What is the difference between @Component, @Service, and @Repository?
10. How would you implement global exception handling in Spring Boot?
11. What is lazy vs eager loading in JPA? In which scenarios can it impact performance?
12. How do you manage concurrent updates to the same database record?
13. Explain ACID properties using a banking transaction example.
14. How would you optimize a slow-performing SQL query?
15. How would you design pagination and sorting in a REST API?
16. Explain the step-by-step flow of JWT authentication.
17. If your API performance degrades under load, how would you identify the bottleneck?
18. REST vs Messaging (Kafka) when would you choose each approach?
19. How would you Dockerize a Spring Boot application?
20. If two microservices fail during communication, how would you implement fault tolerance?
---
## Here you go 👍 — a complete Java Backend Developer (3–6 Yrs) :: Interview Questions Asked @ HCL Technologies 🚀
HCL interviews are usually practical + project-based, focusing on:
 ✔ Core Java
 ✔ Spring Boot
 ✔ SQL
 ✔ Microservices basics
 ✔ Some coding + real-time scenarios
💡 HCL :: Java Backend Developer Interview Questions (3–6 Yrs)
🧠 Core Java (Very Important)
1️⃣ Difference between HashMap, LinkedHashMap, TreeMap
 2️⃣ How does HashMap work internally? (hashing, buckets, collision)
 3️⃣ Difference between Comparable vs Comparator
 4️⃣ What is immutable class? How to create one?
 5️⃣ Difference between String, StringBuilder, StringBuffer
 6️⃣ What is multithreading? Explain lifecycle of thread
 7️⃣ Difference between synchronized vs Lock (ReentrantLock)
 8️⃣ What is volatile keyword?
 9️⃣ What is deadlock and how to prevent it?
 🔟 Explain ExecutorService and thread pool
🌿 Spring & Spring Boot
1️⃣1️⃣ Difference between Spring and Spring Boot
 1️⃣2️⃣ What is @RestController?
 1️⃣3️⃣ Difference between @Component, @Service, @Repository
 1️⃣4️⃣ How does Spring Boot Auto Configuration work?
 1️⃣5️⃣ What is Dependency Injection (IoC)?
 1️⃣6️⃣ How do you handle global exception handling? (@ControllerAdvice)
 1️⃣7️⃣ What is @Autowired and @Qualifier?
 1️⃣8️⃣ What is Spring Boot Actuator?
 1️⃣9️⃣ What is @Transactional?
 2️⃣0️⃣ How do you implement pagination & sorting in Spring Boot?
💾 JPA / Hibernate & Database
2️⃣1️⃣ Difference between save(), persist(), merge()
 2️⃣2️⃣ What is lazy loading vs eager loading?
 2️⃣3️⃣ What is N+1 problem?
 2️⃣4️⃣ Explain @OneToMany and @ManyToOne mapping
 2️⃣5️⃣ What are entity states in Hibernate?
 2️⃣6️⃣ What is indexing and how it improves performance?
 2️⃣7️⃣ Difference between INNER JOIN vs LEFT JOIN
 2️⃣8️⃣ What is ACID property?
 2️⃣9️⃣ Write SQL to find second highest salary
 3️⃣0️⃣ How do you optimize slow SQL queries?
🧩 Microservices & Architecture
1️⃣ Difference between monolithic vs microservices architecture
 2️⃣ What is API Gateway?
 3️⃣ What is Service Discovery?
 4️⃣ How do microservices communicate? (REST / Kafka)
 5️⃣ What is Circuit Breaker pattern?
 6️⃣ How do you handle configuration management?
 7️⃣ What is load balancing?
 8️⃣ How do you ensure fault tolerance?
 9️⃣ What is idempotent API?
 🔟 How do you implement logging & monitoring?
☁️ Cloud & DevOps Basics
1️⃣ What is Docker?
 2️⃣ Difference between Docker image vs container
 3️⃣ What is CI/CD pipeline?
 4️⃣ How does Jenkins pipeline work?
 5️⃣ What is Kubernetes (basic)?
 6️⃣ Difference between vertical vs horizontal scaling
 7️⃣ What is Blue-Green deployment?
⚙️ Coding Round (Common in HCL)
1️⃣ Reverse a string
 2️⃣ Find duplicate elements in array
 3️⃣ First non-repeating character
 4️⃣ Check palindrome string
 5️⃣ Find second largest number
 6️⃣ Reverse linked list
---
## Stop writing manual null-checks in your Spring Boot controllers! 🛡️

Bean Validation with @Valid lets you declare validation rules directly on your model — Spring handles the rest automatically.

public record CreateUserRequest(
 @NotNull String name,
 @NotBlank String username,
 @Size(min = 8, max = 64) String password,
 @Email String email,
 @Min(18) int age
) {}

@PostMapping("/users")
public ResponseEntity<UserResponse> createUser(
 @Valid @RequestBody CreateUserRequest request) {
 // Validation fails → 400 Bad Request auto-returned
 return ResponseEntity.status(201).body(service.create(request));
}

Key annotations to master:
- @NotNull / @NotBlank / @NotEmpty — null and empty checks
- @Size(min, max) — string or collection length
- @Min / @Max — numeric bounds
- @Email — valid email format
- @Pattern(regexp) — custom regex rules

Pair it with @RestControllerAdvice + MethodArgumentNotValidException handler to return clean, structured error messages to your API consumers.

And if built-in annotations aren't enough? You can create custom constraints with your own business logic (e.g. @UniqueEmail that queries the database).
---
## When building a Java Spring Boot project, the project structure is often overlooked. How you organize packages directly impacts scalability and maintainability.
From my experience, a clean, well defined structure makes development smoother, especially as the project grows.
Here’s how I usually structure my project and how each part connects in the request flow:

- Controller
 Receives HTTP requests and forwards data to the service layer. It stays simple, handling request/response only.

- DTO (Data Transfer Object)
 Maps incoming data to control what enters and leaves the system, avoiding direct exposure of entities.

- Service
 Contains business logic. It processes input from the controller, applies rules, and decides what happens next.

- Mapper
 Converts DTOs into entities and vice versa, keeping transformation logic separate from business logic.

- Model (Entity)
 Represents database tables. Data is converted into entities matching the database structure.

- Repository
 Handles database interaction. The service calls the repository to save, update, or fetch data.

- Security
 Manages authentication and authorization (e.g., JWT) to ensure only valid users access the system.

- Exception
 Handles errors globally, returning consistent responses to the client.

- Config
 Contains setup like beans, CORS, Swagger, and other configuration support.

- Constants
 Stores fixed values (messages, keys, roles) to avoid hardcoding across the project.

- Enums
 Defines predefined values (user roles, order status) for type safety and readability.

Flow: Request → Controller → DTO → Service → Mapper → Model → Repository → back → Response.

This structure keeps responsibilities clear, improves readability, and allows the project to scale without messiness. Avoid putting everything in one package, it becomes hard to manage.

How do you structure your projects? Do you follow a similar flow, or approach it differently?
---
## Spring Boot simplified — from startup to production 🚀

Understanding how Spring Boot works internally is a game-changer for backend developers.

From auto-configuration to dependency injection, and from embedded servers to REST APIs, everything is designed to reduce boilerplate and speed up development.

🔑 Key takeaways:

No XML config — convention over configuration

Embedded servers (no external deployment needed)

Powerful auto-configuration based on classpath

Clean layered architecture (Controller → Service → Repository)

Production-ready apps with minimal setup

- Build fast. Scale smart. Ship confidently.
---
## Spring Boot: Understanding the Internal Request Flow 🚀

Ever wondered what actually happens inside a Spring Boot application when a request is sent? Here’s a simplified breakdown of the internal flow:

1️⃣ Dispatcher Servlet
Every HTTP request (from browser, Postman, or mobile) first reaches the Dispatcher Servlet. It acts as the central entry point that manages and routes all incoming requests.

2️⃣ Handler Mapping
The Dispatcher Servlet consults Handler Mapping to identify which controller method should handle the incoming request URL.

3️⃣ Controller Layer (@RestController)
Once identified, the appropriate controller method is invoked to handle the request.

4️⃣ Service Layer (@Service)
The controller delegates business logic to the service layer, ensuring proper separation of concerns.

5️⃣ Data Access Layer (@Repository)
The service interacts with the repository layer, which communicates with the database using Spring Data JPA.

6️⃣ Database Interaction
The query is executed in the database, and results flow back through the layers:
Database → Repository → Service → Controller → Dispatcher Servlet

7️⃣ Serialization (Jackson)
With @RestController, Spring skips the View Resolver. Instead, Jackson automatically converts Java objects into JSON/XML format.

8️⃣ HTTP Response
Finally, the serialized response is sent back to the client in a clean and efficient way.

💡 Key Insight
@RestController = @Controller + @ResponseBody
This is why Spring Boot directly returns data instead of resolving views—making REST APIs lightweight and high-performing.
---
## 🚀 Day 69/100 - Spring Boot - @Cacheable & @CacheEvict

Caching is not just about storing data...

You also have to keep the data consistent when it changes.

Spring Boot provides 2 annotations for this:

1️⃣ @Cacheable - Store & Reuse Data

@Cacheable caches the result of a method so repeated calls with the same parameters skip the execution.

➡️ Example (see attached image 👇)

➡️ Behavior
🔹First call → executes method & caches result
🔹Next calls (same id) → returned directly from cache
🔹Improves performance by avoiding repeated DB calls

2️⃣ @CacheEvict - Keep Cache in Sync

When data changes, the cache must be updated or cleared. That’s where @CacheEvict comes in.

➡️ Example (see attached image 👇)

➡️ Why it matters
🔹Removes stale data from cache
🔹Ensures users don’t see outdated results
🔹Keeps cache consistent with the database
---
## 🚀 Day 72/100 - Spring Boot -Scheduling Tasks (@Scheduled)

Modern applications often need to run tasks in the background. For instance:

🔹Send daily reports
🔹Clean up old data
🔹Sync systems

Spring Boot makes this possible using @Scheduled.

➡️ Enable Scheduling

You can enable scheduling in your main class, OR the class where you want it, using @EnableScheduling annotation.

➡️ Using @Scheduled

You can use @Scheduled annotation for a task/method, for which different scheduling options are available:

- fixedRate
Runs a task at a fixed interval, regardless of execution time.

- fixedDelay
Runs a task after the previous execution finishes.

- cron
Provides flexible scheduling using cron expressions (I'll explain it deeply in the next post)

➡️ Example: see attached image 👇
---
## Deep Dive into Spring Boot Internals: How Auto-Configuration Really Works

Most developers use Spring Boot daily, but very few truly understand what happens behind the scenes when an application starts. One of the most powerful features of Spring Boot is Auto-Configuration, which automatically sets up beans, configurations, and dependencies based on the classpath and application settings.

🧠 Core Idea

Spring Boot scans the classpath, detects available libraries (like Spring MVC, JPA, Kafka, etc.), and automatically configures beans so developers don’t have to manually write large configuration files.
---
## 𝗕𝗲 𝗰𝗮𝗿𝗲𝗳𝘂𝗹 𝘄𝗵𝗲𝗻 𝘂𝘀𝗶𝗻𝗴 @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹!

When working with Spring Boot with Hibernate, annotations play an important role in building compact and efficient systems. Thus, knowing what the annotations are doing and how to correctly use them is a key part of software development.

The annotation @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹 can have an undesired behavior if used incorrectly.

In the self-invocation example, we have an internal method making a database call, annotated with @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹, while the public method that is called by the Controller doesn’t have any. As Spring is proxy-based, this simple method call inside a Java class will not trigger the annotation, meaning a transaction is never started. This can cause serious inconsistencies, because a rollback will not be applied to your database if something goes wrong further in the process, leaving you with corrupted data.

So, to be able to have the benefits of the Transactional annotation, you can either move it to the method that is being called by the Controller, or, my preferred approach, extract the database handling to its own Service class and add @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹 to the method. This ensures the transaction is started, enforcing the atomicity of the process.

Two tips to keep in mind when using @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹:

1. The use of 𝘳𝘰𝘭𝘭𝘣𝘢𝘤𝘬𝘍𝘰𝘳 = 𝘌𝘹𝘤𝘦𝘱𝘵𝘪𝘰𝘯.𝘤𝘭𝘢𝘴𝘴 as a parameter of this annotation is beneficial, because, by default, Spring only rolls back for unchecked exceptions (𝘙𝘶𝘯𝘵𝘪𝘮𝘦𝘌𝘹𝘤𝘦𝘱𝘵𝘪𝘰𝘯 and 𝘌𝘳𝘳𝘰𝘳), so using this parameter also triggers the rollback for checked exceptions.
2. Use the 𝘳𝘦𝘢𝘥𝘖𝘯𝘭𝘺=𝘵𝘳𝘶𝘦 parameter when you are only fetching data (e.g. GET requests). This disables Hibernate’s 𝗗𝗶𝗿𝘁𝘆 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴, meaning it avoids allocating memory for entity snapshots in the 𝗣𝗲𝗿𝘀𝗶𝘀𝘁𝗲𝗻𝗰𝗲 𝗖𝗼𝗻𝘁𝗲𝘅𝘁. This reduces Garbage Collection and CPU pressure, resulting in faster response times.

Do you know other powerful @𝗧𝗿𝗮𝗻𝘀𝗮𝗰𝘁𝗶𝗼𝗻𝗮𝗹 parameters? Let me know in the comments.
---
## 💻 Modern Spring Boot Patterns Every Developer Know
When you’re coding in Spring Boot, you probably know how to make services, repositories, and DTOs work… but do you know the design patterns hiding behind your code? 🤔
Understanding these patterns helps you:
✨ Write cleaner, more maintainable code
 ⚡ Debug faster and trace issues like a pro
 💬 Communicate design decisions clearly with your team
Here’s a modern cheat sheet mapping Spring Boot code to OOAD patterns:
---
## 🚀 Understanding the Internal Working of Spring Boot
As a Java developer, mastering how Spring Boot works internally can significantly improve debugging, performance tuning, and system design.
Here’s a simplified flow of how a request is processed:
🔹 1. Client Request
A request is sent from the browser (HTTP).
🔹 2. Dispatcher Servlet (Front Controller)
Acts as the entry point and receives all incoming requests.
🔹 3. Handler Mapping
Identifies the correct controller method based on the request URL.
🔹 4. Handler Adapter
Invokes the appropriate controller method.
🔹 5. Controller Layer
Handles the request and delegates business logic to the service layer.
🔹 6. Service Layer
Contains core business logic and interacts with repositories.
🔹 7. Data Access Layer (Repository)
Communicates with the database using tools like Spring Data JPA.
🔹 8. Database Interaction
Data is fetched/stored in the database.
🔹 9. View Resolver & View
Maps the response to a view (like Thymeleaf/JSP) or returns JSON.
🔹 10. Response to Client
Final response is sent back to the user.
💡 Why this matters?
Understanding this flow helps in: ✔ Debugging issues faster
✔ Writing clean layered architecture
✔ Optimizing performance
✔ Cracking interviews with confidence
👨‍💻 As developers, we often use frameworks but knowing what happens behind the scenes gives us an edge.
---
## THE INTERVIEWER OPENS YOUR SPRING BOOT PROJECT
AND STARTS ASKING QUESTIONS.

Not about theory.
About decisions you made in the code.

Questions like these:

- Why did you choose @RestController instead of @Controller in this API?
- Why are you using constructor injection instead of field injection here?
- Why did you mark this service as @Transactional?
- Why did you choose Spring Data JPA instead of writing JDBC queries?
- Why did you configure HikariCP with this pool size?
- Why did you separate Controller, Service, and Repository layers?
- Why is this endpoint returning DTOs instead of entities?
- Why are you using @Async for this method?
- Why did you introduce caching for this API?
- Why are you using pagination for this database query?
- Why did you configure a global exception handler with @ControllerAdvice?
- Why are you using environment profiles (dev, prod)?
- Why is this API call wrapped with a timeout?
- Why are you using validation annotations like @Valid?
- Why is this API idempotent for retries?
- Why did you move this logic out of the controller into a service?
- Why are you using a connection pool instead of opening connections manually?
- Why did you configure logging differently for production?
- Why is this API call asynchronous instead of synchronous?
- Why did you structure the project this way?

Spring Boot interviews often look like this.

They don’t just test if you know annotations.

They test whether you understand
*why your backend is designed the way it is.*

Which of these would be hardest for you to answer in an interview?
---
## Spring Boot looks easy…
Until the interviewer goes deep.

Many developers can build APIs using Spring Boot. But in product company interviews, they test what happens internally.

Here are 30 real Spring Boot questions asked in backend interviews 👇

1. How does Spring Boot decide which auto-configuration to apply?
2. What happens internally when you add spring-boot-starter-web?
3. Why does Spring Boot prefer Convention over Configuration?
4. How does Spring Boot load application.properties internally?
5. What is the exact startup flow of a Spring Boot application?
6. Difference between @ComponentScan and @SpringBootApplication?
7. How does Spring Boot detect embedded Tomcat automatically?
8. What happens if two beans of same type exist without @Qualifier?
9. How does Spring Boot load profile specific configurations?
10. What is the role of SpringFactoriesLoader?
11. How did Spring Boot remove XML configuration almost completely?
12. Difference between @RestController and @Controller internally?
13. How does Spring Boot manage dependency versions automatically?
14. What is the complete lifecycle of a Spring Bean?
15. How does Spring Boot handle externalized configuration?
16. What happens if application.yml and application.properties both exist?
17. How does Spring Boot integrate with Actuator internally?
18. Difference between @Configuration class and normal class?
19. How does Spring Boot auto-create DataSource?
20. What is the real use of CommandLineRunner?
21. How does Spring Boot handle exception translation?
22. Difference between @EnableAutoConfiguration and @Import?
23. What happens when you exclude an auto-configuration class?
24. Why is Spring Boot perfect for microservices?
25. Difference between fat JAR and normal JAR?
26. How does Spring Boot handle logging by default?
27. How does Spring Boot decide server port priority?
28. What happens internally when you hit a REST endpoint?
29. Why is Spring Boot preferred for cloud-native apps?
30. What are the most common Spring Boot performance mistakes?

Spring Boot looks simple. But its internal architecture is what makes it powerful.
If you can answer these questions confidently, you are already ahead of 90% backend candidates.
---
## 🚀 @RestController vs @Controller — Do You Know the Real Difference?

Most Spring Boot developers reach for @RestController without thinking twice. But knowing why it exists separates good engineers from great ones.

@Controller is the classic Spring MVC annotation — it marks a class as a web controller that returns view names (like Thymeleaf templates). To return JSON from a @Controller method, you must explicitly add @ResponseBody.

@RestController is simply a convenience annotation that combines @Controller + @ResponseBody. Every method automatically serializes the return value to JSON/XML via Jackson — no extra annotation needed.

// Classic MVC — returns a Thymeleaf view
@Controller
public class PageController {
 @GetMapping("/home")
 public String home(Model model) {
 model.addAttribute("user", "Janis");
 return "home"; // resolves to home.html
 }
}

// REST API — returns JSON automatically
@RestController
@RequestMapping("/api/users")
public class UserController {
 @GetMapping("/{id}")
 public User getUser(@PathVariable Long id) {
 return userService.findById(id); // auto-serialized to JSON
 }
}

The rule is simple:
→ Building a REST API? Always use @RestController.
→ Building server-side rendered views (SSR)? Use @Controller.

In modern microservice architectures, @RestController dominates — because APIs communicate via JSON, not HTML pages.
---
## 🚀 What actually happens inside the JVM when a Spring Boot application starts?

Most developers run a Spring Boot app with one command:

"java -jar app.jar"

But inside the JVM, a lot happens before your API becomes available.

Here’s a simplified breakdown 👇
---
## 🔹 4. Spring Boot Startup Begins

"SpringApplication.run()" starts the Spring ecosystem:

- Creates ApplicationContext
- Reads "application.properties" / "application.yml"
- Determines auto configurations
---
## 🔹 5. Component Scanning

Spring scans packages to detect components like:

- "@Controller"
- "@Service"
- "@Repository"
- "@Component"

These become Spring Beans.
---
## 🔹 6. Bean Creation

Spring first creates Bean Definitions and then instantiates beans.

Process:

Constructor → Dependency Injection → Bean Post Processing
---
## 🔹 7. AOP Proxies

For features like:

- "@Transactional"
- "@Async"
- "@Cacheable"

Spring creates proxies using JDK Dynamic Proxy or CGLIB.
---
## 🔹 8. Embedded Server Starts

Spring Boot starts an embedded server like Tomcat and initializes DispatcherServlet.

Your APIs are now ready to serve requests.
---
## 💡 Full Startup Flow

JVM Start
↓
Class Loading
↓
Bytecode Verification
↓
main() execution
↓
SpringApplication.run()
↓
ApplicationContext creation
↓
Component scanning
↓
Bean creation
↓
Dependency injection
↓
AOP proxy creation
↓
Embedded server start
↓
Application ready
---
## ⚡ Senior developer insight

Most startup issues in production happen during:

- Bean creation
- Dependency injection
- Auto configuration
- Missing environment properties

Understanding this flow makes debugging Spring Boot startup failures much easier.
---
## If you're a Spring developer:

- Which startup error has troubled you the most?
---
## In a recent Java backend interview, I was asked some interesting questions.

Not about frameworks like Spring Boot.
But about core backend fundamentals.

Here are a few that stood out:

1️⃣ Why does Java use Stack and Heap memory?
– What kind of data goes into Stack vs Heap?
– Why are local variables stored in Stack?

2️⃣ When designing REST APIs, what should a developer consider besides writing endpoints?

Things like:
- API design and naming conventions
- Proper HTTP methods (GET, POST, PUT, DELETE)
- Error handling
- Validation
- Security
- Idempotency
- Versioning

3️⃣ What business problems do BPM platforms solve?

For example tools like Newgen or Pega help automate complex workflows such as:

- Loan approval processes
- Insurance claims workflows
- KYC verification pipelines
- Document approvals

Instead of hardcoding business flows, BPM engines orchestrate the process.

4️⃣ What exactly is HTTP and how is it different from WebSockets?

HTTP → Request/Response communication
WebSockets → Full duplex (two-way persistent connection)

Used in:
- Chat systems
- Live notifications
- Real-time dashboards

5️⃣ Design problem:

"Create a Spring Boot API that accepts a pin code and date, calls an external weather API, and returns weather data."

Which tests:
- Controller design
- Service layer
- External API calls
- DTO responses

Sometimes interviews remind us that strong fundamentals matter more than frameworks.
---
## 𝗝𝗮𝘃𝗮 𝗕𝗮𝗰𝗸𝗲𝗻𝗱 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 – 𝗜𝗻𝘁𝗲𝗿𝘃𝗶𝗲𝘄 𝗘𝘅𝗽𝗲𝗿𝗶𝗲𝗻𝗰𝗲
I recently appeared for a Java Backend Developer interview and wanted to share some of the challenging questions that were asked.
Sharing this here in case it helps others preparing for Java / Spring Boot backend roles.
𝗖𝗼𝗿𝗲 𝗝𝗮𝘃𝗮 (𝗗𝗲𝗲𝗽 𝗖𝗼𝗻𝗰𝗲𝗽𝘁𝘀)
- What happens internally in HashMap when two keys generate the same hash?
- How does ConcurrentHashMap achieve thread safety?
- Difference between Synchronized Collections and Concurrent Collections.
- What is the volatile keyword and how is it different from synchronization?
- Explain the Java Memory Model (JMM).
- Difference between Future and CompletableFuture.
- What are Parallel Streams and when should they not be used?
- What is a ClassLoader in Java and what are the different types?
𝗦𝗽𝗿𝗶𝗻𝗴 𝗕𝗼𝗼𝘁 / 𝗠𝗶𝗰𝗿𝗼𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀
- How does Spring Boot Auto Configuration work internally?
- Difference between @ComponentScan and @SpringBootApplication.
- Explain the Spring Bean Lifecycle.
- What are Circular Dependencies in Spring and how can they be resolved?
- Difference between @ControllerAdvice and @RestControllerAdvice.
- How would you implement Rate Limiting in a Spring Boot API?
𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 / 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲
- What is the N+1 Query Problem in JPA and how can it be solved?
- Difference between LAZY Fetching and EAGER Fetching.
- When should you use database indexing and when should you avoid it?
- How would you debug a slow SQL query in production?
𝗦𝘆𝘀𝘁𝗲𝗺 𝗗𝗲𝘀𝗶𝗴𝗻 𝗦𝗰𝗲𝗻𝗮𝗿𝗶𝗼
Design a system that can send millions of emails per day.
Discussion included:
- Message Queues (Kafka / RabbitMQ)
- Retry Mechanisms
- Dead Letter Queues (DLQ)
- Horizontal Scaling
- Logging and Monitoring
𝗣𝗿𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝗦𝗰𝗲𝗻𝗮𝗿𝗶𝗼
If multiple users update the same database record simultaneously, how would you prevent data inconsistency?
Discussion points:
- Optimistic Locking
- Pessimistic Locking
- Transaction Isolation Levels
---
## Spring boot Annotation cheat sheet
Spring Boot Annotations Cheat Sheet with use cases.😎

🚀 Spring Boot Quick - Reference
Overview🚀

1. @SpringBootApplication 📥: The Master Key—it launches your app, enables auto-config, and scans for beans.

2. @Configuration & @Bean 🛠️: The Blueprint—manually define and customize Java objects for Spring to manage.

3. Stereotypes (@Service, @Repository) 🏗️: The Layers—cleanly separate business logic from data access.

4. @RestController 🌐: The API Gateway—turns a simple class into a powerful web handler for JSON/XML.

5. @GetMapping / @PostMapping 🛤️: The Traffic Routes—shortcuts to map specific HTTP actions to methods.

6. @Autowired & @Qualifier 🧩: The Glue—automatically connects your beans together without manual new keywords.

7. @PathVariable & @RequestBody 📦: The Data Extractors—pull values from URLs and JSON bodies instantly.

8. @Entity & @Transactional 💾: The Database Shield—maps objects to tables and ensures safe data transactions.

9. @Value & @PropertySource ⚙️: The Settings—inject external configurations without hardcoding values.

10. @SpringBootTest & @MockBean 🧪: The Lab—load the full app context or use mocks to ensure high-quality code
---
## 🚀 All Spring Boot Annotations — One Cheat Sheet
I created a complete cheat sheet covering the most important Spring Boot annotations:
✅ Dependency Injection
✅ JPA & Data Access
✅ REST & Web
✅ Security
✅ Testing
✅ Configuration & Profiles
Perfect for developers and interview preparation.
🎁 Download full package for FREE here:
Also, I’ve opened all my packages for free — including Spring Boot, Microservices, and AI.
Let’s grow together 🚀
---
## Hi everyone ,
From today onwards, I’m starting a small series where I’ll share Spring Boot concepts the way we actually use them in real projects. No heavy theory, no copy-paste definitions — just practical understanding, useful for both
development and interviews.
Let’s start with the first thing we write in any Spring Boot project 👇

🔹 #SpringBootAnnotation — @SpringBootApplication
- What is it?
 @SpringBootApplication is the entry point of a Spring Boot application.
 It tells Spring Boot: “Start the application from here.”

- Why do we use it?
 Instead of writing multiple configurations, this single annotation does the job by combining:
@Configuration
@EnableAutoConfiguration
@ComponentScan
Less boilerplate, cleaner code.

- When do we use it?
 Every time we create a Spring Boot application — this is always the starting
point.

- Where do we use it?
On the main class, ideally placed in the root package so Spring can scan all components properly.

Real-world uses:
Auto-configures the embedded server (Tomcat).
Scans controllers, services, repositories.
Starts the entire Spring context.

🎯 Interview tip
 If your components are outside the base package, Spring won’t detect them unless you specify:
@ComponentScan("com.example")

I’ll be posting more Spring Boot annotations and project concepts in this series.
Let’s learn Spring Boot practically, not just for exams.
 If you’re learning Spring Boot or revising for interviews, follow along 👍
---
## 👉 Spring Boot Annotations Overview: Mastering Your Development

- Ready to dive into the world of Spring Boot? Here’s a quick overview of key annotations that can supercharge your development process.

→ @SpringBootApplication combines essential configurations for your app to run smoothly.

→ @EnableAutoConfiguration automates settings based on your classpath and beans.

→ @ComponentScan specifies which packages the Spring Framework should scan for components.

→ @RestController simplifies REST API development by combining @Controller and @ResponseBody.

→ @RequestMapping maps HTTP requests to specific controller methods for seamless navigation.

→ @Autowired allows Spring to manage dependencies automatically, no more manual wiring!

→ @Qualifier helps when multiple candidates exist for dependency injection, ensuring the right one is chosen.

→ @Bean indicates that a method produces a bean to be managed by the Spring container.

→ @ConfigurationProperties binds external configurations to your application, improving flexibility.

→ @Scheduled enables you to run methods at specific intervals, perfect for background tasks.

- What annotation are you most excited to use in your next project? Let's discuss in the comments!

Follow Hamza Ullah to explore more about software engineering, AI, leadership, and startups.

👇 Drop a comment, like, and repost if this was helpful!

## Spring Boot alone won’t get you into MAANG-level backend roles (30LPA+)
These are the questions that will.👇

📍 Concurrency & Threading
1/ How do you configure thread pools in Spring Boot under high load?
2/ How do you decide thread count for CPU vs IO tasks?

📍System Design Thinking
3/ Your system goes down for 5 mins, how will you process backlog + live traffic?
4/ How do you design retry + backoff mechanisms?

📍Spring Internals
5/ Why does injecting a @RequestScope bean into singleton fail?
6/ How does Spring manage bean lifecycle?

📍Kafka & Messaging
7/ How do you retry failed messages 5 times?
8/ What is DLQ and when should you use it?

📍Low-Level Design
9/ Design a flood-fill system (MS Paint fill tool)

📍DSA asked alongside backend

📍Backend Fundamentals
12/ SQL vs NoSQL- tradeoffs?
13/ What are idempotent APIs?
14/ How do microservices communicate securely?
---
## 5 Rounds. 38 LPA. The Goldman Sachs Interview Breakdown
Role: Java Backend Developer
Application Mode: Direct Application

𝗥𝗼𝘂𝗻𝗱 𝟭: 𝗢𝗻𝗹𝗶𝗻𝗲 𝗔𝘀𝘀𝗲𝘀𝘀𝗺𝗲𝗻𝘁
 - Problem 1: Validate a Custom Expression
 - Given a string with {, }, and *, where * can be {, }, or empty, validate if the expression is balanced.
 - Problem 2: K Most Frequent Words
 - Return top-k frequent words sorted by frequency and lexicographical order.

𝗥𝗼𝘂𝗻𝗱 𝟮: 𝗗𝗦𝗔 + 𝗝𝗮𝘃𝗮 𝗖𝗼𝗻𝗰𝗲𝗽𝘁𝘀
 - Q1: Reverse Linked List in Pairs, Input: 1 → 2 → 3 → 4 → 5, Output: 2 → 1 → 4 → 3 → 5
 - Q2: Core Java Topics
 - == vs equals()
 - How HashMap works internally
 - Collision handling (LinkedList vs Tree in Java 8+)
 - Load factor reasoning (0.75)
 - Java Memory Model
 - Thread safety & concurrency

𝗥𝗼𝘂𝗻𝗱 𝟯: 𝗦𝗽𝗿𝗶𝗻𝗴 𝗕𝗼𝗼𝘁 + 𝗟𝗼𝘄-𝗟𝗲𝘃𝗲𝗹 𝗗𝗲𝘀𝗶𝗴𝗻
 - Q1: Rate Limiter Design
 - Max 5 requests/user/min
 - Q2: Spring Boot Deep Dive
 - @Component vs @Service vs @Repository
 - Bean scopes and lifecycle
 - Startup process of Spring Boot
 - Internals of @Transactional and pitfalls

𝗥𝗼𝘂𝗻𝗱 𝟰: 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 + 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗢𝗽𝘁𝗶𝗺𝗶𝘇𝗮𝘁𝗶𝗼𝗻
 - Q1: SQL Query Optimization
 - Indexed WHERE/JOIN fields
 - Removed SELECT *
 - Used EXPLAIN
 - Discussed denormalization & slow log analysis
 - Q2: API Gateway Auth & Security
 - OAuth vs JWT
 - How token expiration works
 - Can JWTs be invalidated?
 - Refresh token flows

𝗥𝗼𝘂𝗻𝗱 𝟱: 𝗛𝗥 + 𝗖𝘂𝗹𝘁𝘂𝗿𝗲 𝗙𝗶𝘁
 - Why Goldman Sachs?
 - Handling pressure & deadlines?
 - Experience with global teams?
 - Career growth plans?

Pattern: Goldman doesn’t test topics. They test thinking depth.
---
## Recently attended a Java Developer interview and thought of sharing the actual questions that came up.

Posting this purely from memory not a prepared list in case it helps someone preparing 😊

Some of the things we discussed:

1. How @RequestBody works internally in Spring Boot
2. End-to-end flow of how an Entity class eventually becomes a table in the database (JPA → Hibernate → SQL)
3. Why we use @Service and @Repository, what Spring does differently with them internally
4. What happens if both @Service and @Repository are used on the same class
5. Thread lifecycle - especially NEW vs RUNNABLE states
6. Fail-Fast vs Fail-Safe iterators (with real examples)
7. Why ConcurrentHashMap exists and when to use it
8. What an API Gateway does in a microservices setup

Coding / hands-on questions:

9. 2Sum problem (follow-up: 3Sum)
10. Filtering employees above a certain salary using Java Streams
11. Finding average salary using Streams
12. Grouping employees by department (Streams + follow-up in SQL)
13. Self join in SQL and real use cases

Java basics check:

14. Output and execution order of try–catch–finally blocks
After this, they deep-dived into Microservices and Kafka, which I’ll probably cover in another post.

It was a good learning experience revisiting the fundamentals.
😊
---
## 🚀 Spring Boot Interview Preparation

One of my friends recently attended an interview at Accenture for the Customer Support Engineer role. Sharing some core and trending Spring Boot questions that were asked and discussed in the interview. These questions are very helpful for anyone preparing for Java / Spring Boot interviews (3–5 years experience).

Most Asked Questions:

1. What is Spring Boot and how is it different from the Spring Framework?
2. How does Spring Boot Auto Configuration work internally?
3. What is the role of the @SpringBootApplication annotation?
4. What is the difference between @Component, @Service, and @Repository?
5. What is the difference between @Controller and @RestController?
6. What is Spring Boot Starter and why is it used?
7. What is Spring Boot Actuator and what are its common endpoints?
8. What is the difference between @Autowired and @Qualifier?
9. What happens if multiple beans of the same type exist?
10. What are Bean scopes in Spring?
11. What is the difference between BeanFactory and ApplicationContext?
12. What is Dependency Injection in Spring?
13. What is the difference between @Value and @ConfigurationProperties?
14. What is @RequestBody and @ResponseBody?
15. What is the difference between @PathVariable and @RequestParam?
16. How do you implement global exception handling in Spring Boot?
17. How do you validate request data using @Valid / @Validated?
18. What is Spring Data JPA?
19. What is the N+1 problem in Hibernate?
20. What is the difference between Lazy and Eager fetching?
21. What is the difference between save() and saveAndFlush() in JPA?
22. What is DTO and why is it used?
23. How do you implement pagination and sorting in Spring Boot?
24. How do microservices communicate with each other?
25. What is API Gateway in microservices architecture?
26. What is the Circuit Breaker pattern?
27. What is the Bulkhead pattern?
28. How do you implement JWT authentication in Spring Boot?
29. What is method-level security in Spring Security?
30. How do you secure Actuator endpoints in Spring Boot?

Practicing these questions will help a lot if you are preparing for Spring Boot / Microservices interviews.

💡 If you are preparing for interviews, feel free to connect and practice together. Let’s grow together! 💯
---
## Complete Roadmap to Become a Java Developer:

Learn these things (preferably) in the given order:

1. Core Java (fundamentals of Java programming language)
2. Maven
3. Spring Core, Spring MVC, and Spring AOP
4. Spring Boot and REST APIs (Restful Web Services)
5. Spring Data - JPA, Hibernate (with H2, MySQL, MongoDB and Redis)
6. Testing (JUnit 5, JPA Test, MockMVC, etc.)
7. Spring Security
8. Microservices and Spring Cloud
9. Docker and Kubernetes
10. Deployment of Spring Boot Apps on Cloud (AWS, Azure or Google Cloud)
11. Optional - Serverless, Batch processing with Spring, etc.

keep learning, keep sharing !
---
## 1. Why does a Spring Boot app consume more memory over time?
2. How do you detect bean initialization issues in large applications?
3. What happens if @PostConstruct throws an exception?
4. Why does @Value sometimes fail to inject properties?
5. How does Spring Boot decide the order of auto-configurations?
6. What are the risks of enabling too many Actuator endpoints?
7. Why does your app behave differently after scaling pods?
8. How does Spring Boot handle classpath scanning internally?
9. What causes duplicate bean registration in multi-module projects?
10. Why does your API return correct data but response time fluctuates?
11. How do you control thread usage in Spring Boot applications?
12. What happens when application.yml and application.properties both exist?
13. Why do custom exception handlers sometimes not trigger?
14. How do you handle large payloads without killing performance?
15. Why does Hibernate generate unexpected queries?
16. How do you debug a deadlock in Spring?
17. What happens if a BeanFactoryPostProcessor fails?
18. How do you avoid startup failure due to missing configs?
19. Why does Spring Boot retry DB connections on startup?
20. How do you manage feature toggles safely?
21. Why does @Cacheable sometimes not cache?
22. How does Spring Boot isolate environment-specific configs?
23. What causes classloader issues in fat JARs?
24. How do you safely reload configs without restarting?
25. Why does logging behave differently in prod vs local?
26. How do you handle partial failures in dependent services?
27. What is the real impact of using too many interceptors?
28. How do you prevent breaking changes during deployments?
29. Why does @ConfigurationProperties fail silently?
30. What Spring Boot decision has caused you a real production issue?

𝑶𝑹

All the best!
---
## Stop memorizing syntax and start breaking the framework.

23 sections into my Spring Boot journey, and my biggest takeaway isn't a line of code. It’s the shift from "How" to "Why."

I realized that if you don't understand the problem, the solution looks like magic. So, I slowed down to ask: Why does Spring Boot exist? What does a container solve that plain Java doesn't?

Here is how that "clicking" moment happened:
 The Core Foundation: I went back to the basics like OOP, Multithreading, and Lambdas. Without a strong Java core, Spring feels like a black box. With it, it becomes a powerful, predictable tool.

 The Data Evolution: I started with raw JDBC and PostgreSQL to feel the "pain" of manual CRUD and boilerplate. Moving to Hibernate/JPA after that wasn't just a lesson; it was a relief.

 The Mindset Shift (IoC & DI): Inversion of Control genuinely changed how I think about architecture. Letting the Spring container manage the bean lifecycle instead of manual instantiation is a total paradigm shift.

 The Modern Stack: It all converged with REST APIs, Spring Security, and Docker. Containerizing the app was the final piece of the puzzle ensuring that "it works on my machine" actually means it works everywhere.

 The Verdict: Moving from code that just "works" to code that is structured, scalable, and production ready. By letting the framework handle the repetitive plumbing, I can finally focus on what matters: Building the business logic.

Next up: A deep dive into the E-commerce backend I’m currently building with these tools! 🏗️
To my fellow backend devs: What concept took you the longest to really "get"? For me, the Bean Lifecycle was the final boss! 🛡️
TELUSKO
---
## Java Backend Interview Questions (4–5 Years Experience)

Sharing some practical Spring Boot / Java backend interview questions that focus more on real-world decision-making rather than just annotations. Helpful for developers preparing for backend interviews or strengthening fundamentals.

1. Why does a Spring Boot app consume more memory over time?
2. How do you detect bean initialization issues in large applications?
3. What happens if @PostConstruct throws an exception?
4. Why does @Value sometimes fail to inject properties?
5. How does Spring Boot decide the order of auto-configurations?
6. What are the risks of enabling too many Actuator endpoints?
7. Why does your app behave differently after scaling pods?
8. How does Spring Boot handle classpath scanning internally?
9. What causes duplicate bean registration in multi-module projects?
10. Why does your API return correct data but response time fluctuates?
11. How do you control thread usage in Spring Boot applications?
12. What happens when application.yml and application.properties both exist?
13. Why do custom exception handlers sometimes not trigger?
14. How do you handle large payloads without killing performance?
15. Why does Hibernate generate unexpected queries?
16. How do you debug a deadlock in Spring?
17. What happens if a BeanFactoryPostProcessor fails?
18. How do you avoid startup failure due to missing configs?
19. Why does Spring Boot retry DB connections on startup?
20. How do you manage feature toggles safely?
21. Why does @Cacheable sometimes not cache?
22. How does Spring Boot isolate environment-specific configs?
23. What causes classloader issues in fat JARs?
24. How do you safely reload configs without restarting?
25. Why does logging behave differently in prod vs local?
26. How do you handle partial failures in dependent services?
27. What is the real impact of using too many interceptors?
28. How do you prevent breaking changes during deployments?
29. Why does @ConfigurationProperties fail silently?
30. What Spring Boot decision has caused you a real production issue?
---
## Why “N+1 Query Problem” Can Kill Your Application Performance

Your API works fine…
Your database is healthy…

But your application is still slow.

You might be facing the N+1 Query Problem.

What is N+1 Problem?

It happens when your application makes:
 1 query to fetch a list
 N additional queries to fetch related data

So instead of 1 efficient query, you end up with N+1 database calls.

Simple Example

You fetch a list of 100 users:
SELECT * FROM users;

Then for each user:
SELECT * FROM orders WHERE user_id = ?;

Total queries = 101 instead of 1

Why It’s Dangerous

Hidden Performance Killer
 Works fine in development, fails at scale.
Increases DB Load
 More queries = more CPU, memory, latency.
Slows Down APIs
 Response time increases drastically with data size.

Where It Happens (Java World)
- Hibernate / JPA lazy loading
- Improper entity relationships
- Fetching nested data without optimization

How to Fix It
Use JOIN FETCH in JPA
Use DTO projections
Apply batch fetching
Analyze queries with logs (hibernate.show_sql)

Pro Tip:
 If your API gets slower as data grows…
 It’s often not your logic - it’s your queries.

In backend systems, efficiency is not just about code - it’s about how you talk to your database.

Have you ever debugged an N+1 issue in production?
---
## Spring Data Interview Question - Identify & Optimize Slow SQL Queries

Scenario

Your application is experiencing high latency and database CPU spikes.

You suspect inefficient SQL queries, but the system runs hundreds of queries per second, making it unclear which ones are the real bottlenecks.

You need a systematic approach to:

- Identify problematic queries
- Diagnose why they are slow
- Apply optimizations safely in production

Naive Query Example

SELECT * FROM todo
WHERE name = ‘Install FooTool’;

Potential issues:

- No index on name → full table scan
- SELECT * → unnecessary I/O for unused columns
- Query may run frequently → multiplied impact

How would you systematically identify slow SQL queries and optimize them in a production system?

Checkout the detailed solution:

Subscribe and join 6200 Java & Spring Boot devs :