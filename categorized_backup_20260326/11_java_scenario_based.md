## 🔹 Interview Question: What is the transient keyword in Java?
Me:
The transient keyword in Java is used to indicate that a field should NOT be serialized.
🧠 First, what is Serialization?
Serialization is the process of converting an object into a format (byte stream / JSON) so that it can be:
- Saved to a file
- Sent over the network
- Stored in a database
🎁 Real-Life Analogy
Imagine you want to send a gift to a friend who lives far away.
You:
📦 Pack the gift
🔒 Seal the box
🚚 Send it via delivery
This process is similar to Serialization.

When your friend receives it:
📦 Opens the box
🎁 Restores the gift
This is Deserialization.

💻 Example in Java
public class Employee {
 private long id;
 private String name;
 private String department;

 private transient BigDecimal salary;

 // getters & setters
}
Here, the salary field is marked as transient.
- This means:
It will NOT be included during serialization
After deserialization, its value will be default (null / 0)
⚙️ Where is this useful?
We use transient when:
- Data is sensitive (e.g., salary, passwords)
- Data is temporary / derived
- Data is not required to persist or transfer

🔄 Example with JSON (Jackson / Gson)
When converting object → JSON:
{
 "id": 1,
 "name": "John",
 "department": "Engineering"
}
- Notice that salary is NOT present.
🚀 Key Takeaway
transient helps control what should NOT travel with your object when it is serialized.
A small keyword, but very important in real-world backend systems and interviews.
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

Result - REJECTED .

Despite the good interview where 80-85% questions i answered correctly I was not able to clear.

Learning - Sometimes your best interview also can lead to rejection so just focus on next interview rather than thinking about previous Results 😊

Hope this helps Java developers preparing for backend interviews.
---
## Want Cleaner, Faster Java Code? Start Here.
---
## Most Spring Boot apps I review have the same problems.

Not complex architecture issues. Basic mistakes that compound over time and make the codebase painful to work with.

Here are 7 that come up again and again:

1. Field injection instead of constructor injection
2. Business logic stuffed inside controllers
3. Try-catch scattered everywhere instead of a global exception handler
4. No database indexes on filtered columns
5. Hardcoded config values baked into the code
6. One config file for all environments
7. Unit tests only, no integration tests

The fix for each one takes less than 30 minutes.

The cost of ignoring them shows up months later when onboarding slows down, bugs slip through, and deployments break.

Which of these have you seen in production code?
---
## JAVA INTERVIEW SCENARIO:

The interviewer says:

“Let’s see how you think about real Java behavior, not just code.”

- Your HashMap suddenly starts behaving incorrectly in production. Why?

Answer:
- equals() and hashCode() not implemented properly
- Mutable keys being modified after insertion
- High hash collisions degrading performance
- Using non-thread-safe HashMap in concurrent environment
---
## 2) Your Java application shows high GC activity and performance drops. Why?

Answer:
- Excessive object creation increasing GC pressure
- Short-lived objects flooding the heap
- Improper memory allocation patterns
- Large objects frequently created and discarded
---
## 3) Your application sometimes processes the same request twice. Why?

Answer:
- Retry logic without idempotency
- Duplicate message processing in async systems
- Network timeouts causing re-execution
- Missing request deduplication logic
---
## This is what real Java interviews look like.

They don’t test syntax.
They test how you reason about real-world problems.

Which one would you struggle to explain?

I’ll share the detailed Java and Spring boot Questions and Answers PDF with interested folks.
---
## 𝗣𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝘄𝗮𝘀 𝘀𝗹𝗼𝘄.
API latency went from 180ms to 14s.
No memory leak. No deadlock. Logs looked clean.

One line looked harmless:
orders.forEach(o -> o.getItems().size());

But Hibernate did this behind the scenes:
𝗤𝘂𝗲𝗿𝘆 𝟭: fetch all orders
𝗤𝘂𝗲𝗿𝘆 𝟮..𝗡: fetch items for each order
For 100 orders, that became 101 queries.
That hidden blast radius is called the 𝗡+𝟭 𝗤𝘂𝗲𝗿𝘆 𝗣𝗿𝗼𝗯𝗹𝗲𝗺.

𝗪𝗵𝘆 𝘁𝗵𝗶𝘀 𝗯𝘂𝗴 𝗶𝘀 𝗱𝗮𝗻𝗴𝗲𝗿𝗼𝘂𝘀
It passes in dev with small data.
It fails in production with real volume.
You don’t see it in code review unless you check generated SQL.

