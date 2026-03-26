## 🚀 30 Days of Java Interview Questions – Day 12

💡 Question:
What is the final keyword in Java?

🔹 What is final?

final is a keyword in Java used to restrict modification.

It can be applied to:

- Variables
- Methods
- Classes

🔹 final Variable

Once a variable is assigned, its value cannot be changed.

Example:

```java id="k3h9ds"
final int x = 10;
// x = 20; ❌ Error
```

🔹 final Method

A final method cannot be overridden in a subclass.

```java id="p8f2la"
class A {
 final void show() {
 System.out.println("Hello");
 }
}
```

🔹 final Class

A final class cannot be extended (no inheritance allowed).

Example:

```java id="z1d8qp"
final class A {}

// class B extends A ❌ Not allowed
```

⚡ Quick Summary

- final variable → value cannot change
- final method → cannot override
- final class → cannot inherit

📌 Interview Tip

final is widely used to create immutable objects and to improve security and performance in Java applications.
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
## Most Java developers confuse this 👇
Fail-Fast vs Fail-Safe ⚡🛡️

It feels like just another definition-based question…
But interviewers are actually testing your understanding of collections behavior 👀

🔴 Fail-Fast Iterator

- Works directly on the original collection
- If the collection is modified during iteration → 💥 Exception thrown

Example:
ArrayList, HashMap
💡 Throws: ConcurrentModificationException
✔️ Fast
❌ Not safe during modification

🟢 Fail-Safe Iterator

- Works on a clone (copy) of the collection
- Changes in original collection won’t affect iteration

Example:
CopyOnWriteArrayList, ConcurrentHashMap
✔️ Safe during modification
❌ Slightly slower (extra memory used)

🔥 Real Difference (What interviewers expect):
- Fail-Fast → Detects changes and fails immediately
- Fail-Safe → Ignores changes by working on a copy

💡 Simple Analogy:
Fail-Fast ⚡
= “Something changed? I’m out!” ❌
Fail-Safe 🛡️
= “I’ll continue with my own copy.” ✅

🎯 Interview Tip:
- Use Fail-Fast when performance matters
- Use Fail-Safe when concurrent modification is expected

Stop memorizing definitions.
Start explaining behavior. 🚀
---
## Java Collections Interview Questions
📌 Basic Level
What is the Java Collection Framework?
What is the difference between Collection and Collections?
What are the main interfaces in the Collection Framework?
What is the difference between List, Set, and Map?
What is ArrayList?
What is LinkedList?
What is HashSet?
What is HashMap?
What is the difference between ArrayList and LinkedList?
What is the difference between HashMap and Hashtable?
📌 Intermediate Level
How does HashMap work internally?
What is hashing?
What is a bucket in HashMap?
What is collision in HashMap?
What is load factor?
What is initial capacity?
What is the difference between Iterator and ListIterator?
What is fail-fast and fail-safe iterator?
What is Comparable interface?
What is Comparator interface?
What is TreeMap?
What is TreeSet?
What is PriorityQueue?
What is BlockingQueue?
What is the difference between Set and List?
📌 Advanced Level (Product-Based Companies)
Why is HashMap not thread-safe?
How can you make HashMap thread-safe?
What is ConcurrentHashMap?
What is the difference between HashMap and ConcurrentHashMap?
What happens when two keys have the same hashCode?
What is rehashing?
What is IdentityHashMap?
What is WeakHashMap?
What is the difference between WeakHashMap and HashMap?
How does equals() and hashCode() work together?
📌 Coding + Scenario-Based
How do you remove duplicates from a list?
How do you find frequency of elements using collections?
How do you sort a list of custom objects?
How do you synchronize a collection?
How do you iterate over a HashMap?
How do you convert List to Set?
How do you find the second largest element in a list?
How do you detect and handle concurrent modification?
How do you implement LRU cache using collections?
How do you group objects using Map?
📌 Tricky / Deep Questions
Why does HashSet not allow duplicates?
Can we store null in HashMap and HashSet?
What is the difference between fail-fast and fail-safe in real scenarios?
Why is TreeMap slower than HashMap?
What happens internally when HashMap resizes?
---
## Most asked #Java 8 programs in Interview

