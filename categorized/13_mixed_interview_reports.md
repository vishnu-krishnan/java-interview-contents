## 🚨 EY Java Full Stack Developer (L1) Interview – Questions Asked (4–6 YOE) 🔥

Sharing insights from a recent EY Java Full Stack Developer – L1 interview experience (shared by a candidate).

If you're preparing for Java Full Stack / Spring Boot / Microservices roles, this will help you understand the real expectation level 👇

💼 Interview Format (1 Hour Round)
- Conceptual + Practical + Coding
- Strong focus on Microservices, Java 8, Spring Boot, Multithreading & SQL

Here are the actual questions asked:

🔹 Microservices & Architecture
- How do you handle fault tolerance in microservices?
- What design patterns are used in microservices architecture?
- Explain Circuit Breaker pattern. How have you implemented it using Resilience4j?
- What is CQRS pattern?
- Have you worked with Kafka or RabbitMQ?

🔹 Spring Boot & Security
- Have you implemented RBAC using Spring Security?
- Difference between "@Qualifier" and "@Primary"
- Which annotation injects values from application.properties / application.yaml?
- How do you use those constants inside the service layer?

🔹 Java & Multithreading
- Difference between Thread and Runnable
- If two threads are using shared resources, how do "wait()" and "run()" differ?

🔹 Coding Round (Java 8 / Brute Force)
Write a program to print combinations that sum to 6

Input:
nums = [2, 4, 3, 3, 5, 7]
target = 6

Output:
[[2,4], [3,3]]

🔹 SQL
- Write a query to find employees earning more than the average salary of their department
- Primary Key vs Unique Key

💡 Key Insight:
This round clearly checks:
✔ Real microservices implementation experience
✔ Practical circuit breaker usage
✔ Strong multithreading fundamentals
✔ Solid SQL understanding

If you're targeting strong product-based or consulting companies, prepare at this depth.
---
## Recently I attended a Java Backend Developer interview (4+ years experience). Sharing some of the questions that were asked. Hope it helps others preparing for similar roles.

Round 1 – Coding + Core Java + Spring Boot
Duration (40 mins)