𝟱 𝗽𝗿𝗮𝗰𝘁𝗶𝗰𝗮𝗹 𝘄𝗮𝘆𝘀 𝘁𝗼 𝗳𝗶𝘅 𝗡+𝟭
① 𝗝𝗢𝗜𝗡 𝗙𝗘𝗧𝗖𝗛
Use when parent + child data is always needed in one call.
② 𝗘𝗻𝘁𝗶𝘁𝘆𝗚𝗿𝗮𝗽𝗵
Declarative fetch strategy. Cleaner than JPQL in many repository methods.
③ 𝗕𝗮𝘁𝗰𝗵𝗦𝗶𝘇𝗲
Converts many per-row child fetches into batched IN queries.
④ 𝗗𝗧𝗢 𝗣𝗿𝗼𝗷𝗲𝗰𝘁𝗶𝗼𝗻
Best for read-only APIs and high-performance response models.
⑤ 𝗦𝗨𝗕𝗦𝗘𝗟𝗘𝗖𝗧
Useful when you want predictable parent-child loading behavior.

𝗤𝘂𝗶𝗰𝗸 𝘀𝗮𝗳𝗲𝘁𝘆 𝗻𝗲𝘁
Add this in every app:
hibernate.default_batch_fetch_size=25
Not a full cure, but a strong guardrail.

Connect: Amaan Nirban

If this helped, save it before your next backend interview.
What’s the worst “works in dev, fails in prod” Hibernate issue you’ve seen?
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
## JAVA INTERVIEW SCENARIO:

The interviewer says:

“Let’s see how you debug real problems in Java.”

- Your Java service starts throwing OutOfMemoryError even though heap size looks sufficient. Why?

Answer:
- Memory leak due to objects being referenced (not eligible for GC)
- Large number of objects created and retained in collections
- Improper use of caches without eviction
- High GC pressure causing memory not being freed efficiently
---
## 2) Multiple threads update shared data and results become inconsistent. Why?

Answer:
- Lack of synchronization (race condition)
- Non-thread-safe data structures used
- Missing locks or improper concurrency control
- Visibility issues (no use of volatile or proper synchronization)
---
## 3) Your application becomes slower after increasing thread pool size. Why?

Answer:
- Context switching overhead increases
- Threads competing for limited resources (CPU, DB connections)
- Lock contention increases
- More threads ≠ better performance in CPU-bound tasks
---
## This is what real Java interviews look like.

They don’t test syntax.
They test how you think when systems behave unexpectedly.

Which one have you faced in real scenarios?

 I’ll share the detailed Pdf with interested folks.
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
## 🚨 Questions asked in my Mastercard First Round Interview (for Backend Developer) — and trust me, this was NOT basic 👇

If you’re preparing for product-based companies, this is your reality check.
💡 They didn’t just test theory — they went deep into real-world system design, Kafka, and clean code practices.

Here’s what was covered:
🔥 API Gateway & Authentication flow
🔥 Authentication vs Authorization (with practical use cases)
🔥 Microservices architecture discussion
🔥 @Transactional → what actually rolls back? (tricky!)
🔥 SAGA pattern & distributed transactions
🔥 Garbage Collector internals
🔥 Caching strategies (Redis, cache-aside)

⚡ Kafka Deep Dive:
Delivery semantics (at least once, exactly once)
Consumer failure handling
DLQs (Dead Letter Queues)
Schema Registry
Kafka vs ActiveMQ

🧠 Design & Coding:
Identify problem in if-else heavy code
Apply Strategy + Factory Pattern
Serialization & serialVersionUID
Making a class immutable
@ConditionalOnProperty usage

💻 Coding Question:
➡️ Find common elements in 2 lists
➡️ Optimize from O(n²) → O(n) using HashSet

⚔️ Java Concepts:
Default methods conflict in interfaces
Abstract class vs Interface (when to use what)

💬 What I realized:
- Interviews are no longer about “what you know”
- They are about “how you think in production systems”

🎯 If you’re preparing for companies like Mastercard, JPMorgan, etc:
Focus on:
✔️ Kafka + Event-driven architecture
✔️ System Design (SAGA, idempotency, retries)
✔️ Clean code & design patterns
✔️ Performance optimization mindset

💬 Comment “PREP” if you want a mock interview or detailed answers
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
## INTERVIEWER:
“Let’s forget theory for a moment.