1. Reverse a String using Java 8
 2. Find Duplicate Elements in a List
 3. Find First Non-Repeated Character in a String
 4. Count Occurrence of Characters in a String
 5. Sort a List of Objects using Comparator
 6. Find Maximum Number in a List
 7. Find Minimum Number in a List
 8. Calculate Sum of Elements in a List
 9. Filter Even Numbers from a List
 10. Filter Odd Numbers from a List
 11. Convert List of Strings to Uppercase
 12. Convert List of Strings to Lowercase
 13. Flatten a List of Lists
 14. Find Second Highest Number in a List
 15. Remove Duplicates from a List
 16. Find Longest String in a List
 17. Group Elements by Property using groupingBy
 18. Partition Numbers into Even and Odd
 19. Find Frequency of Each Word in a Sentence
 20. Join List of Strings with Delimiter
 21. Check if List Contains Duplicates
 22. Find Common Elements Between Two Lists
 23. Sort a Map by Values
 24. Convert List to Map
 25. Find Employee with Highest Salary
 26. Skip and Limit Elements in Stream
 27. Check if a String is Palindrome
 28. Find Missing Number in an Array
 29. Merge Two Lists using Streams
 30. Count Words in a String
 31. Find Numbers Starting with Specific Digit
 32. Extract Unique Characters from String
 33. Use Parallel Stream for Processing
 34. Find Average of Numbers in a List
 35. Find All Even Numbers and Their Squares
 36. Convert Array to List using Streams
 37. Iterate Map using forEach and Lambda
 38. Filter Null Values from List
 39. Sort Strings by Length
 40. Find Any Matching Element using findAny
 41. Find First Element using findFirst
 42. Check All Match Condition in List
 43. Check Any Match Condition in List
 44. Check None Match Condition in List
 45. Convert Map Keys to List
 46. Convert Map Values to List
 47. Concatenate Two Streams
 48. Find Distinct Elements from List
 49. Create Stream from Collection
 50. Generate Infinite Stream using iterate

1.Send me connection request so that you can message me.

2.Send me CV , notice period , current and preferred location , years of experience if criteria is matched .

3.I will upload your CV and other details to portal .

4.You will get mail , Recruiter will contact you .

5.If you pass Technical Interview , You will get selected and Onboarding starts .
---
## Java Stream API is confusing… until you solve THESE 🔥

Most developers keep reading theory but still get stuck in interviews.
I decided to practice instead — and everything started making sense.
Here are 6 real problems I solved using Streams 👇

✔ Find the second-highest number in a list
✔ Count frequency of characters in a string
✔ Find duplicate elements
✔ Reverse each word in a sentence
✔ Find the longest string
✔ Sort strings by length

Instead of writing long loops, I used:
→ map()
→ filter()
→ sorted()
→ collect()

💡 Practicing problems > Reading theory

---
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
## 𝐓𝐨𝐩 50 𝐉𝐚𝐯𝐚 𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐚𝐧𝐝 𝐀𝐧𝐬𝐰𝐞𝐫𝐬 𝐏𝐃𝐅

In this Document, you will find a collection of 50 Java interview questions and answers that will help you prepare for your next Java programming interview.

The notes are divided into two sections: basic and advanced. The basic section covers the fundamental Java topics that every Java developer should know, such as data types, operators, control statements, arrays, strings, classes, objects, constructors, methods, interfaces, and abstract classes.

𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐏𝐃𝐅:
---
## 𝐌𝐨𝐬𝐭 𝐀𝐬𝐤𝐞𝐝 𝐉𝐚𝐯𝐚 𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰 (100 𝐐&𝐀) 𝐏𝐃𝐅

By studying these questions and answers, you'll be well-equipped to tackle any Java interview with confidence. So, let's dive in and start preparing for your next Java interview!

To help you prepare, we have compiled a list of the most commonly asked Java interview questions and answers. This PDF contains 100 Q&A that cover topics such as Java basics, object-oriented programming, collections, multithreading, exception handling, and more.

𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐏𝐃𝐅:
---
## Q.Sort Map by Values & use java8.
Map<String, Integer> map = Map.of("apple", 3, "banana", 1, "kiwi", 2);
To sort a Map by its values in Java 8, you must convert the entry set into a Stream, sort it using a value-based comparator, and collect the results into a LinkedHashMap to preserve the sorted order.
Map<String, Integer> sortedMap = map.entrySet()
 .stream()
 .sorted(Map.Entry.comparingByValue())
 .collect(Collectors.toMap(
 Map.Entry::getKey,
 Map.Entry::getValue,
 (oldValue, newValue) -> oldValue,
 LinkedHashMap::new
 ));

