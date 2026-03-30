<!-- Part of Java Learning Roadmap — Section 7 -->

# ☕ 7. Java Version Features & Implementations (8 to 21)

---

## 1. Definition

Java has evolved from a slow, verbose, purely Object-Oriented language into a modern, multi-paradigm language. Enterprises generally only adopt **LTS (Long Term Support)** releases.

### 1.1 The Evolution of Java (LTS Versions)

**Core Idea:**
Java isn't "just an old Enterprise language" anymore. Since Java 8, it has adopted the best features of modern languages (Python, Scala, Kotlin) while keeping its legendary stability.

**Why it matters:**
Java 8 changed how we *write* code (Functional). Java 17/21 changed how we *design* systems (Data Carriers and High Throughput). Staying on Java 8 today is like using a flip phone in a smartphone world.

**When to use:**
*   **Java 17:** The new baseline for all modern projects (required for Spring Boot 3).
*   **Java 21:** Use when building high-concurrency Microservices that handle thousands of simultaneous requests.

**When NOT to use:**
*   Avoid non-LTS versions (9, 10, 12, 13, 14, 15, 16, 18, 19, 20) in production unless you are willing to upgrade your entire tech stack every 6 months.

**Example (Production Stack):**
A typical modern microservice uses **Java 17**, **Spring Boot 3**, and **Hibernate 6**. It uses **Records** for all API data transfers (DTOs) and **Text Blocks** for SQL queries.

**Deep Dive:**
The release cycle changed in 2018. Now, a new "Feature Release" comes every 6 months, and an "LTS" (Long Term Support) release comes every 2 years. This allows the JVM to get new features (like Virtual Threads) faster without breaking the entire ecosystem.

**Advanced Insight:**
**The 6-month train.** Features now go through "Preview" stages. You can try Features like "Scoped Values" in Java 21, but they aren't "standard" yet. This "Preview" system allows Oracle to get developer feedback before finalizing the API.

**Pitfall:**
**Migrating from 8 to 17.** The biggest hurdle isn't the code, it's the **JPMS (Java Module System)** introduced in Java 9. Many old libraries (that use internal `sun.misc.Unsafe`) will crash in Java 17+ unless you add specific `--add-opens` flags to your JVM.

**Production Tip:**
Always use **JDK 17 or 21** for your Docker base images. They have significant performance improvements in G1 Garbage Collection and memory footprint that Java 8 simply doesn't have.

**Interview Trap:**
"Can you run a Java 17 JAR on a Java 8 JRE?"
**Answer:** **No.** Java is backward-compatible (old code runs on new JVM), but not forward-compatible. A Java 17 class file has a higher version number (61.0) that Java 8 (52.0) doesn't understand.

---

## 2. Why It Exists

Java's evolution solves specific historical pain points:
*   **Verbosity:** Writing getters, setters, constructors, and `equals/hashCode` by hand. Fixed by **Records (Java 17)**.
*   **Clunky Strings:** Concatenating JSON or SQL with `+ "\n" +`. Fixed by **Text Blocks (Java 17)**.
*   **Concurrency limits:** The 1:1 mapping of Java threads to OS threads capped scaling. Fixed by **Virtual Threads (Java 21)**.
*   **Boilerplate typing:** `List<Map<String, User>> map = new ArrayList<Map<String, User>>();` Fixed by **`var` (Java 11)**.

---

## 3. How It Works Internally

### 3.1 Records (Java 17) — The Data Carrier

**Core Idea:**
A "no-boilerplate" class for data. It’s like a POJO but the compiler writes the constructor, getters, and `equals/hashCode` for you in one line.

**Why it matters:**
POJOs are 5% data and 95% noise (getters/setters). Records make your code "honest"—when you see a Record, you know instantly it's just a transparent data carrier that doesn't change.

**When to use:**
*   **DTOs (Data Transfer Objects):** API requests and responses.
*   **Database Projections:** Reading specific columns from SQL.
*   **Temporary Tuples:** Returning two values from a private method.