I’ll give you real situations from Java production systems.
Tell me what might be happening.”

Here are the kinds of questions interviewers ask:

- Your HashMap suddenly starts performing very slowly with large data. What internal behavior could cause this?
- A ConcurrentModificationException appears randomly in production. What coding mistake might cause it?
- Your API response time increased after switching from ArrayList to LinkedList. Why?
- A static variable starts causing inconsistent data across requests. Why can static state be dangerous?
- Your application crashes with StackOverflowError. What kind of bug usually leads to this?
- An API endpoint creates thousands of objects per request and performance drops. What JVM behavior might explain this?
- Two threads updating the same object sometimes produce wrong values. What concurrency issue could this be?
- A HashSet suddenly starts allowing duplicates. What mistake might exist in the object class?
- Your application becomes slow after adding heavy logging statements. Why can logging affect performance?
- An API endpoint blocks the entire service during heavy traffic. What coding pattern might cause this?
- A Java Stream pipeline produces unexpected results in parallel execution. Why might this happen?
- Your application becomes unstable after introducing caching. What design mistake might exist?
- A background thread silently dies and stops processing tasks. Why might this happen?
- Your application creates too many threads and the server becomes unstable. What should be used instead?
- An API occasionally returns stale data even though the database is updated. What could be wrong?
- Your equals() method works but HashMap lookups fail. What method might be missing?
- After deploying on a multi-core machine performance actually drops. Why might that happen?
- A scheduled job suddenly runs multiple times instead of once. What configuration issue might cause this?
- A memory leak appears even though objects are no longer used. What references might still hold them?
- Your service becomes slower after introducing synchronized blocks. Why?

These questions test whether you understand
how Java behaves in real systems — not just syntax.

Which one would you struggle to answer in an interview?

Comment the number.

I’ll share the detailed Java and Spring boot Questions and Answers PDF individually with interested folks.
---
## How to Improve API Performance in Production

Many APIs work perfectly in development.
But once traffic grows, performance problems start to appear: slow responses, database overload, and high infrastructure costs.

Improving API performance is often about applying a few proven architectural patterns.

Here are 5 simple techniques that make a huge difference.

1. Pagination

Instead of returning thousands of records in a single request, split the data into pages.

Why it matters:
- Reduces payload size
- Improves response time
- Prevents memory pressure on servers

Example:
GET /users?page=1&size=20

2. Async Logging

Logging can become a hidden performance bottleneck if every request writes directly to disk.

Better approach:
- Write logs to a memory buffer
- Flush them to disk asynchronously

Benefits:
- Lower request latency
- Higher throughput
- Less blocking in the application

3. Caching

Not every request needs to hit the database.
Frequently accessed data can be stored in a cache layer such as Redis.

Typical flow:
- Try cache first
- If cache miss, query database
- Update cache with fresh data

Benefits:
- Faster responses
- Reduced database load
- Better scalability

4. Payload Compression

Large JSON responses increase network latency.
Compressing responses with gzip or brotli reduces payload size significantly.

Benefits:
- Faster downloads
- Reduced bandwidth usage
- Better performance for mobile users

5. Connection Pooling

Opening and closing database connections for every request is expensive.
Connection pools maintain reusable connections.

Benefits:
- Faster database access
- Reduced overhead
- Improved system stability under load

Final Thought:

Most API performance issues are not solved with more servers.

They are solved with better architecture.

Small improvements like caching, pagination, and connection pooling can transform the performance of your system.
---
## A Common Production Issue in Java Systems: Connection Pool Misconfiguration
One issue I’ve seen more than once in backend systems is database connection pool misconfiguration.
In many cases, everything works perfectly in development and QA.
But once real traffic hits production, APIs suddenly start slowing down.
The database is usually blamed first.
But often the real issue is how the application manages database connections.
Here are a few things that usually cause problems:
- Thread pool vs connection pool mismatch
If an application can handle hundreds of concurrent requests but the database pool only allows a small number of connections, many requests end up waiting. Over time this leads to latency and timeouts.
- Connection leaks
If connections are not properly released back to the pool, even a small leak can gradually exhaust available connections.
- Missing or poorly configured timeouts
Without proper timeouts, threads may block indefinitely waiting for a connection, which can affect the entire service.
- Lack of monitoring
Metrics like active connections, idle connections, and connection wait time can often reveal problems much earlier than CPU or memory metrics.
In many production systems, performance issues are not caused by complex bugs.
They happen when traffic, thread pools, and database connection pools are not balanced correctly.
Curious to hear from others working on backend systems:
What kind of resource bottlenecks have you encountered most often in production?
---
## INTERVIEWER:
“Pretend you’re the engineer on-call tonight.