For descending order
Map<String, Integer> sortedDesc = map.entrySet()
 .stream()
 .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
 .collect(Collectors.toMap(
 Map.Entry::getKey,
 Map.Entry::getValue,
 (e1, e2) -> e1,
 LinkedHashMap::new
 ));

Q.Employee highest earning employee dept wise using java 8.

Map<String, Employee> topPaidByDept = employeeList.stream()
 .collect(groupingBy(
 Employee::getDepartment,
 collectingAndThen(
 maxBy(comparingDouble(Employee::getSalary)),
 Optional::get
 )
 ));
---
## Records in Java are used to create immutable data objects with minimal code.
They automatically generate constructors, getters, equals(), hashCode(), and toString().

Unlike traditional bean classes, they eliminate boilerplate and improve readability.Records are best suited for DTOs and data carriers in modern applications.

Java 14 → Preview

Java 15 → Preview (second iteration)

Java 16 → Official release
---
## Refactoring in Java isn’t “clean-up”.
It’s how you keep change cheap.

Here are 5 Java refactoring moves I use constantly (with quick examples):
- Extract Method (name the intent)
 Before: one 60-line method
 After: subtotal(), applyVipDiscount(), priceWithTaxIfNeeded()

- Kill boolean flags
 Before: generate(true)
 After: generateSummary() / generateDetailed()

- Replace switch with Strategy
 Before: switch(shippingMethod)
 After: ShippingPolicy.cost(order) implementations

- Replace primitives with Value Objects
 Before: createUser(String email)
 After: createUser(new Email(email)) (validation lives in one place)

- Separate domain logic from infrastructure
 Before: “God service” does everything
 After: domain objects own rules, service only orchestrates

Refactor like a professional:
 ✅ small steps
 ✅ tests/characterisation tests
 ✅ behaviour stays the same

What refactor gives you the biggest win in real production code?
---
## ✒ Write a method to verify whether the given two strings are anagrams using Java Streams.

Input - CarRace, RaceCar and BatRat, CatRat
---
## 📌Java Control Flow Statement Cheatsheet. (Explained)

⭕Here is the quick reference guide for control flow statements in Java.

🔵What are control flow statements?
Control flow statements are the statements in a program which control the flow of execution of a program.

📌There are three types of control flow statements in Java.

🔸Decision Making Statements
🔹Looping Statements
🔸Branching Statements

🟢Decision Making Statements :
Decision making statements determine which statements to execute depending upon the outcome of a supplied condition or an expression.

🟡Looping Statements :
Looping statements are used to execute a set of statements repeatedly until supplied condition becomes FALSE.

🟤Branching Statements :
Branching statements or jump statements are used to transfer the control of execution to some other part of the program.
---
## “I thought I knew Strings… until my recent interviews proved me wrong!” 😅

During my recent #Java developer interviews (while switching jobs), I was hit with some deceptively simple-looking String questions —
but trust me, they test how deeply you understand memory, immutability, and the String Pool.

Check these out 👇 — can you guess the outputs? 🤔

1️⃣ String s1 = "Java";
 String s2 = "Java";
 System.out.println(s1 == s2);

2️⃣ String s1 = new String("Hello");
 String s2 = "Hello";
 System.out.println(s1 == s2);

3️⃣ String s1 = "Java";
 String s2 = "Ja" + "va";
 System.out.println(s1 == s2);

4️⃣ String s1 = "Ja";
 String s2 = s1 + "va";
 System.out.println("Java" == s2);

5️⃣ String s1 = "abc";
 s1.concat("xyz");
 System.out.println(s1);

6️⃣ String s1 = "abc";
 s1 = s1.concat("xyz");
 System.out.println(s1);

7️⃣ String s1 = "HELLO";
 String s2 = s1.toLowerCase();
 System.out.println(s1 == s2);

8️⃣ String s1 = new String("Java");
 String s2 = s1.intern();
 System.out.println(s1 == s2);

💥 Most developers fail these not because of logic — but because they don’t truly get how JVM handles Strings internally.

Thanks Vipul Tyagi for ur Detailed Explanation ✨
---
## 📌Java Collections Cheat Sheet. (complete Guide)