- Find the first non-repeated character in a string
- OOPs concepts in detail (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Coding question: Can a private method in parent be overridden in child? Explain with code
- Method overloading in child class – coding example
- Connection Pooling in Java / Spring Boot
- Spring Boot Bean Lifecycle
- Difference between @Component and @Service

Round 2 – Advanced Java + Coding + System Design
(Duration 1hr 20 minutes)

- OOPs concepts discussion
- REST APIs concepts and best practices
- Type Erasure in Generics (Java Generics concept)
- Coding problem: Sort strings by length, and if length is same sort alphabetically
- What will be the output of:
"String str = "java.code"
"str.replaceAll(".", "__");"
- Immutable class in Java – how to design
- Singleton class implementation
- In constructor, can we write logic other than initializing fields?
- Design patterns used in your projects
- Fault tolerance – Circuit Breaker pattern in Microservices
- SQL Question: Find average salary and 2nd highest average salary
- How to use @EmbeddedId in JPA
- How to resolve NoUniqueBeanDefinitionException.

And many cross questions.

Round 3 - Hackerrank Assessment

- Functionality implmentation based on Oops concept successfully completed.
- Medium level question 4 out of 7 test case passed.

Round 4 - Management round.
Project Related and tech stack related questions.

Despite the good interview where 80-85% questions i answered correctly I was not able to clear.

Learning - Sometimes your best interview also can lead to rejection so just focus on next interview rather than thinking about previous Results 😊
---
## I’m sharing my recent interview experience for a Java Developer role (Java, Spring Boot, Microservices).

Sharing some of the questions that were asked 👇

First, I introduced myself and explained the projects I have been working on in detail. After that, I was asked:

𝗦𝗽𝗿𝗶𝗻𝗴/𝗗𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝗰𝘆 𝗜𝗻𝗷𝗲𝗰𝘁𝗶𝗼𝗻
→ What design patterns are used in your project?
→ What is Dependency Injection?
→ Different approaches to inject beans in Spring
→ Which injection method is recommended and why?
→ Bean lifecycle in Spring
→ Bean scopes and the default scope
→ Difference between ApplicationContext and Spring Context
→ What is the @Configuration annotation?

𝗠𝗶𝗰𝗿𝗼𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀
→ How do microservices communicate with each other?
→ RestTemplate vs WebClient
→ What is Feign Client?
→ Why might Feign not always be recommended for production environments?

𝗖𝗼𝗿𝗲 𝗝𝗮𝘃𝗮/𝗠𝘂𝗹𝘁𝗶𝘁𝗵𝗿𝗲𝗮𝗱𝗶𝗻𝗴
→ What is the volatile keyword?
→ Different ways to create threads
→ Are threads created manually in production-level applications?

𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻𝘀
→ Internal working mechanism of HashMap
→ Difference between Collection vs Collections

𝗖𝗼𝗱𝗶𝗻𝗴 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻𝘀
→ Count character frequency in a string and print in ascending order
→ Print all substrings of a given string

𝗦𝗤𝗟
→ Basic data retrieval query

Most of the discussion focused on strong fundamentals and real project experience, rather than purely theoretical knowledge.
---
## Java Backend Developer - 1st Round Interview

These 20 questions are being asked in interviews right now.

Interviewers are evaluating: Core Java fundamentals + Spring framework expertise + Database fundamentals + Practical problem-solving ability.

Here are 20 questions candidates are encountering in Round 1:

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
## Java was always the "it starts slow but runs fast" language.

For years, that was the trade-off we accepted. You build your Spring Boot microservice, deploy it to AWS, and watch the JVM spend 10+ seconds warming up before it can handle its first request properly.

In serverless and auto-scaling scenarios? That warm-up time was a dealbreaker.

I've spent the last 4+ years building Java/Spring Boot microservices on AWS. I've felt this pain firsthand — watching Lambda cold starts eat into our SLAs, or seeing Kubernetes pods take forever to pass readiness probes during traffic spikes.

Java 25 LTS changes the game.

Here's what's different:

→ AOT Method Profiling (JEP 515) captures how your code runs during a training phase, then reuses that profile on every subsequent startup. The JIT compiler generates optimized native code immediately — no more slow interpretation phases.

→ Compact Object Headers (JEP 519) shrink every Java object header from 96-128 bits to 64 bits. Real-world result: 10-20% memory savings across applications managing large object volumes.

→ The numbers: Applications with AOT cache are hitting first-request readiness in ~3 seconds vs. 10+ seconds on Java 21. That's a ~70% reduction in initial latency. Oracle's Helidon team reported ~70% performance gains just by upgrading from JDK 21 to 25 — with zero code changes.

→ On AWS Lambda specifically: Java 25 replaces traditional CDS with AOT caches by default. Combined with SnapStart, Spring Boot functions now show P50 cold starts around 182ms. Java is now directly competing with Node.js and Python for serverless.

For teams running Kubernetes: AOT cache enables 50-60% more pods per node due to lower CPU and memory requirements at startup. That's a direct infrastructure cost reduction.

The warm-up tax is over. Java 25 doesn't just catch up — it makes the JVM a genuine contender for latency-sensitive, scale-to-zero workloads.

If you're still on Java 21 and running cloud-native workloads, the migration path is clear.
---
## 🚀 Accenture Interview Experience | Java Backend Developer
Recently, I had the opportunity to interview with Accenture for a Java Backend Developer role. It was a valuable learning experience with discussions covering Java fundamentals, Spring Boot, System Design, SQL, AWS, and a coding round.
Here are some of the topics/questions discussed during the interview:
🔹 Java & OOP Concepts
 - Aggregation vs Composition
 - this vs super keyword
 - Why runtime polymorphism is used in method overriding
 - Fail-Fast vs Fail-Safe iterators
 - sleep() vs wait() in multithreading
 - Liskov Substitution Principle (SOLID principles)
🔹 Java 8 Features
 - map() vs flatMap()
🔹 Concurrency / Multithreading
 - ExecutorService and its important methods
 - Thread lifecycle and thread pool concepts
🔹 Spring / Backend Concepts
 - IoC Container (Inversion of Control)
 - Spring Bean Lifecycle
 - AOP and how it was implemented in my project
🔹 Database
 - Normalization and its types
 - Writing optimized SQL queries
🔹 System Design / Architecture
 - Design patterns used in real projects
 - Saga Design Pattern in microservices
🔹 Cloud
 - Discussion on AWS services used in backend applications
🔹 Coding Question
 - Convert Infix Expression to Postfix Expression
🔹 Project Discussion
 - Detailed questions about project architecture, implementation approach, and real-world scenarios.
Overall, the interview focused on core Java concepts, practical backend development knowledge, and real project experience.
Grateful for the opportunity and the learning from this experience. Looking forward to more such technical discussions and growth opportunities!
---
## 🚀 Deloitte Interview Experience | Java Backend Developer

Recently, I had the opportunity to interview with Deloitte for a Java Backend Developer role. It was a great learning experience with discussions covering Java, Spring Boot, System Design, SQL, and AWS, along with a coding round.

Here are some of the topics/questions discussed during the interview:

🔹 Java & OOP Concepts
 - Aggregation vs Composition
 - this vs super
 - Why runtime polymorphism is used in method overriding
 - Fail-Fast vs Fail-Safe iterators
 - Sleep vs Wait in multithreading
 - Liskov Substitution Principle (SOLID principle)

🔹 Java 8
 - Map vs FlatMap

🔹 Concurrency
 - ExecutorService and its important methods

🔹Testing
 - Which version for Junit used in your project.

🔹 Spring / Backend
 - IoC Container (Inversion of Control)
 - Spring Bean Lifecycle
 - AOP and how it was implemented in my project

🔹 Database
 - Normalization and its types
 - Difference between View and Procedure

🔹 System Design / Architecture
 - Design patterns used in projects
 - Saga Design Pattern

🔹 Cloud
 - AWS related discussion

🔹 Coding Question
 - Convert Infix Expression to Postfix Expression

🔹 Project Discussion
 - Detailed questions about project architecture, implementation, and real-world scenarios

Overall, it was a very insightful interview focusing on practical understanding, real project experience, and core fundamentals.

Grateful for the opportunity and the learning from this experience. Looking forward to more such discussions!
---
## 🚀 Java Backend Interview Experience (4+ Years Experience)

Today I attended a technical interview for a Java Backend / Microservices role, and these were the key topics the interviewer focused on.

Sharing this for developers preparing for Java + Spring Boot interviews.

📌 Core Java
- OOPs with real-world examples
- HashMap internal working
- Thread Lifecycle in Java
- Runnable vs Callable
- Deadlock & How to avoid Deadlock
- Garbage Collection
- Checked vs Unchecked Exceptions
- Custom Exception

📌 Spring Framework
- Spring Boot fundamentals
- @SpringBootApplication annotation
- @Component vs @Service vs @Repository
- DispatcherServlet
- Global Exception Handling
- Spring Security

📌 Database & SQL
- Hibernate / JPA
- Transaction Management
- Indexing
- Pagination
- Lazy Loading vs Eager Loading
- Primary Key vs Foreign Key
- Surrogate Key
- Function vs Procedure

📌 Microservices Architecture & Design Pattern
- Microservice vs Monolith Architecture
- How Distributed Systems Communicate
- API Gateway
- Circuit Breaker Pattern
- Event-Driven Architecture
- Design Pattern used in your project and sample code (Singleton)

📌 Messaging Systems
- Kafka
- Kafka vs RabbitMQ

📌 DevOps
- Docker
- Image vs Container

📌 Production Scenario
- Handling API Slowness in Production

💡 Observation: Modern backend interviews are heavily focused on Core Java fundamentals, concurrency, microservices architecture, and real production debugging scenarios.

If you are preparing for Java backend interviews, these topics are must-know.

- What are the most challenging questions you faced in your recent interviews?
---
## 🎯 Interview Experience – Java Backend Developer
Yesterday, I attended an interview for the Java Backend Developer role.
Below are some of the key questions that were asked 👇

🔹 Core Java
 1️⃣ Tell me about yourself.
 2️⃣ Difference between ArrayList and LinkedList ?
 3️⃣ What are java 8 features and explain functional interface?
 4️⃣ Inheritance and where you use functional interface?
 5️⃣ About Garbage collections and where you stored unwanted objects?
 6️⃣ Why Java doesn’t support multiple inheritance with classes?
 7️⃣ Difference between Abstract Class and Interface?
 8️⃣ Difference between HashMap and Concurrent HashMap ?

🔹 Spring Boot:
 9️⃣Explain Spring Bean lifecycle (init & destroy)
 🔟 Difference between Spring Boot Application vs Spring Boot Microservice?
 1️⃣1️⃣ Global exception handling using @ControllerAdvice
 1️⃣2️⃣ Difference Between Authentication and Authorization ?
 1️⃣3️⃣ JWT authentication & OAuth2 in microservices
 1️⃣4️⃣ Internal working of REST API in Spring Boot?
 1️⃣5️⃣HTTP Status Codes Explanation: 200, 300, 201, 400, 500, 404
 1️⃣6️⃣ When do we identify 500 – Internal Server Error?

🔹 SQL
 1️⃣7️⃣ Constraints in SQL ?
 1️⃣8️⃣ Write a Query add a new table with existing table without changes in old table?
 1️⃣9️⃣ Write a Query to find 2nd highest salary ?

🔹 Coding Questions:
 2️⃣0️⃣ Sorting of two Array Lists ?
 2️⃣1️⃣ Write code find the 2nd Non-Repeating Character? Ex: Programming

Thanks for reading!

If you find these interview questions helpful, please feel free to connect with me for more interview-related posts.

Do share your feedback in the comments. Your comments and suggestions are always welcome.
---
## Interview Experience – L1 & L2

(Java | Spring Boot | AWS | Microservices - 7 YOE)

🔹 L1 – Technical Round

- Introduction and detailed project explanation
- Recent technical challenges faced at work and how it was resolved
- Asynchronous programming
 Follow-up: Difference between CompletableFuture and Stream API
- Rate limiting – explanation and whether it was used in project
- Design a system with high throughput and better performance
- Database optimization – sharding vs partitioning
- Read-heavy vs write-heavy systems
 How to design DB for both requirements
- DB Schema creation & maintenance process - Liquibase usage in deployment
- Caching mechanism used in project
- CI/CD hands-on experience
 GitLab CI/CD runner
 Dockerfile explanation
- SSO login process
- AWS services used in the project(follow-up questions on RDS Replication)

🔹 L2 – Advanced Round

- Detailed project architecture explanation
- Spring Boot auto-configuration
- Observability
 Integration of Prometheus
 Integration of Micrometer in Spring Boot
- API Gateway usage in the project - all key features explanation
- Token handling
 Where tokens are stored
 Difference between token in cookie vs header
 Which is more secure and why?
- NoSQL database usage in project
 - Design patterns used in the project and reasoning behind them
- Sidecar observability pattern (suggested area to explore further)
- Pull Request - Maximum recommended lines of change
- Kafka experience
 Since I worked with SQS: explained SQS implementation in Spring Boot - - JUnit version and Mockito usage
- SAML assertion in SSO login flow
---
## 🚨 Suppose you are in a Java Backend Interview and the interviewer asks:
“If I ask you to create 100,000 threads in Java — how will you do it?”

Most candidates smile confidently 😎 and write this:

for (int i = 0; i < 100000; i++) {
 new Thread(() -> System.out.println(Thread.currentThread().getName())).start();
}

💥 But soon —
They get greeted with this beauty:
java.lang.OutOfMemoryError: unable to create new native thread

🧠 Why does this happen?
- Each traditional thread in Java is OS-managed and consumes around 1 MB of stack memory.
- So 100K threads ≈ 100 GB memory! 😱 Clearly… not scalable.

💡 Enter Virtual Threads (Java 21)
- Java 21 introduced Virtual Threads — lightweight threads managed by the JVM, not the OS.
- They’re part of Project Loom, designed to handle massive concurrency without memory overhead.
- Each virtual thread takes only a few KB of memory and is multiplexed over a small pool of platform threads.

⚙️ How to create 100K Virtual Threads easily

public class VirtualThreadDemo {
 public static void main(String[] args) throws InterruptedException {
 for (int i = 0; i < 100_000; i++) {
 Thread.startVirtualThread(() -> {
 System.out.println(Thread.currentThread());
 });
 }

 Thread.sleep(2000); // Wait for threads to complete
 }
}

✅ Output:
- You’ll see all 100K threads running smoothly — no OutOfMemoryError.
- Each thread runs concurrently, lightweight, and efficiently managed by the JVM.

🧩 Why Virtual Threads are a Game Changer
🚀 Handle massive concurrency with minimal memory
🧵 Ideal for blocking I/O operations (like DB calls or HTTP)
🔄 Seamlessly works with existing Java thread APIs
⚡ No need to re-architect your app for async frameworks