Production just broke.

Let’s see how you think.”

Then the interviewer asks questions like these:

- Your Java API suddenly starts returning very slow responses after a traffic spike. What internal issue could cause this?
- A HashMap in your service sometimes loses data unexpectedly. What coding mistake could lead to this?
- After deploying a small change, the JVM memory usage suddenly doubles. What could explain this?
- Your application becomes unstable when too many threads are created dynamically. What is the underlying problem?
- A REST endpoint works fine with few users but crashes when thousands of requests arrive. Why might that happen?
- Your system occasionally returns partially updated data during concurrent requests. What concurrency issue might exist?
- A background job sometimes runs twice even though it was scheduled once. What might cause this?
- After adding caching, users start seeing outdated responses. What design issue might exist?
- Your Java service suddenly throws ClassCastException in production but not in testing. Why?
- An API endpoint suddenly starts consuming huge memory for a simple operation. What might be happening?
- A synchronized block added for safety starts slowing down the entire application. Why?
- Your application throws IllegalStateException under heavy traffic. What situation might cause this?
- A thread pool keeps growing but tasks are still delayed. What could be misconfigured?
- A microservice call blocks your main request threads for a long time. What should be investigated?
- Your application logs suddenly increase disk I/O and slow down the service. Why?
- A long-running loop accidentally blocks an important worker thread. What kind of issue is this?
- After enabling parallel processing, CPU usage spikes but throughput doesn’t improve. Why?
- Your service sometimes processes the same request twice. What design issue might cause this?
- A Java service deployed on multiple instances starts behaving inconsistently. What shared-state issue could exist?
- A small bug causes a recursive method to run indefinitely until the application crashes. What error does this lead to?

These questions test whether you can reason about
how Java systems behave in real production situations.

Which question would you find hardest in an interview?

Comment the number.

I’ll share the detailed Java and Spring boot Questions and Answers PDF with interested folks.
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
## Java behaves differently in Kubernetes than it does on your laptop.
I recently explored a few subtle JVM traps that can cause:
Unexpected latency spikes
Silent OOMKills
JVM silently choosing the wrong garbage collector
All without a single error in your logs.
It turns out JVM ergonomics and container limits don't always align the way we expect.
Wrote a short article breaking down what's happening under the hood — and the flags that fixed it.
Check here.

medium.com

Prominent academy
Prominent academyView company: Prominent academy
5K followers
2w • 2w Visible to everyone

🚫 4+YOE Java Developers - Still Getting Rejected by Zensar Technologies?
-----------------
Many developers clear basic Java questions, but struggle when interviews move to real engineering responsibilities.
Because companies like Zensar don’t just test syntax knowledge - they evaluate how well you design, build, review, and maintain enterprise backend systems.

⚠️ Where Most Candidates Fail
❌ Strong in Core Java basics, but weak in multithreading scenarios
❌ Know Spring Boot, but cannot explain microservice communication or failure handling
❌ REST APIs implemented, but API design principles are unclear
❌ Poor understanding of SDLC, code reviews, and engineering processes
This is why many developers with 5–10 years experience still fail backend interviews.

🎯 Scenario Interview Questions (Latest 2026)
1️⃣ Your microservice processes thousands of concurrent requests. How would you design a thread-safe caching mechanism that avoids race conditions and still maintains high throughput?
2️⃣ A Spring Boot service in production suddenly starts showing thread starvation under heavy traffic. How would you diagnose the root cause and redesign the concurrency model?
3️⃣ Two microservices update the same database record simultaneously, causing data inconsistency. How would you design a solution to maintain consistency without reducing performance?
4️⃣ A REST API used by multiple clients must evolve with new features. How would you introduce changes without breaking existing integrations?
5️⃣ Your application experiences database connection pool exhaustion during peak hours. How would you investigate and fix this issue?
6️⃣ A Spring Boot application deployed on cloud instances shows high latency only during specific traffic patterns. How would you identify the bottleneck?
7️⃣ Your system processes financial transactions and must ensure exactly-once processing. How would you design the backend to guarantee this behavior?
8️⃣ A stored procedure used by your application becomes the major performance bottleneck when data volume grows 10x. How would you redesign the solution?
9️⃣ Your service depends on three external APIs, and one of them becomes unreliable. How would you ensure your system remains stable?
🔟 After deployment, your application’s memory consumption continuously increases until it crashes. How would you identify and fix the root cause?
1️⃣1️⃣ You need to design a highly scalable REST API expected to handle millions of requests per day. What architectural decisions would you make?