⭕Here is the quick reference guide for collections in java

🔵What is Java Collection Framework?

➡️ Java Collection Framework is a framework which provides some predefined classes and interfaces to store and manipulate the group of objects. Using Java collection framework, you can store the objects as a List or as a Set or as a Queue or as a Map and perform basic operations like adding, removing, updating, sorting, searching etc.. with ease.

🟡Why Java Collection Framework?

➡️ Earlier, arrays are used to store the group of objects. But, arrays are of fixed size. You can’t change the size of an array once it is defined. It causes lots of difficulties while handling the group of objects. To overcome this drawback of arrays, Java Collection Framework is introduced from JDK 1.2.

🟢Java Collections Hierarchy :

➡️All the classes and interfaces related to Java collections are kept in java.util package. List, Set, Queue and Map are four top level interfaces of Java collection framework. All these interfaces (except Map) are the sub interfaces of java.util.Collection interface.

⭕Let’s see these primary interfaces one by one👇
---
## The first Java roadmap that you can talk with!! This roadmap covers both Core Java topics (like Syntax, OOP and Exception Handling) and more advanced topics like JVM Internals and Annotations. You'll also learn about Java Frameworks, Microservices Architecture and Performance Optimization.

About
Accessibility
Talent Solutions
Professional Community Policies
Careers
Marketing Solutions

Privacy & Terms
Ad Choices
Advertising
Sales Solutions
Mobile
Small Business
Safety Center
Questions?
Visit our Help Center.

Manage your account and privacy
Go to your Settings.

Recommendation transparency
Learn more about Recommended Content.

Select Language

English (English)
LinkedIn Corporation © 2026

Vishnu KrishnanStatus is online
MessagingYou are on the messaging overlay. Press enter to open the list of conversations.

Compose message
You are on the messaging overlay. Press enter to open the list of conversations.
0 notifications total

Skip to search

Skip to main content

Keyboard shortcuts
Close jump menu
Search
new feed updates notifications
Home
My Network
Jobs
Messaging
2
2 new notifications
Notifications
Vishnu Krishnan
Me

For Business
Try Premium for ₹0
My items
Job tracker
Saved posts and articles
10+
Saved Posts
All
Articles

## Atlassian pays around 50-70LPA for SDE-1 and 60-90LPA for SDE-2

This is the classic question they generally ask

𝗝𝗮𝘃𝗮/𝗕𝗮𝗰𝗸𝗲𝗻𝗱1. How HashMap works internally
2. ConcurrentHashMap vs HashMap3. String immutability in Java4. ArrayList vs LinkedList5. Garbage Collection in Java6. JVM vs JRE vs JDK7. Checked vs Unchecked Exceptions8. try-catch-finally flow9. Multithreading, synchronization, race conditions10. Runnable vs Callable11. Executor Framework12. Deadlock, starvation, livelock13. volatile vs synchronized14. Java 8 Streams15. Optional in Java16. LRU Cache design in Java17. Microservices vs Monolith18. Idempotent APIs19. SQL vs NoSQL20. Database Indexing21. Redis caching use cases22. Pagination for large datasets23. REST API best practices24. Authentication vs Authorization25. Connection Pooling26. Debugging a slow Spring Boot API27. Dependency Injection in Spring28. Designing for high throughput and low latency

𝗦𝘆𝘀𝘁𝗲𝗺 𝗗𝗲𝘀𝗶𝗴𝗻
1. Design a Project Management Tool Like Jira
2. Design a Real-Time Collaboration Tool.
3. Design a Scalable Notification System
4. Design a Search System for Knowledge Base Articles
5. Design an API Gateway for Atlassian Services
6. Design a Version Control System for Documentation
7. Design a Real-Time Analytics Platform
8. Design a Scalable User Authentication and Authorization System
9. Design a Workflow Automation System
10. Design a Logging and Monitoring System
11. Design a Rate Limiter
12. Design a parking
13. Database Design
14. Design Snake Game
15. Design a Ticketing System like Jira
16. Design a URL Shortening Service
17. Design a Notification System
18. Design a Distributed Messaging System
19. Design a Scalable Chat Application
20. Design a Job Scheduler

Cracking Atlassian is not just about DSA.

For SDE-1/SDE-2, they often test System Design, LLD, Java internals, backend architecture, and real-world problem solving.