**When NOT to use:**
*   **Hibernate Entities:** JPA/Hibernate currently requires mutable objects and no-arg constructors (which Records don't have). Use standard classes or Lombok for Entities.
*   When you need internal state that can change (Records are immutable).

**Example:**
Instead of 50 lines of code, use:
`public record UserDTO(String id, String email, LocalDate dob) {}`

**Deep Dive:**
A Record is a special kind of class. It is **implicitly final** (cannot be extended) and its fields are **implicitly final**. It does not allow instance fields outside the header. 

**Advanced Insight:**
**Compact Constructors.** Records allow you to write a constructor *without* parameters just for validation:
`public record User(String email) { public User { if (email == null) throw new Error(); } }`
The compiler adds the `this.email = email` assignment *after* your validation block automatically.

**Pitfall:**
**Serialization Compatibility.** Records have a different serialization protocol than regular classes. They use the canonical constructor during deserialization, which makes them safer but can break old systems expecting raw field injection.

**Production Tip:**
Use Records with **Jackson (Spring Boot)**. Jackson 2.12+ supports Records out of the box, making your REST layers significantly cleaner than using Lombok or manual POJOs.

**Interview Trap:**
"Can a Record extend another Class?"
**Answer:** **No.** All Records implicitly extend `java.lang.Record`. Since Java doesn't support multiple inheritance, they cannot extend anything else. However, they **can** implement interfaces.

---

### 3.2 Sealed Classes (Java 17) — Controlled Inheritance

**Core Idea:**
"A class with a guest list." You define a parent class and explicitly list exactly which child classes are allowed to extend it.

**Why it matters:**
In big projects, you don't want a junior dev creating a new `DiscountType` that breaks your logic. Sealed classes give the architect total control over the inheritance tree.

**When to use:**
*   Defining **Domain States** (Order Status: Paid, Pending, Refused).
*   Library development where you want to prevent users from sub-classing your core internals.

**When NOT to use:**
*   General-purpose utility classes where you want developers to extend functionality freely.

**Example:**
`public sealed class Shape permits Circle, Square {}`
If a developer tries to create `class Triangle extends Shape`, the code won't compile.

**Deep Dive:**
The compiler uses the `PermittedSubclasses` attribute in the class file. Subclasses of a sealed class must be `final`, `sealed`, or `non-sealed`.

**Advanced Insight:**
**Switch Exhaustiveness.** Combined with Java 21 Switch Pattern Matching, the compiler can tell if you've missed a case. If `Shape` only allows `Circle` and `Square`, and you switch on it, you don't need a `default` case!

**Pitfall:**
Subclasses must be in the same **Module** or (if in the same package) the same **Jar**. You can't "Permit" a class that you don't own.

**Production Tip:**
Use Sealed Classes for **Result/Either types** in your Service layer (e.g., `Result permits Success, Error`). This forces the UI layer to handle both cases explicitly.

**Interview Trap:**
"What is a `non-sealed` class?"
**Answer:** It is a subclass of a sealed class that "re-opens" the inheritance tree. It's used when you want a specific branch of your hierarchy to be freely extendable again.

### 3.3 Virtual Threads (Java 21) — The Scaling Hero

**Core Idea:**
Threads that cost almost nothing. You can run 1,000,000 of them on a standard laptop.

**Why it matters:**
Classic Java scalability was limited by OS threads (1 thread = 1MB RAM). With Virtual Threads, you can follow the "Thread-Per-Request" model without fearing a server crash. It makes Java as efficient at I/O as Go or Node.js.

**When to use:**
*   **I/O Blocking:** Calling a Database, calling an external REST API, reading from a Disk.
*   Spring Boot 3.2+ microservices.

**When NOT to use:**
*   **CPU Intensive Tasks:** Hashing, complex math, video encoding. Virtual threads won't help you here; they actually add a tiny bit of overhead.

**Example:**
A Gateway service that calls 5 different microservices for every user request. Using Virtual Threads, you can handle 50,000 simultaneous users on a small 1GB RAM container.

**Deep Dive:**
Virtual Threads are managed by the JVM and run on top of a pool of "Carrier Threads" (usually ForkJoinPool). When a Virtual Thread waits for a DB response, it is "yielded" and the Carrier Thread runs a different Virtual Thread.

**Advanced Insight:**
**The Stack Storage.** While Platform Threads have a fixed 1MB stack on the OS, Virtual Threads store their call stack on the **Java Heap**. As the stack grows and shrinks, it only uses as much memory as it actually needs.

**Pitfall:**
**ThreadLocal Overuse.** If you have 1 million virtual threads, each having a 1MB `ThreadLocal` object, you will hit an `OutOfMemoryError` very quickly. Use **Scoped Values** for large-scale data sharing.

**Production Tip:**
Do **NOT** pool Virtual Threads. Just create them using `Executors.newVirtualThreadPerTaskExecutor()`. They are meant to be short-lived and disposable.

**Interview Trap:**
"Will Virtual Threads make my code run faster?"
**Answer:** **No.** They don't speed up the execution. They improve **Throughput** (how many tasks a single server can handle), not **Latency** (how long one task takes).

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

### 3.4 Lambda Expressions (Java 8) — The Functional Shift

**Core Idea:**
A "Method without a name" that you can pass around like a piece of data.

**Why it matters:**
Before Java 8, we had to use "Anonymous Inner Classes" just to sort a list or handle a button click (7 lines of code). Lambdas reduced this to 1 line, enabling functional processing with the Streams API.

**When to use:**
*   Anywhere a **Functional Interface** (SAM - Single Abstract Method) is required.
*   In `List.forEach`, `Stream.map`, and Event Listeners.

**When NOT to use:**
*   For very long, complex multi-line logic. If a lambda is more than 3-5 lines, put it in a separate private method and use a **Method Reference** (`this::myMethod`).

**Example:**
`list.removeIf(user -> user.age() < 18);`

**Deep Dive:**
Unlike Anonymous Inner Classes (which create a new `.class` file for every instance), Lambdas are converted into a private method inside the current class and called via the **`invokedynamic`** instruction.

**Advanced Insight:**
**LambdaMetafactory.** At runtime, the JVM uses the `LambdaMetafactory.metafactory` method to dynamically generate a "call site" that links the functional interface to the lambda logic. This makes lambdas faster and more memory-friendly than anonymous classes.

**Pitfall:**
**Variable Capture.** Lambdas can only use local variables that are `final` or "effectively final." If you try to change a local variable inside a lambda, it won't compile.

**Production Tip:**
Avoid "Side Effects" in lambdas. A lambda should ideally take an input and return an output without modifying external state (like updating a list outside the lambda). This makes your code thread-safe and easier to read.

**Interview Trap:**
"Are Lambdas just syntactic sugar for Anonymous Inner Classes?"
**Answer:** **No.** They differ at the bytecode level (`invokedynamic` vs `new`), they don't have their own scope (`this` in a lambda refers to the surrounding class), and they don't generate separate class files on disk.

---

### 3.5 Text Blocks (Java 17) — Readable JSON & SQL

**Core Idea:**
A string that spans multiple lines without needing `\n` or `+` everywhere. Just wrap it in triple quotes `"""`.

**Why it matters:**
Java developers used to hate writing SQL or JSON because of the "String Concatenation Hell." Text blocks make your code look exactly like the query you execute in a database tool.

**When to use:**
*   SQL queries (`@Query` in Spring Data).
*   JSON templates for testing or mock responses.
*   HTML snippets for emails.

**When NOT to use:**
*   Single-line strings.
*   Dynamic strings where you need heavy variable interpolation (use `String.format` or Java 21's **String Templates**).

**Example:**
```java
String json = """
    {
      "id": 1,
      "status": "SUCCESS"
    }
    """;
```

**Deep Dive:**
Text blocks automatically handle **Indentation**. The JVM looks at the "Incidental Whitespace" (the smallest common indentation) and strips it away.

**Advanced Insight:**
**Escaping.** Inside a text block, you can use raw double-quotes `"` without backslashes. You only need to escape triple-quotes `\"""`.

**Pitfall:**
**Trailing Whitespace.** By default, text blocks strip trailing whitespace on every line. If you need a space at the end of a line for some reason, you must use the `\s` escape character.

**Production Tip:**
Combine Text Blocks with **`String.formatted()`**. It’s much cleaner than using old-school `String.format()`:
`var query = """SELECT * FROM %s""".formatted(tableName);`

**Interview Trap:**
"How does the JVM decide how much indentation to remove in a Text Block?"
**Answer:** It uses the "Common Indentation" across all lines. The leftmost character of any non-empty line (including the closing `"""`) determines the margin.

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

### 7.1 Real-World Feature Mapping

| Version | Feature | Production Benefit |
|---|---|---|
| **Java 8** | **Lambdas / Streams** | Drastically reduced "Boilerplate loops" in data processing logic. |
| **Java 11** | **`var`** | Reduced verbosity for complex generics: `Map<String, List<Order>> m = new HashMap<>();` becomes `var m = new HashMap<String, List<Order>>();`. |
| **Java 17** | **Records** | Standardized DTOs. One line of code replaces 50 lines of Lombok-laden boilerplate. |
| **Java 17** | **Text Blocks** | Allows clean, multi-line SQL or JSON directly in Java code without `+ "\n"`. |
| **Java 21** | **Virtual Threads** | Allowed microservices to scale to 10x more concurrent users on existing Kubernetes hardware. |
| **Java 21** | **Sequenced Collections** | Finally provides a standard `getFirst()` / `getLast()` across all List/Deque types. |

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