Most developers prepare only coding questions, but real interviews evaluate engineering thinking and system understanding.
At Prominent Academy, we focus on:
- Scenario-based interview preparation
- Java + Spring Boot + Microservices depth
- Pay After Placement
So developers don’t just learn concepts - they learn how to apply them in real interviews and real systems.
📞 Call / WhatsApp: +91 93594 45862
---
## 🚀 Spring Boot 4.0: Writing Safer Code with Null Safety

One of the biggest causes of production bugs in Java applications is the infamous NullPointerException.

Modern Java development is moving toward explicit null safety, making our code more predictable and maintainable.

Instead of relying only on runtime checks, developers can design APIs that clearly define what can be null and what cannot.

Why this matters for backend systems:

🔹 Fewer Runtime Errors
By clearly defining nullable and non-nullable values, many issues can be caught early during development.

🔹 Cleaner API Design
Well-defined method contracts make the code easier for other developers to understand.

🔹 Better Code Readability
Annotations and clear patterns make the intent of the code obvious.

🔹 More Reliable Microservices
In distributed systems, predictable APIs reduce unexpected failures between services.

Modern Java practices combined with Spring Boot, Optional, and clear API design help developers build robust and production-ready backend systems.

Small improvements in code safety can prevent big problems in production. 🚀
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
## When a HashMap Quietly Turns Into a Red-Black Tree

Most developers learn that HashMap operations run in O(1) time.

But that assumption only holds when the hash function distributes keys well.

What happens when it doesn’t?

When multiple keys collide into the same bucket, the entries start forming a linked list.
And suddenly your lookup time degrades from O(1) → O(n).

In large systems, that can become a serious performance bottleneck.

Starting with Java 8, the JVM introduced an elegant safeguard.

When the number of entries in a single bucket grows beyond 8, the structure automatically transforms from a linked list into a Red-Black Tree.

This small internal change has a big impact:

- Worst-case lookup improves from O(n) → O(log n)
- Systems become more resilient to hash collision attacks
- Performance stays predictable even with poor hash distribution

But there’s an important detail many engineers miss.

This treeification only happens when the HashMap capacity is at least 64.

If the table is smaller, the JVM chooses to resize the map instead of converting the structure.

Why?

Because resizing usually redistributes the keys and eliminates the collision entirely.

📌 The takeaway:
A HashMap isn’t just a simple key-value store.
It’s a carefully engineered hybrid data structure that adapts dynamically to maintain performance.

Most engineers use HashMap every day.

Very few understand what happens inside the bucket when things go wrong.
---
## Only for backend engineers:

☕ Java:
- OOPs & SOLID principles.
- Collections Framework: Deep dive into HashMap, List vs Set, and their internal workings.
- Java 8 Features: Streams, Lambdas, Optional, Functional interfaces.
- Multithreading: Lifecycle, synchronized, volatile, and ExecutorService.
- Exception Handling: Design custom exceptions, manage try-catch-finally effectively.
- Memory Management: Stack vs Heap, Garbage Collection.

🌱 3. Spring Boot

- Core Annotations: Master the usage of @RestController, @Service, @Repository, etc.
- Spring Internals: Learn about starters, application.properties, and auto-configuration.
- JPA & Hibernate: Mapping entities, @Transactional, lazy vs eager fetching.
Error Handling: Implement @ControllerAdvice and @ExceptionHandler for centralized error handling.
- RESTful APIs: Create REST APIs with CRUD operations, use @Valid, DTOs, and proper HTTP status codes.
- Security Basics: Implement JWT authentication and role-based authorization.
Testing: Use @WebMvcTest, @DataJpaTest, and Mockito for testing controllers and repositories.

🏗️ 4. Low-Level Design (LLD)
- Focus on building scalable, maintainable, and clean software designs:
- Class-Based Design: Design scenarios like Parking Lot, BookMyShow, and similar use cases.
- Design Patterns: Learn core patterns such as Singleton, Strategy, Factory, Observer.
- SOLID Principles & Clean Architecture: Aim for maintainable code with proper separation of concerns.
- UML Diagrams: Use UML to showcase your design thinking process.