From what I’ve seen, these are the kinds of questions candidates should prepare for

Stay Hungry, Stay FoolisH!
---
## 🚀 𝐅𝐚𝐢𝐥-𝐅𝐚𝐬𝐭 𝐯𝐬 𝐅𝐚𝐢𝐥-𝐒𝐚𝐟𝐞 𝐈𝐭𝐞𝐫𝐚𝐭𝐨𝐫𝐬 𝐢𝐧 𝐉𝐚𝐯𝐚
If you're preparing for Java interviews, this is an important concept to understand.
When iterating over collections in Java, two types of iterator behaviors exist.

🔴 Fail-Fast Iterator
If the collection is modified while iterating, it immediately throws a Concurrent Modification Exception.

Example collections:
- ArrayList
- HashMap
- HashSet

Example:
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Spring");
for (String s : list) {
 list.add("Docker"); // throws ConcurrentModificationException
}
These iterators detect structural modifications during iteration and fail immediately.

🟢 Fail-Safe Iterator
Fail-Safe iterators work on a copy of the collection, so modifications during iteration do not throw exceptions.

Example collections:
- ConcurrentHashMap
- CopyOnWriteArrayList

Example:
CopyOnWriteArrayList<String> list = new CopyOnWriteArrayList<>();
list.add("Java");
for (String s : list) {
 list.add("Spring"); // no exception
}
📌 Key Difference
Fail-Fast → Throws exception if collection is modified during iteration
Fail-Safe → Works on a copy, so no exception occurs
Understanding this concept is important when working with multithreading and concurrent collections.
---
## I have reviewed hundreds of Java PRs over years. The same mistakes show up every single time.
Here are 6 I flag in almost every review and exactly what I write in the comment:

1. Catching generic Exception
try {
 sendEmail(user);
} catch (Exception e) {
 log.error("something went wrong");
}

My comment: "What are you actually catching? Handle specific exceptions. This swallows everything silently — including bugs you need to know about."
----------------------------------------

2. Using Optional.get() without checking first
Optional user = userRepo.findById(id);
return user.get(); // ← NoSuchElementException waiting to happen

My comment: "Use orElseThrow() with a meaningful message. Optional exists to make absence explicit — don't bypass it."
----------------------------------------

3. Building strings inside a loop
for (String tag : tags) {
 result = result + ", " + tag; // ← new object allocated every iteration
}

My comment: "Use String.join() or StringBuilder. With a large list this quietly becomes a performance problem."
----------------------------------------

4. Returning null instead of empty collection
public List getOrders(Long userId) {
 if (noResults) return null; // ← NullPointerException gift to every caller
}

My comment: "Return Collections.emptyList(). Never make the caller guess whether null means 'not found' or 'something broke'."
----------------------------------------

5. One method doing everything
public void submitOrder(OrderRequest req) {
 // 180 lines: validate, calculate, persist, notify, log, respond
}

My comment: "Single Responsibility. If I can't unit test one concern in isolation, the method is doing too much. Break it up."
----------------------------------------

6. Magic numbers with no context
if (retryCount > 3) { ... }
if (discount > 0.25) { ... }
My comment: "Extract to named constants. 3 and 0.25 mean nothing to the next developer (or to you in 6 months)."
----------------------------------------

Which one do you see most often on your team?
---
## I Remember Struggling With Java Interviews… Until I Found My Path! 💪

When I started preparing for Java interviews, it felt overwhelming—like a giant puzzle with too many pieces.
But breaking it down into smaller, manageable parts made all the difference.

✅ Core Java Mastery:
 - OOP Concepts (Inheritance, Polymorphism, Encapsulation, Abstraction)
 - Collections Framework (List, Set, Map)
 - Exception Handling
 - Multithreading & Concurrency

✅ Java 8 Features:
 - Lambda Expressions
 - Streams API
 - Optional Class
 - Functional Interfaces

✅ Java Memory Management:
 - JVM Architecture
 - Garbage Collection
 - Heap & Stack Memory

✅ Practical Coding:
 - Practice DSA (Data Structures & Algorithms) using Java.
 - Solve coding problems daily.

I faced the same struggle, but consistency and proper planning helped me conquer it.
If you’re feeling lost in your Java interview preparation, let’s discuss and improve together!

For queries and guidance, connect with me here: Topmate
---