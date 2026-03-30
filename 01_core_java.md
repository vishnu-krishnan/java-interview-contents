<!-- Part of Java Learning Roadmap — Section 1 -->

# 📘 1. Core Java

---

## 1. Definition

**Java** is a high-level, statically-typed, object-oriented, platform-independent programming language developed by Sun Microsystems (now Oracle) in 1995. It follows the **WORA** (Write Once, Run Anywhere) principle — Java source code is compiled to **bytecode** which runs on any platform that has a **JVM** installed.

### 1.1 JDK vs JRE vs JVM

**Core Idea:**
JDK is for writing code, JRE is for running it, and JVM is the actual "engine" that executes the instructions.

**Deep Dive:**
*   **JDK (Java Development Kit):** The full toolbox. Contains the compiler (`javac`), debugger, and documentation tools (`javadoc`), plus the JRE.
*   **JRE (Java Runtime Environment):** The minimum set of files to run a Java app. Contains the JVM and core class libraries (`rt.jar`).
*   **JVM (Java Virtual Machine):** The abstract computer that converts **bytecode** into **machine code** for your specific OS.

**Advanced Insight:**
The JVM is actually "stack-based" (it uses an internal operand stack to perform calculations) rather than "register-based" like a real CPU. This makes bytecode extremely portable because it doesn't rely on a specific number of CPU registers.

**Pitfall:**
Installing only the JRE and trying to run `javac`. You'll get a "Command not found" error. Developers always need the JDK.

**Production Tip:**
In modern containerized environments (Docker), we use a "Slim JDK" or "JRE" in the final image to keep the image size small and reduce the security attack surface (no compilers in production!).