🏢 5. High-Level Design (HLD)
- System Thinking: Focus on scalability, fault tolerance, and handling high availability.
- Key Concepts: Load Balancers, Redis, Kafka, SQL vs NoSQL databases.
- System Design Scenarios: Work through designs like URL Shortener, WhatsApp, Instagram, Rate Limiter.
- API & DB Design: Understand sharding, partitioning, and rate-limiting strategies.
- Trade-offs: Be prepared to discuss design trade-offs and justify your decisions.

Resources:
Spring Boot from Basics to Advanced (All Videos are in English)

High Level Design from Basics to Advanced (Some Initial Videos are in Hindi, rest in English)

Low Level Design from Basics to Advanced (Some Initial Videos are in Hindi, rest in English)

JAVA from Basics to Advanced (All Videos are in English)

JUnit5:
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
## YOU'RE IN A JAVA INTERVIEW.

The interviewer asks:

"Your Java service suddenly slows down in production.
CPU usage is low.
Memory usage is normal.
But requests are still taking a long time to complete.

What could be happening?"

Possible things to investigate:

- Thread blocking – threads might be waiting on locks or synchronized blocks
- I/O wait – database calls, APIs, or file operations may be slow
- Deadlock – two or more threads waiting for each other
- Thread pool exhaustion – tasks waiting in queue because workers are busy
- External service latency – downstream service responding slowly
- Excessive logging – blocking I/O from heavy log writing

This is why multithreading questions appear in interviews.

They want to see if you understand
how Java behaves under real production conditions.

So here’s the real question:

What would YOU check first in this situation?

Comment your answer.

I’ll share the detailed Java and Spring Boot Question & Answers PDF individually with interested folks.
---
## YOU’RE IN A JAVA INTERVIEW.

The interviewer starts with a simple question.

Then the questions start getting deeper…

Below are REAL interview questions
used to test production-level Java understanding:

- Your Java application is slow in production, but CPU and memory look normal. What do you check first?
- OutOfMemoryError occurs even though heap size seems sufficient. How is that possible?
- Threads are available in the pool but requests are still waiting. Why?
- Increasing heap size made the application slower. Explain why.
- GC pauses suddenly increased after a small deployment. What could have changed?
- JVM does not shut down even after the main() method finishes. What might be holding it?
- Parallel streams were added but overall throughput dropped. Why?
- Memory usage slowly keeps increasing over time. What would you investigate first?
- Logging configuration change caused a production slowdown. How can logging impact performance?
- ExecutorService tasks fail silently without visible errors. What might be happening?
- Application behaves differently on Java 8 vs Java 17. What could cause this?
- Retry logic implemented in the application caused system overload. What mistake might have been made?
- Deadlock occurs rarely in production but never locally. Why can that happen?
- Thread pool size was increased but throughput didn’t improve. Why?
- Application works perfectly in testing but fails under real production traffic. What could be the reason?

These questions are used to see
whether you understand how Java behaves in real systems,
not just how to write code.

I’ll share the detailed questions with answers pdf individually with interested folks.
---
## Top 10 Advanced Interview Questions for Senior Java Developer (Latest Technologies & Tools)

If you are preparing for a Senior Java Developer role, modern interviews focus on architecture, cloud, microservices, and AI-driven systems.

1. How do you design scalable microservices architectures using Spring Boot, Spring Cloud, and Kubernetes in cloud-native environments?

2. How do you optimize JVM performance using tools like JVM monitoring, JProfiler, VisualVM, or Grafana in high-scale applications?

3. What strategies do you use to implement event-driven architectures using tools such as Apache Kafka or RabbitMQ?

4. How do you design secure enterprise applications using OAuth2, JWT, and Spring Security?

5. How do you implement CI/CD pipelines for Java applications using tools like Jenkins, GitHub Actions, or GitLab CI?

6. How do you manage containerized Java applications using Docker and Kubernetes in production environments?

7. What is your approach to implementing reactive programming using Spring WebFlux or Project Reactor for high-performance systems?

8. How do you integrate AI/ML services or data pipelines with Java applications in modern architectures?

9. How do you ensure observability and monitoring using tools like Prometheus, ELK Stack, or OpenTelemetry?

10. How do you design resilient and fault-tolerant distributed systems using patterns such as Circuit Breaker, API Gateway, and Service Mesh?

Follow: Akshay Kumawat

