<!-- Part of Java Learning Roadmap — Section 7 -->

# ☕ 7. Java Version Features & Implementations (8 to 21)

---

## 1. Definition

Java has evolved from a slow, verbose, purely Object-Oriented language into a modern, multi-paradigm language. Enterprises generally only adopt **LTS (Long Term Support)** releases.

The essential LTS releases to know are:
*   **Java 8 (2014):** The Functional Revolution (Lambdas, Streams).
*   **Java 11 (2018):** Productivity & Cloud (Local Variable Type Inference `var`, HTTP Client, new String methods).
*   **Java 17 (2021):** Boilerplate Reduction (Records, Text Blocks, Sealed Classes, Pattern Matching `instanceof`). *Minimum for Spring Boot 3.*
*   **Java 21 (2023):** Scalability Revolution (Virtual Threads, Pattern Matching for switch, Sequenced Collections).

---

## 2. Why It Exists

Java's evolution solves specific historical pain points:
*   **Verbosity:** Writing getters, setters, constructors, and `equals/hashCode` by hand. Fixed by **Records (Java 17)**.
*   **Clunky Strings:** Concatenating JSON or SQL with `+ "\n" +`. Fixed by **Text Blocks (Java 17)**.
*   **Concurrency limits:** The 1:1 mapping of Java threads to OS threads capped scaling. Fixed by **Virtual Threads (Java 21)**.
*   **Boilerplate typing:** `List<Map<String, User>> map = new ArrayList<Map<String, User>>();` Fixed by **`var` (Java 11)**.

---

## 3. How It Works Internally

### 3.1 Records (Java 17)
When you define `public record User(String name, int age) {}`, the Java compiler automatically generates:
1.  A `final` class that extends `java.lang.Record`.
2.  `private final` fields for `name` and `age`.
3.  A canonical constructor assigning the fields.
4.  Public accessor methods: `name()` and `age()` (Note: NOT `getName()`).
5.  Optimized `equals()`, `hashCode()`, and `toString()`.

### 3.2 Virtual Threads (Java 21)
A Virtual Thread is not an OS thread. It is managed entirely by the JVM. 
When a Virtual Thread makes a blocking call (like reading from a DB), the JVM **unmounts** it from the underlying "carrier" OS thread, and mounts a different Virtual Thread that is ready to work. This allows 10 OS threads to power 100,000+ Virtual Threads.

### 3.3 Pattern Matching `instanceof` (Java 17)
Previously: `if (obj instanceof String) { String s = (String) obj; s.length(); }`
The compiler now combines the type check and the cast into one step, binding the casted result to a new flow-scoped variable.

---

## 4. Code Examples

### 4.1 Java 11: `var` and String Methods
```java
// var infers type from the right side. Only works for LOCAL variables.
var users = new ArrayList<String>(); 
var client = HttpClient.newHttpClient();

// Java 11 String tools
System.out.println("  ".isBlank());           // true
System.out.println("Java\n11".lines().count()); // 2
System.out.println("Ha".repeat(3));           // HaHaHa
```

### 4.2 Java 17: Records & Text Blocks
```java
// Immutable DTO in one line
public record UserResponse(Long id, String username) {}

UserResponse res = new UserResponse(1L, "admin");
System.out.println(res.username()); // Accessor

// Text Blocks for JSON/SQL (No escaping quotes!)
String query = """
    SELECT id, email 
    FROM users 
    WHERE status = 'ACTIVE' 
    ORDER BY created_at DESC
    """;
```

### 4.3 Java 17/21: Pattern Matching (instanceof & switch)
```java
Object obj = "Hello Java 21";

// Java 17: instanceof pattern matching
if (obj instanceof String s && s.length() > 5) {
    System.out.println(s.toUpperCase());
}

// Java 21: switch pattern matching (Exhaustive, no breaks needed)
String description = switch (obj) {
    case Integer i -> "An integer: " + i;
    case String s  -> "A string of length: " + s.length();
    case null      -> "Null value!";
    default        -> "Unknown object type";
};
```

### 4.4 Java 21: Sequenced Collections
```java
// Uniform interface to access first/last elements
SequencedCollection<String> list = new ArrayList<>();
list.add("First");
list.add("Middle");
list.add("Last");

System.out.println(list.getFirst()); // "First"
System.out.println(list.getLast());  // "Last"
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Can you extend a `Record`? | **No**. Records are implicitly `final` and already extend `java.lang.Record`. Java does not support multiple inheritance. You *can* implement interfaces, though. |
| Where can you use `var`? | Only for **local variables** inside methods with an immediate initializer. You cannot use it for class fields, method parameters, or method return types. |
| What is a Sealed Class? | A class that specifies exactly which classes are allowed to extend it using the `permits` keyword. (e.g., `public sealed class Result permits Success, Failure`). Exhaustive in `switch` blocks. |
| Are Virtual Threads faster than OS Threads? | **No.** They execute instructions at the same speed. Their superpower is **Scale**, not Speed. They allow you to hold open thousands of blocking HTTP/DB connections without running out of RAM. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Using `var` when type is unclear | `var result = service.process();` (What is result?) | Only use `var` when the type is obvious: `var users = new ArrayList<User>();` |
| Pinning Virtual Threads | Using `synchronized` blocks inside a Virtual Thread prevents the JVM from unmounting it during a block. | Use `ReentrantLock` instead of `synchronized` inside highly concurrent Virtual Thread code. |
| Trying to map JSON to a Record using an old Jackson library | Records don't have standard `getXYZ()` methods or zero-arg constructors. | Jackson requires version `2.12+` to natively deserialize JSON into Java Records. |

---

## 7. Real-World Usage

| Feature | Where it shows up |
|---|---|
| **Text Blocks** | Writing complex Postgres SQL queries inside Spring Data `@Query` annotations. |
| **Records** | Every Request/Response DTO in a Spring Boot REST Controller. Replaces Lombok `@Data`. |
| **Virtual Threads** | Enabling `spring.threads.virtual.enabled=true` in Spring Boot 3.2+ to handle 10,000 concurrent REST API calls without changing any application code. |
| **`HttpClient` (Java 11)** | Replaces the heavy Apache HTTP client for making API calls to external microservices. |

---

## 8. Practice Tasks

1.  **Lombok to Record:** Take an existing Data Transfer Object (DTO) class that uses `@Getter`, `@Setter`, `equals()`, and `hashCode()`. Rewrite it as a single-line Java 17 `record`. Test creating it and reading data.
2.  **Modern Switch:** Write a method taking an `Object`. Use Java 21 Switch Pattern Matching to return "Small String" if it's a string < 5 chars, "Big String" if > 5 chars, "Integer" if it's an int, and "List" if it's an ArrayList.
3.  **Virtual Thread Tester:** Write a `for` loop that submits 100,000 tasks that just `Thread.sleep(1000)`. Run it using a fixed thread pool of 200. Note the time (will be ~500 seconds). Change `Executors.newVirtualThreadPerTaskExecutor()` run it again (will be ~1 second).

---

## 9. Quick Revision

| Version | Top Features | Impact |
|---|---|---|
| **Java 8 (2014)** | Lambdas, Streams, Optional, java.time | Brought Functional Programming |
| **Java 11 (2018)** | `var`, HTTP Client, String methods (`isBlank`) | Developer Productivity |
| **Java 17 (2021)** | Records, Text Blocks (`"""`), Sealed Classes | Slain Boilerplate, Standardized DTOs |
| **Java 21 (2023)** | Virtual Threads (Loom), Switch Pattern Matching | Massive Concurrency Scale |