**Interview Trap:**
"Is the JVM platform independent?"
**Answer:** **No.** The JVM is platform-dependent (there's a different JVM for Windows, Mac, and Linux). It is the **Bytecode** that is platform independent.

---

## 2. Why It Exists

Java was designed to solve three key problems of earlier languages (C/C++):

| Problem | Java's Solution |
|---|---|
| Platform dependency | JVM abstracts the OS — same bytecode everywhere |
| Manual memory management | Automatic Garbage Collection |
| Unsafe pointer arithmetic | No raw pointers — reference types with bounds checking |
| Low code reuse | OOP with inheritance and interfaces |

**Key design goals:** Simple, Secure, Portable, Robust, Multithreaded, High-performance.

---

## 3. How It Works Internally

### 3.1 Compilation & Execution Flow

**Core Idea:**
Java code follows a two-step process: Compile once (to universal bytecode) and Interpret/JIT everywhere (to specific machine code).

**Deep Dive:**
1.  **Compile-time:** `javac` converts `.java` into `.class` (bytecode). This is just a set of instructions for the JVM.
2.  **Runtime:** The JVM loads the bytecode, verifies it for safety, and then passes it to the **Execution Engine**.

**Advanced Insight (JIT & Tiered Compilation):**
The JVM doesn't just "interpret" bytecode line-by-line (which is slow). It uses the **JIT (Just-In-Time) Compiler**. It identifies "hot" methods (code run many times) and compiles them directly into **native machine code**. This is why Java apps "warm up" and get faster over time.

**Pitfall:**
Assuming bytecode is as fast as C++ binary immediately. Java requires a "warm-up" period for the JIT to kick in and optimize the hot paths.

**Production Tip:**
For low-latency applications, avoid frequent restarts. Every restart resets the JIT optimizations, making the first few thousand requests slower than the rest.

**Interview Trap:**
"What is the role of the Bytecode Verifier?"
**Answer:** Security. It ensures the bytecode doesn't perform illegal operations like jumping to invalid memory addresses or violating access modifiers, preventing malicious code from crashing the OS.

### 3.2 JVM Memory Areas (Run-Time Data Areas)

**Core Idea:**
The JVM splits memory into functional zones. The **Stack** is for short-lived personal tasks (threads), and the **Heap** is for long-lived shared data (objects).

**Deep Dive:**
*   **Heap:** Shared by all threads. This is where Garbage Collection happens.
*   **Stack:** Private to each thread. It stores "Frames" (local variables, partial results). When a method finishes, its frame is "popped" and memory is reclaimed instantly.

**Advanced Insight (Escape Analysis):**
The JVM uses **Escape Analysis** to see if an object "escapes" a method. If it doesn't, the JVM might allocate that object on the **Stack** instead of the Heap to avoid GC entirely. This is a massive performance optimization.

**Pitfall:**
**Memory Leaks in the Heap.** Objects that are no longer needed but are still referenced (e.g., in a static List) cannot be GC'd. The Stack never leaks memory because it's cleared automatically as methods return.

**Production Tip:**
If you see `OutOfMemoryError`, look at the Heap. If you see `StackOverflowError`, look for infinite recursion in your calls.

**Interview Trap:**
"Are primitive variables always stored on the Stack?"
**Answer:** **No.** If a primitive is a field in a class (e.g., `class User { int age; }`), it is stored on the **Heap** as part of the object. Only local primitives inside methods are stored on the Stack.

### 3.3 Data Types

**Primitives (stored on Stack):**

| Type | Size | Default | Range |
|---|---|---|---|
| `byte` | 1 byte | 0 | -128 to 127 |
| `short` | 2 bytes | 0 | -32,768 to 32,767 |
| `int` | 4 bytes | 0 | -2³¹ to 2³¹-1 |
| `long` | 8 bytes | 0L | -2⁶³ to 2⁶³-1 |
| `float` | 4 bytes | 0.0f | ~7 decimal digits |
| `double` | 8 bytes | 0.0d | ~15 decimal digits |
| `char` | 2 bytes | '\u0000' | 0 to 65,535 (Unicode) |
| `boolean` | ~1 bit | false | true / false |

**Reference types** (stored on Heap): `String`, arrays, all objects.

### 3.4 String Internals & The Pool

**Core Idea:**
Strings are immutable (unchanging). To save memory, Java reuses identical string literals in a special space called the **String Pool**.

**Deep Dive:**
*   **Immutability:** Once a `String` object is created, its value cannot be changed. This makes them inherently **thread-safe**.
*   **Pool Re-use:** When you write `String s = "Hello"`, Java checks the pool first. If "Hello" exists, it returns the reference. 

**Advanced Insight:**
String immutability is the secret to **HashMap performance**. Since the String value never changes, its `hashCode` can be calculated once and cached. If Strings were mutable, using them as HashMap keys would be a disaster.

**Pitfall:**
Using `new String("hello")`. This creates two objects: one in the pool (if not there) and a totally unnecessary one on the heap. Always use literals.

**Production Tip:**
For building complex strings (like JSON or long log messages), always use **`StringBuilder`**. Using `+` in a loop creates thousands of temporary String objects, causing high GC activity.

**Interview Trap:**
"Why is String immutable for security?"
**Answer:** Imagine a database connection string or a file path. If you pass a String to a validation method, and it could be changed by another thread *after* validation but *before* use, it would create a massive security hole (TOCTOU attack).

### 3.5 Wrapper Classes & Autoboxing

**Core Idea:**
Object-oriented "jackets" for primitives. They allow you to use numbers and booleans inside Collections (which only accept objects).

**Deep Dive:**
*   **Autoboxing:** Java automatically converts a primitive to its wrapper (`int` → `Integer`).
*   **Unboxing:** Automatically converts a wrapper back to a primitive (`Integer` → `int`).
*   **Integer Cache:** To save memory, Java caches `Integer` objects for values between **-128 and 127**.

**Advanced Insight:**
Autoboxing creates a **new object** on the heap every time it happens (outside the cache). In a loop that runs 1 million times, `Integer sum = 0; sum += i;` creates 1 million objects, putting massive pressure on the Garbage Collector.

**Pitfall:**
**NullPointerException during Unboxing.** If you have an `Integer x = null;` and you try to use it as an `int y = x;`, Java will throw an NPE because it can't call `.intValue()` on `null`.

**Production Tip:**
Avoid using wrapper classes in performance-critical math or high-frequency loops. Stick to primitives (`int`, `double`) to keep your data on the **Stack** and avoid heap allocation.

**Interview Trap:**
"What happens if you compare two `Integer` objects with `==`?"
**Answer:** It compares their **memory addresses**. It works for -128 to 127 because of the cache, but fails for other values. **Always use `.equals()` for wrappers.**

---

### 3.6 Java Generics (Type Erasure & Wildcards)

**Core Idea:**
A way to write "template" code that works with any type while maintaining **compile-time safety**.

**Deep Dive:**
*   **Type Erasure:** At runtime, Java "removes" the generic types (`List<String>` becomes `List<Object>`). This is done for backward compatibility with older Java versions.
*   **Wildcards:** 
    *   `? extends T` (Upper Bound): Reading only. You can read T, but not add anything.
    *   `? super T` (Lower Bound): Writing only. You can add T, but reading only gives you `Object`.

**Advanced Insight:**
Because of **Type Erasure**, you cannot use `instanceof` with generics (e.g., `if (list instanceof List<String>)` won't compile). To fix the eraure issue, the JVM generates "Bridge Methods" to ensure polymorphism works correctly with erased types.

**Pitfall:**
Creating a `new T()` inside a generic class. Because of erasure, the constructor `T` is unknown at runtime. You must pass a `Class<T>` or a `Supplier` to create objects.

**Production Tip:**
Follow the **PECS** rule (Producer Extends, Consumer Super). Use `<? extends T>` when you are only taking items out of a collection, and `<? super T>` when you are putting items into it.

**Interview Trap:**
"Can you use primitives in Generics (e.g., `List<int>`)?"
**Answer:** No. Generics require objects. Java 8+ uses **Autoboxing** to hide this, but it still stores `Integer` objects, not raw `int` values. (Project Valhalla is working to fix this).

---

### 3.7 Immutable Class Design

**Core Idea:**
Building a class that is a "Read-Only" vault. Once created, it never changes.

**Deep Dive:**
1.  **Mark the class `final`** (so it can't be extended).
2.  **Make fields `private final`**.
3.  **No Setters**.
4.  **Constructor with deep copy** for mutable fields (like Lists or Dates).
5.  **Getters return deep copies** (don't return the original reference).

**Advanced Insight:**
String and all Wrapper classes are immutable. This makes them perfect for being keys in a **HashMap**. If a key's value changed *after* being put in the map, the map would never be able to find it again.

**Pitfall:**
**Shallow Copy Leak.** If your immutable class has a `List` and your constructor just does `this.list = list;`, the outside code still has a reference and can modify your "immutable" object.

**Production Tip:**
In Java 14+, use **`record`**. It automatically handles fields, constructor, `equals`, `hashCode`, and `toString` while being immutable by default.

**Interview Trap:**
"Is an immutable class always thread-safe?"
**Answer:** Yes. Since the state never changes, there is no risk of one thread seeing a "partially modified" state from another thread.

---

## 4. Code Examples

### 4.1 JDK / JRE / JVM check
```java
// Check Java version at runtime
System.out.println(System.getProperty("java.version"));   // e.g. 21.0.2
System.out.println(Runtime.version().feature());           // e.g. 21
```

### 4.2 Primitive vs Reference
```java
int x = 5;           // primitive — stored directly on stack
Integer y = 5;       // reference — points to Integer object on heap
Integer z = 5;
System.out.println(y == z);        // true  (Integer cache -128~127)
System.out.println(y.equals(z));   // true  (always use .equals() for objects)

Integer a = 200;
Integer b = 200;
System.out.println(a == b);        // false (outside cache range!)
System.out.println(a.equals(b));   // true
```

### 4.3 String Pool
```java
String s1 = "Java";
String s2 = "Java";
String s3 = new String("Java");

System.out.println(s1 == s2);        // true  — same pool reference
System.out.println(s1 == s3);        // false — s3 is a new heap object
System.out.println(s1.equals(s3));   // true  — same content
System.out.println(s3.intern() == s1); // true — intern() puts s3 into pool
```

### 4.4 StringBuilder vs StringBuffer vs String
```java
// BAD: String concatenation in loop — O(n²), creates n new String objects
String result = "";
for (int i = 0; i < 1000; i++) result += i;   // DON'T

// GOOD: StringBuilder — O(n), single mutable buffer
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) sb.append(i);
String result = sb.toString();   // DO

// StringBuffer — thread-safe (synchronized), use only when shared across threads
StringBuffer sbuf = new StringBuffer();
sbuf.append("safe");
```

### 4.5.1 Checked Exceptions: The "Recoverable" Failures

**Core Idea:**
A "contract-based" error. The compiler forces you to prepare for these because they involve things outside your control (Network, Disk, Database).

**When to Use:**
When the caller **must** handle the error to proceed safely (e.g., File not found, User not authorized, Invalid input from API).

**Deep Dive:**
*   **Physics:** Extends `java.lang.Exception`.
*   **Requirement:** Must be handled via `try-catch` or declared via `throws`.
*   **The Problem:** Leads to **"Exception Pollution."** If a low-level DB method throws `SQLException`, every method in the call stack must now `throws SQLException`, tightly coupling your architecture to the data layer.

**Advanced Insight:**
**Checked Exceptions vs. Lambdas.** Java's Functional Interfaces (like `Predicate` or `Function`) don't allow checked exceptions. This is why you cannot easily call a method that `throws IOException` inside a `.stream().map()`. You must wrap it in a `RuntimeException` or use a "Sneaky Throw" trick.

**Pitfall:**
**Swallowing exceptions to "quiet" the compiler.** Never write `catch(Exception e) {}` just to make the red line go away. If the file is missing, your app will later crash with a confusing `NullPointerException` because the data was never loaded.

**Production Tip:**
**Translate Exception layers.** Catch a checked `SQLException` in your Repository and throw a custom unchecked `DataAccessException`. This keeps your Service layer clean and independent of the database implementation.

---

### 4.5.2 Unchecked Exceptions: The "Programmer" Errors

**Core Idea:**
Errors that shouldn't happen if the code was perfect. They crash the thread immediately because there's usually no way to "fix" it mid-execution.

**When to Use:**
For logic errors (Null pointer, Array out of bounds) or fatal infrastructure failures where recovery is impossible (e.g., Connection pool exhausted).

**Deep Dive:**
*   **Physics:** Extends `java.lang.RuntimeException`.
*   **Advantage:** Cleaner code. It follows the **"Fail-Fast"** principle. No need to pollute every method with `throws` declarations.

**Advanced Insight:**
**The Global Exception Handler.** In modern Spring Boot/Microservices, architects prefer Unchecked Exceptions combined with a `@ControllerAdvice`. You throw the error deep in the code, and a single global class catches it and converts it into a clean JSON error for the user.

**Pitfall:**
**Lack of Documentation.** Since the compiler doesn't force you to declare them, developers often forget to mention which `@throws RuntimeException` a method might throw. Always document these in the **Javadoc**.

**Production Tip:**
For business logic failures (e.g., "Insufficient Funds"), use **Custom Unchecked Exceptions**. They are easier to manage in modern asynchronous and functional pipelines.

---

### 4.5.3 Exception Design for Production

| Feature | Checked Exception | Unchecked Exception |
|---|---|---|
| **Best For** | External/Recoverable errors (File IO) | Logic/Fatal errors (NPE, DB Down) |
| **Compiler** | Mandatory handling | Optional |
| **Pros** | Enforces safety and error-handling logic | Cleaner code, no declaration bloat |
| **Cons** | Brittle, couples code, breaks Lambdas | "Invisible" errors can surprise you at runtime |

**Architectural Rule of Thumb:** 
In 2024, the trend is toward **Unchecked Exceptions**. Only use Checked Exceptions if you genuinely expect the caller to perform a specific "Retry" or "Alternative" action when that error happens.

---

### 4.5.4 Multiple Catch & Union Catch

**Core Idea:**
Handling different types of broken pipes differently. You wouldn't fix a leaky faucet the same way as a blown circuit; multiple catches allow per-error logic.

**Deep Dive:**
*   **Sequential Catch:** Catching one exception after another. The most specific (lowest in the hierarchy) MUST come first.
*   **Union Catch (Java 7+):** Catching multiple, unrelated exceptions in a single block using the pipe `|` operator: `catch (IOException | SQLException e)`.

**Advanced Insight:**
In a **Union Catch**, the variable `e` is implicitly `final`. You cannot re-assign `e` inside that block. This is a compiler optimization to ensure the multi-type reference stays consistent.

**Pitfall:**
**Unreachable Bench.** If you catch `Exception` at the top, every catch block underneath it is "Unreachable" and will cause a compile-time error. Java forces you to be logical about your hierarchy.

**Production Tip:**
In many web apps, you don't need a catch for every possible error. Catch only what you can **actually fix**. For everything else, let it bubble up to the **Global Exception Handler**.

**Interview Trap:**
"Can you catch `IOException` and `FileNotFoundException` in a single union catch?"
**Answer:** **No.** You cannot union-catch exceptions that have a Parent-Child relationship (`FileNotFoundException` is a child of `IOException`). You must use separate blocks.

---

### 4.5.5 The `finally` Block

**Core Idea:**
The "Guaranteed Cleanup" officer. It runs no matter what happened in the try or catch.

**Deep Dive:**
Whether an exception was thrown, caught, or even if the `try` block returned early, `finally` will execute before the method finishes.

**Advanced Insight:**
**The Exit Strategy.** Exception to the rule: `finally` does NOT run if `System.exit(0)` is called, the JVM crashes, or the thread is killed.

**Pitfall:**
**Returning from `finally`.** If your `try` block returns `10` but your `finally` block returns `20`, the method will return `20`. This silently swallows any value or exception from the `try` block. **Never return from finally**.

**Production Tip:**
Only use `finally` for **Closing resources** (if not using try-with-resources) or for **Closing Locks** in multi-threaded code. For everything else, try-with-resources is superior.

**Interview Trap:**
"If a `try` block has a return statement, does `finally` still run?"
**Answer:** **Yes.** The return value is "stashed" away, `finally` runs, and then the method returns the stashed value.

---

### 4.5.6 Common Exceptions Survival Guide

| Exception | Type | Why it happens |
|---|---|---|
| **`NullPointerException`** | Unchecked | Calling a method on a `null` reference. |
| **`ClassCastException`** | Unchecked | Invalid downcasting (e.g., Cat → Dog). |
| **`ArithmeticException`** | Unchecked | Division by zero. |
| **`ArrayIndexOutOfBounds`** | Unchecked | Accessing `index < 0` or `index >= length`. |
| **`NumberFormatException`** | Unchecked | Parsing "abc" into an `int`. |
| **`IOException`** | **Checked** | General file/network failure. |
| **`SQLException`** | **Checked** | Database query failure. |
| **`ClassNotFoundException`** | **Checked** | Trying to load a class that doesn't exist at runtime. |

---

### 4.5.7 Full Production Exception Example

```java
public void processTransaction(Long userId, Double amount) {
    try (TransactionResource res = new TransactionResource()) {
        // Business logic
        if (amount > 1000000) {
            throw new FraudulentTransactionException("Too large", userId);
        }
        res.commit(userId, amount);
    } catch (FraudulentTransactionException | ValidationException e) {
        // High-level "fixable" errors
        log.warn("Business rule violation: " + e.getMessage());
        throw e; // rethrow for the UI layer
    } catch (Exception e) {
        // Low-level unexpected disasters
        log.error("Fatal system error during transaction", e);
        throw new SystemFailureException("Transaction failed", e); // Exception Chaining
    } finally {
        // Only for things NOT covered by try-with-resources
        System.out.println("Processing complete for user: " + userId);
    }
}
---

### 4.6 Try-With-Resources (AutoCloseable)

**Core Idea:**
Automatic cleanup. It ensures that files, database connections, and sockets are closed correctly, even if an error occurs.

**Deep Dive:**
Introduced in Java 7, it works with any class that implements the `AutoCloseable` or `Closeable` interfaces.
*   *Old way:* Manual `finally` block with nested `null` checks and `close()` calls.
*   *New way:* `try (Resource r = new Resource()) { ... }`.

**Advanced Insight:**
**Multiple Resources.** You can open multiple resources in one try: `try (A a = new A(); B b = new B())`. They are closed in the **reverse order** of their creation.

**Pitfall:**
Opening a resource outside the parentheses but using it inside. The auto-close ONLY works if the resource is declared inside the `try (...)` block starting in Java 7, or passed as a variable (effectively final) in Java 9+.

**Production Tip:**
Always prefer `try-with-resources` over manual `finally` blocks for **IO-bound** operations. It is cleaner, safer, and correctly handles suppressed exceptions during the closing phase.

**Interview Trap:**
"Does a resource have to be initialized inside the try-with-resources block?"
**Answer:** Not since Java 9. You can pass an already initialized variable as long as it is `final` or effectively final.

### 4.7 Keywords Deep Dive (final, static, transient, volatile)

**Core Idea:**
Keywords are modifiers that change how Java handles variables, methods, and memory visibility.

**Deep Dive:**
*   **`static`:** Belongs to the class, not an object. Shared by all instances.
*   **`final`:** Immutable constant (variable), non-overridable (method), non-extendable (class).
*   **`transient`:** Instructs the JVM to skip this field during **Serialization**.
*   **`volatile`:** Ensures that value changes are visible to all threads (memory barrier).

**Advanced Insight:**
`volatile` actually prevents **Instruction Reordering** by the CPU and JIT compiler. It ensures a **"Happens-Before"** relationship in the Java Memory Model (JMM), making sure one thread sees the most recent write from another.

**Pitfall:**
Assuming `volatile` is for thread-safety during math (`volatile int++`). It is NOT atomic. For counter increments, you MUST use `AtomicInteger` or `synchronized`.

**Production Tip:**
Use `transient` for sensitive data like passwords or temporary cache values in your DTOs to ensure they aren't accidentally leaked when writing objects to files or over the network.

**Interview Trap:**
"Can a `static` method be overridden?"
**Answer:** No. It can be **Hidden**, but not overridden. Overriding depends on the object type (polymorphism), while `static` depends on the class type.

---

### 4.8 Soft, Weak, and Phantom References

**Core Idea:**
Ways to hint to the Garbage Collector how "valuable" an object is.

**Deep Dive:**
*   **Strong Reference (Default):** GC never collects it as long as it's reachable.
*   **Soft Reference:** GC collects only if memory is low (ideal for caches).
*   **Weak Reference:** GC collects it at the **very next GC cycle** (ideal for `WeakHashMap`).
*   **Phantom Reference:** GC collects it, and the reference is put in a `ReferenceQueue` (used for cleanup tasks).

**Advanced Insight:**
**Direct Memory Cleanup.** Phantom references are often used by the JVM (and libraries like Netty) to clean up **Direct Buffers** (off-heap memory) which the standard GC cannot reach.

**Pitfall:**
Using `SoftReference` for a cache and forgetting that it can return `null` at any time. Always check `.get()` for null.

**Production Tip:**
Use `WeakHashMap` for metadata association where you don't want the map itself to prevent the keys from being garbage collected.

**Interview Trap:**
"What is the use of `phantom` references?"
**Answer:** To perform post-mortem cleanup. Unlike `finalize()`, they are reliable and don't slow down the GC or keep the object alive longer than necessary.

---

### 4.9 Type System: Upcasting and Downcasting

**Core Idea:**
Climbing up and down the inheritance tree. 

**Deep Dive:**
*   **Upcasting:** Implicit. Converting a child to a parent (`Dog` → `Animal`). Always safe.
*   **Downcasting:** Explicit. Converting a parent to a child (`Animal` → `Dog`). Requires a cast `(Dog) animal`.

**Advanced Insight:**
**ClassCastException.** This is a runtime error. If you downcast an `Animal` that is actually a `Cat` into a `Dog`, the JVM throws this error. Always use `instanceof` (or Pattern Matching in Java 16+) before downcasting.

**Pitfall:**
Overusing `instanceof` checks. This usually indicates a design flaw. Favor **Polymorphism** (interface methods) over manual type checking.

**Production Tip:**
In modern Java (17+), use **Pattern Matching for `instanceof`** to combine the check and the cast into one line: `if (obj instanceof String s) { ... }`.

**Interview Trap:**
"Can you cast between `Integer` and `String`?"
**Answer:** No. They do not have a parent-child relationship. This is a compile-time error. Casting only works within the same inheritance hierarchy.

### 4.7 Serialization & Externalizable
```java
// Serializable — marker interface, JVM handles everything
class Person implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    transient String password;   // excluded
}

// Write
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("p.ser"));
oos.writeObject(person);

// Read
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("p.ser"));
Person p = (Person) ois.readObject();

// Externalizable — full manual control
class Config implements Externalizable {
    String host; int port;
    public Config() {}  // REQUIRED — must have no-arg constructor

    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeObject(host);
        out.writeInt(port);
    }
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        host = (String) in.readObject();
        port = in.readInt();
    }
}
```

---

## 5. Interview Questions

### Conceptual

| Question | Answer |
|---|---|
| JDK vs JRE vs JVM | JDK = JRE + dev tools; JRE = JVM + libraries; JVM = bytecode executor |
| What is WORA? | Bytecode compiled once, runs on any JVM-equipped platform |
| Why is Java not 100% OOP? | 8 primitive types exist outside the object system |
| Heap vs Stack | Heap: objects, long-lived; Stack: method frames, primitives, LIFO, per-thread |
| Why is `String` immutable? | Thread-safety, String Pool reuse, security (passwords, URLs), hashCode caching |
| `==` vs `equals()` | `==` compares references (or primitive values); `equals()` compares content |
| Checked vs Unchecked exception | Checked: compile-time; must handle/declare. Unchecked: runtime; usually programmer error |
| `throw` vs `throws` | `throw` throws an exception instance; `throws` declares a method may throw |
| `final` vs `finally` vs `finalize()` | `final`=keyword; `finally`=cleanup block; `finalize()`=deprecated GC hook |
| What is `serialVersionUID`? | Unique ID for class version — prevents `InvalidClassException` during deserialization if class changes |

### Tricky / Output-Based

**Q: What is the output?**
```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
System.out.println(a == b);   // true  (Integer cache)
System.out.println(c == d);   // false (outside cache)
```

**Q: What is the output?**
```java
String s = "hello";
s.toUpperCase();
System.out.println(s);   // "hello" — String is immutable; toUpperCase() returns new object
```

**Q: Does `finally` always run?**
```java
// NO — finally does NOT run if:
// 1. System.exit() is called in try/catch
// 2. JVM crashes
// 3. Thread is killed (stop())
// Otherwise YES — even if catch rethrows an exception
```

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `String s1 == s2` for equality | Compares references, not content | Use `s1.equals(s2)` |
| `String` concat in loop | O(n²) — creates N new objects | Use `StringBuilder.append()` |
| Catching `Exception` too broadly | Hides root cause, masks different errors | Catch specific exceptions |
| Not closing resources | File/DB connection leak | Use `try-with-resources` |
| Ignoring `serialVersionUID` | `InvalidClassException` on deserialization after class change | Always declare it explicitly |
| `Integer a = 200; a == 200` logic | Outside cache range — fails with `==` | Always use `equals()` |
| Calling `finalze()` manually | Deprecated, unreliable timing | Use `try-with-resources` or `Cleaner` |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **String immutability** | HashMap keys (hashCode cached), HTTP headers, JWT tokens |
| **`StringBuilder`** | SQL query builders, JSON/XML serialization, template engines |
| **Checked exceptions** | File I/O (IOException), JDBC (SQLException) — forced handling |
| **`transient`** | Password fields in `User` entity to skip serialization |
| **`volatile`** | `running` flag in background threads (stop signal) |
| **`serialVersionUID`** | Sending objects over network / to cache (Redis via Java serialization) |
| **`try-with-resources`** | Database connections, file streams, HTTP clients — always used |

---

## 8. Practice Tasks

1. **String Pool explorer** — write a program that proves when `==` is `true` vs `false` for Strings, using literals, `new`, and `intern()`
2. **StringBuilder benchmark** — compare time taken for 10,000 loop concatenations with `String`, `StringBuilder`, and `StringBuffer`
3. **Custom exception hierarchy** — create `AppException → ServiceException → ValidationException`; throw and catch at different layers
4. **Serialization round-trip** — serialize a `User` object (with `transient password`), deserialize and verify password is `null`
5. **`final` keyword matrix** — demonstrate `final` on a variable, method, and class; show what each blocks
6. **Integer cache puzzle** — predict the output of `==` comparisons for values -200, -127, 0, 127, 128, 200

---

## 9. Quick Revision

```
JVM → executes bytecode | JRE = JVM + libs | JDK = JRE + compiler/tools

Primitives: 8 types → stored on Stack | Objects → stored on Heap

String is IMMUTABLE → pool reuse → always use .equals() not ==
StringBuilder → mutable, not thread-safe → use in loops
StringBuffer   → mutable, thread-safe (synchronized) → slower

Integer cache: -128 to 127 → == works | outside range → == fails → use .equals()

Checked exceptions    → compile-time → must handle/declare (IOException, SQLException)
Unchecked exceptions  → runtime → programmer error (NPE, ArrayIndexOutOfBounds)
try-with-resources    → auto-closes Closeable → always use for IO/DB

final   → variable: constant | method: no override | class: no extend
static  → belongs to class, shared
transient → skipped during serialization
volatile  → visibility across threads (NOT atomicity)

serialVersionUID → prevents InvalidClassException on class change
Externalizable   → full manual control over what gets serialized
```