Comment: "Senior Java Developer" and I will share the executive-level answers with you.
---
## MOST PEOPLE FAIL JAVA & SPRING BOOT INTERVIEWS
NOT BECAUSE THEY DON’T KNOW ENOUGH,
BUT BECAUSE THEY CAN’T THINK WHEN SYSTEMS BREAK.

Below are REAL interview questions
used to test production-level Java & Spring Boot understanding:

Java (Runtime, JVM, Concurrency)

- Java app slows down over time without errors. What’s happening internally?
- OutOfMemoryError occurs even when heap looks sufficient. How?
- CPU is low but latency is high. What could be blocking?
- Threads are available, yet requests are queued. Why?
- Increasing heap size made performance worse. Explain.
- GC pauses increased after a small code change. What changed?
- JVM doesn’t exit after main() finishes. What’s holding it?
- Parallel streams reduced throughput instead of improving it. Why?
- Memory keeps growing without static references. What do you suspect?
- Logging level change caused production slowdown. Why?
- ThreadLocal fixed one issue but created another. How?
- ExecutorService tasks fail silently. What went wrong?
- App behaves differently on Java 8 vs Java 17. Why?
- Retry logic overloaded the system. What was the mistake?
- Scaling instances made things worse. Why?

Spring Boot (Production & Scenarios)

- App works locally but fails after deployment. What do you check first?
- APIs are fast locally but slow only in prod. How do you debug?
- application.properties change didn’t reflect. Why?
- CPU is low but requests timeout. What’s the bottleneck?
- Multiple beans of same type cause startup failure. How to fix?
- @Transactional exists but rollback doesn’t happen. Why?
- DB connection pool exhausts under load. Why?
- Scheduled jobs impact API latency. How do you isolate?
- App behaves differently in Docker vs local. Why?
- New deployment but users see old behavior. What went wrong?
- Logs missing in production but present locally. Where to check?
- Async processing made performance worse. How?
- Circuit breaker stays open even when service is healthy. Why?
- Adding more resources didn’t improve performance. Why?
- What Spring Boot decision you made once caused a real production issue?

These questions are asked to see
whether you can OWN systems, not just build them.

👇👇👇
I’ll share the detailed resource individually with interested folks.
---
## 📨 "Design a Notification Service."
This question is quietly showing up in interviews at many product
companies.

On the surface, it sounds simple.

Send Email.
Send SMS.
Send Push.

Done?

Not really.

I had already thought about it from an HLD perspective
Kafka, retries, DLQs, scaling consumers.

But recently I asked myself:

> "If this comes up in an LLD round, can I design it cleanly in 45-60 minutes?"

That's when it becomes a powerful interview problem.

Because at LLD level, this single system touches:

- Strategy pattern (channel behavior abstraction)
- Factory pattern (clean resolution without switch-case)
- Observer pattern (logging, metrics, analytics)
- Custom exception hierarchy
- In-memory queue + async consumer
- Separation of concerns
- Open-Closed Principle
- Extensibility without breaking core logic

Suddenly, it's not "just notifications."

It's a full design patterns playground.

And the best part?

It's realistic.

Every real-world product has a notification system.
So interviewers love it because:

- It's relatable
- It's practical
- It exposes whether you truly understand object modeling

The difference between an average LLD answer and a strong one isn't
complexity.

- It's how cleanly we structure responsibilities.
- It's whether we avoid if-else chains.
- It's whether we design for extension without rewriting everything.

If you're preparing for backend interviews, try this exercise:

Design a Notification Delivery Service in pure Java.
No Spring.
No shortcuts.
Just clean abstractions.

You'll be surprised how much depth is hidden inside it.

If you see improvements or alternative approaches, drop them in the comments.

Comment “Notification” if you want the complete Java implementation zip, I’ll share it.
---
## Code is Easy.
Production is Brutal.

Writing Java code is the comfortable part.
Your API works locally. Tests pass. PR gets approved.

But production doesn’t care about your clean code.

Production cares about:

- Timeouts under load
- Memory leaks at 3AM
- Race conditions you never saw coming
- SSL failures
- Broken deployments
- Logs you forgot to add
- CPU spikes you can’t explain

Anyone can build a microservice.

But can you:

- Trace a request across services?
- Debug an issue without reproducing it locally?
- Roll back safely?
- Handle traffic 10x overnight?
- Secure APIs properly?
- Stay calm during an outage?

That’s the difference between a Java developer
and a production-ready engineer.

Building systems means:

- Designing for failure, not perfection
- Treating observability as a feature
- Automating deployments
- Monitoring what actually matters
- Securing by default
- Planning for scale early
- Owning incidents end-to-end

Because writing code is just the beginning.

Owning it in production —
That’s real engineering.
---
## What I see in most Java resumes:
- Java
- Spring
- Microservices

Great, I see you know Java. But as a senior, can you build, run, scale, observe, and secure Java systems in production?

A few tips and topics with accurate subskills that you need to mention if you need your resume to stand out:

1. Distributed Caching – mention Redis/Memcached

2. Monitoring & Observability – most popular ones are Splunk, Dynatrace, Grafana, ELK

3. Messaging – list one among Kafka, JMS or RabbitMQ

4. Testing – most popular frameworks/methods are TDD, Mockito, JUnit

5. CI/CD & Containers – devops skills like Jenkins, GitHub Actions, Docker, Kubernetes make your profile distinct

6. Frameworks – no prize for guessing: Spring Boot, Spring MVC, Apache Camel

7. Microservices Internals – try to mention one or two at least from Config Server, API Gateway, Service Discovery, Resilience4j

8. Multithreading & Concurrency – do not skip, mention a few of Executors, ForkJoin, CompletableFuture

9. Security – most used and popular ones are Spring Security, OAuth2, JWT

10. Persistence – you should have been using Hibernate, JPA or MyBatis so put one

11. API Development – basics of APIs: REST, Swagger, OpenAPI

12. Reactive Programming – your resume shines with words like WebFlux, Reactor or RxJava

13. Build Tools – mention Maven/Gradle

14. Code Quality – mentioning SonarQube, PMD, Checkstyle shows you care about quality

15. Cloud – shouldn't miss one from AWS, GCP, Azure

16. Java Versions – list a few Java 8 to 21 features you used

17. Design Principles – foundations of large codebase: SOLID, Design Patterns, Clean Architecture

If you are targeting Senior, Staff, or Lead roles:
- Focus on impact, not buzzwords
- Show production ownership
- Highlight architecture and reliability thinking

Good luck!
---
## Preview 👉 "How To Write Great Java Apps With LLMs and Agents"
See you at #JavaOne 2026
---
## One method in my Java demo app was using 71% of CPU. The code looked perfectly fine. After my DevNexus talk, attendees kept asking about the specific anti-patterns. This post shows eight patterns that compile fine, pass code review, and silently kill performance.

Before/after: 1,198ms → 239ms. 85K → 419K orders/sec. 19 GC pauses → 4.

Shoutout to Vinicius Senger for bringing me into his DevNexus talk on Java modernization, this series wouldn't exist without that.
---
## Java Developer Interview Prep Checklist: Don’t Walk In Unprepared

Java 8 & Project-Based Questions:

1. What are the new features introduced in Java 8?
2. What is a Method Reference?
3. What are Default Methods in interfaces?
4. Explain Intermediate Operations in Streams.
5. What is HTTP Status Code 204?
6. Explain the concept of Microservices in your project.
7. Difference between HashMap and Hashtable.
8. Explain the Authentication Layer in your project.
9. How does JWT (JSON Web Token) work?
10. What is Garbage Collector and how does it work?
11. How do you integrate third-party APIs/data in your project?

Core Java:
1. What is Method Hiding?
2. Output of:
System.out.println(Double.MIN_VALUE > 0.0d);
3. If you add a null value to an empty Set, what will be the size?
4. What is Garbage Collection?
5. Can you override a static method in interface?
6. Internal working of HashMap and how get() works.
7. Explain SOLID Principles.

Spring Boot:
1. What is @Lazy?
2. What is @Component?
3. What is Component Scanning?
4. How do you handle Exceptions in Spring Boot?
5. What is JPA?
6. Explain Bean Scopes.
7. @RequestParam vs @RequestBody
8. What is @PathVariable?
9. What is @GeneratedValue?

SQL:
1. You have a user table with 50 records.
Write a query to fetch 20 records starting from 5th row (first & last name only).
Example (MySQL/PostgreSQL):
SELECT first_name, last_name
FROM users
LIMIT 20 OFFSET 4;
2. Write an INNER JOIN query between two tables.
Example:
SELECT u.first_name, u.last_name, o.order_id
FROM users u
INNER JOIN orders o
ON u.id = o.user_id;

This is a solid checklist for Java developers with 2–5 years of experience.
If you can confidently explain these with real project examples, you’re already ahead of many candidates.