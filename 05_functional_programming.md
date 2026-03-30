<!-- Part of Java Learning Roadmap — Section 5 -->

# ⚡ 5. Functional Programming in Java

---

## 1. Introduction to Functional Programming (FP)

**Functional Programming (FP)** is a declarative programming paradigm emphasizing **Pure Functions**—functions that are deterministic, idempotent, and free of side-effects. 

> [!CAUTION]
> **Interviewer Note:** Many candidates claim FP is inherently "thread-safe." This is false if you pass shared mutable objects into a pipeline. True FP requires **Immutability**. If you capture a `List` and call `.add()` inside a lambda, you've violated FP principles and invited race conditions. 

### 1.1 Core Pillars in Java

**Core Idea:**
Lambdas allow you to pass a "behavior" (a piece of code) into a method just like you pass a piece of data (like a String or int).

**Deep Dive:**
This is enabled by **Functional Interfaces** (interfaces with exactly one abstract method). You don't need to write a whole class anymore; you just write the logic.

**Advanced Insight (Boxing Pressure):**
At the bytecode level, specialized interfaces like `IntPredicate` exist specifically to prevent **Autoboxing/Unboxing**. A `Stream<Integer>` creates a wrapper object for every element, causing massive **GC pressure**; `IntStream` uses a primitive `int[]` under the hood, bypassing the heap entirely for elements.

**Pitfall:**
**Capturing Mutable Variables.** Lambdas can only use local variables that are "effectively final." If you try to change a local variable from inside a lambda, it won't compile.

**Production Tip:**
Use **Method References** (`String::toUpperCase`) instead of lambdas (`s -> s.toUpperCase()`) whenever possible. They are cleaner, easier to read, and sometimes more optimized by the JIT compiler.

**Interview Trap:**
"Can a Functional Interface have multiple methods?" 
**Answer:** Yes, but only **one** can be `abstract`. It can have as many `default` or `static` methods as you want without breaking the SAM rule.

### 1.2 The `@FunctionalInterface` Annotation
*   **Definition:** Informative annotation used to strictly enforce SAM.
*   **Internal Detail:** Methods inherited from `java.lang.Object` (e.g., `toString`, `equals`) do NOT count toward the SAM limit.
*   > [!PITFALL]
    *   **Pitfall:** Adding a second abstract method to an existing FI breaks all lambda clients immediately. Always use the annotation to fail-fast during compilation.

---

## 2. Why Functional Programming Exists?

*   **Core Idea:** It shifts the focus from "how" (instruction-based) to "what" (intent-based), leading to cleaner, more maintainable code.

*   **Composability:** Building complex workflows by piping small, testable blocks.
*   **Conciseness:** Reduces "Ceremony Code," making the business logic the first-class citizen.
*   **Concurrency by Default:** Immutable state makes parallelization safe and trivial.
*   **Production Context:** In high-throughput microservices (Spring Cloud/Reactive), FP style reduces the risk of shared-state bugs (Race Conditions) that are nearly impossible to reproduce in staging.

---

## 3. Advanced Lambda Concepts

### 3.1 Target Typing & Poly Expression
*   **Core Idea:** The compiler looks at the surrounding code to determine which interface the lambda corresponds to.
*   **Internal Working:** Java uses **Structural Typing** for lambdas. The type is inferred via the **Target Typing** algorithm (JLS 15.27). A single lambda can satisfy multiple interfaces (e.g., `Runnable` and `Executor`).
*   > [!INTERVIEW TRAP]
    *   **Interview Trap:** "Does a lambda have a class at compile time?" **No.** It is a "Poly Expression." Its type is resolved only when associated with a Target Type.

### 3.2 Variable Capture & Scope
*   **Core Idea:** Lambdas can use variables from the method they are defined in, but only if those variables aren't changed after assignment.
*   **The Rule:** Local variables must be **effectively final**. 
*   **Advanced Insight:** Lambdas capture the **value**, not the reference. If Java allowed capturing mutable locals, it would lead to non-deterministic behavior in multi-threaded stream processing.
*   > [!PITFALL]
    *   **Pitfall:** **Memory Leaks via `this` capture.** If a lambda inside a non-static method captures an instance field, it implicitly captures the entire outer instance (`this`), preventing it from being Garbage Collected.
*   > [!ADVANCED INSIGHT]
    *   **Advanced Insight:** Inside a lambda, `this` refers to the **enclosing class** instance. In an Anonymous Inner Class, `this` refers to the **inner class** itself. This makes lambdas structurally different from classes.

---

## 4. Internal Workings: `invokedynamic`

### 4.1 Bytecode Level Evolution

**Core Idea:**
Before Java 8, every piece of logic needed a `.class` file. Lambdas use a special instruction called `invokedynamic` to create that logic in memory only when needed.

**Deep Dive:**
1.  **Java 7 and Below:** Anonymous inner classes generated separate `.class` files, bloating memory and increasing startup time.
2.  **Java 8+:** Uses the `invokedynamic` (indy) instruction.
    *   The first time a lambda is hit, a **Bootstrap Method (BSM)**—`LambdaMetafactory.metafactory`—is called.
    *   It dynamically generates a function object in memory (not on disk).
    *   Future calls use a cached **CallSite**, making it as fast as a direct method call.

**Advanced Insight:**
`invokedynamic` allows the JVM to defer the implementation strategy. Tomorrow, the JVM authors could change how lambdas are created under the hood, and your old code would run faster without being recompiled.

**Pitfall:**
**Capturing `this`.** If a lambda inside a class uses an instance field, it captures the entire object (`this`). If that lambda is stored in a static list, your object can't be garbage collected, leading to a memory leak.

**Production Tip:**
Lambdas are almost as fast as direct method calls. Don't avoid them for "performance" reasons unless you are in a Nano-second latency critical loop (HFT).

**Interview Trap:**
"Does a lambda have a 'this' context of its own?"
**Answer:** No. Inside a lambda, `this` refers to the **outer class**. This is a major difference from Anonymous Inner Classes where `this` refers to the inner class itself.

### 4.2 Stream Pipeline Execution (Lazy Evaluation & Loop Fusion)
*   **Core Idea:** Streams don't execute until you ask for a result. They "queue up" the work.
*   **Internal Working:** Streams build a linked list of `AbstractPipeline` objects. Only when a terminal operation is called does the `Sink` chain execute.
*   **Loop Fusion:** Instead of iterating N times for N operations, the JVM fuses them into a single pass. 
    *   *Example:* `filter(..).map(..)` does NOT create two loops; it creates one loop where each element is filtered and mapped immediately.
*   > [!PRODUCTION TIP]
    *   **Production Tip:** For resources like files or database connections, use **`Stream.onClose(Runnable)`** to ensure they are released. Streams that access external resources (like `Files.lines()`) implement `AutoCloseable`.

---

## 5. The "Big Four" Core Functional Interfaces

| Interface | Method | Producer/Consumer Logic | Production Use Case |
|---|---|---|---|
| **`Predicate<T>`** | `test(T)` | Boolean logic. | Validation chains, Security checks. |
| **`Function<T, R>`**| `apply(T)`| Transformation (1:1). | Entity-to-DTO mapping. |
| **`Consumer<T>`** | `accept(T)`| Side effects. | Logging, Async event publishing. |
| **`Supplier<T>`** | `get()` | On-demand creation. | Lazy DB connection, Factory patterns. |

### 5.2 Code Examples: The Big Four in Action

#### 1. Predicate<T> (The Validator)
**Logic:** Takes one input, returns `boolean`. Used for filtering and validation.
```java
Predicate<String> isValidEmail = s -> s.contains("@") && s.endsWith(".com");
System.out.println(isValidEmail.test("user@example.com")); // true

// Production Use Case: Chaining filters
list.stream().filter(isValidEmail.and(s -> s.length() > 5)).collect(toList());
```

#### 2. Function<T, R> (The Transformer)
**Logic:** Takes input `T`, returns output `R`. Used for mapping data.
```java
Function<String, Integer> wordLength = s -> s.length();
Integer size = wordLength.apply("Antigravity"); // 11

// Production Use Case: Entity to DTO mapping
Function<User, UserDTO> toDto = u -> new UserDTO(u.getId(), u.getName());
```

#### 3. Consumer<T> (The Side-Effect)
**Logic:** Takes input `T`, returns `void`. Used for actions with side effects (logging, DB writes).
```java
Consumer<String> logger = msg -> System.out.println("LOG: " + msg);
logger.accept("Transaction Started");

// Production Use Case: Processing items in a loop/stream
list.forEach(logger);
```

#### 4. Supplier<T> (The Producer)
**Logic:** Takes NO input, returns output `T`. Used for lazy constant generation or object creation.
```java
Supplier<Double> randomValue = () -> Math.random();
System.out.println(randomValue.get());

// Production Use Case: Lazy initialization or Factory patterns
Supplier<MyConnection> connection = () -> new MyConnection(url, user, pass);
```

### 5.3 Legacy & Extended Functional Interfaces

While the "Big Four" cover 90% of cases, Java provides specialized interfaces for common tasks.

#### 1. Comparator<T> (Custom Sorting)
**Method:** `int compare(T o1, T o2)`
**Logic:** Returns negative if `o1 < o2`, zero if equal, positive if `o1 > o2`.
```java
List<String> list = Arrays.asList("Apple", "Banana", "Kiwi");
// Lambda sorting (Descending)
list.sort((s1, s2) -> s2.compareTo(s1)); 

// Modern Production Tip: Use Comparator.comparing()
list.sort(Comparator.comparingInt(String::length).reversed());
```

#### 2. Runnable & Callable (Task Execution)
**Runnable:** `void run()`. No return, no checked exceptions. Default for basic `Thread`.
**Callable<V>:** `V call() throws Exception`. Returns result and handles exceptions. Used with `ExecutorService`.
```java
// Runnable (Simple task)
new Thread(() -> System.out.println("Processing async task")).start();

// Callable (Used with complex futures)
Callable<String> fetchTask = () -> {
    Thread.sleep(1000);
    return "API Success";
};
```

#### 3. The "Bi" Variants (Processing Pairs)
Use these when one input isn't enough.

| Interface | Method | Use Case |
|---|---|---|
| **`BiPredicate<T, U>`** | `test(T, U)` | Testing condition against two objects (e.g., comparing user/password). |
| **`BiFunction<T, U, R>`**| `apply(T, U)`| Transforming two inputs into one result (e.g., merging two objects). |
| **`BiConsumer<T, U>`** | `accept(T, U)`| Processing key-value pairs in a `Map.forEach()`. |

**Example (BiConsumer):**
```java
Map<String, Integer> map = Map.of("Alice", 1, "Bob", 2);
map.forEach((k, v) -> System.out.println(k + ": " + v));
```

#### 4. UnaryOperator<T> & BinaryOperator<T>
**Core Idea:** Specialized cases of `Function` where all types are the same.
*   **`UnaryOperator<T>`:** One input, same type output. (e.g., `String::toUpperCase`).
*   **`BinaryOperator<T>`:** Two inputs, same type output. (e.g., `sum`, `max`).

*   > [!ADVANCED INSIGHT]
    *   **Advanced Insight:** Using specialized interfaces like `BinaryOperator` is numerically more efficient in parallel streams because they help the compiler optimize the "Reduction" phase without unnecessary type casting.

### 5.1 The "Checked Exception" Problem
*   **Production Tip:** Java's core FIs do not allow checked exceptions. 
    *   *Solution:* Use a wrapper utility or libraries like **Vavr** (`Try.of(..)`) to handle exceptions within functional pipelines without `try-catch` blocks.

---

## 6. Streams API: Deep Dive

### 6.1 Parallel Streams: The Common Pool Trap
*   > [!CAUTION]
    *   **Production Tip:** `.parallelStream()` uses the common `ForkJoinPool`. If one long-running task (e.g., heavy I/O) blocks a thread in this pool, it starves **every other parallel stream in the entire JVM**.
    *   **Rule of Thumb:** Never use parallel streams for I/O bound tasks. Use them ONLY for CPU-intensive data processing on large datasets.

### 6.2 Short-Circuiting Operations
Operations that can finish before processing the entire source, providing significant performance gains:
*   **Intermediate:** `limit(n)` (stops after n elements).
*   **Terminal:** `anyMatch`, `findFirst`, `allMatch`.

### 6.3 Parallelism Internals: The Spliterator
While a `Collection` is about *storage*, a **`Spliterator`** is about *traversal and decomposition*.
*   **How it works:** In a `parallelStream()`, the `Spliterator.trySplit()` method recursively partitions the source into smaller chunks.
*   **Performance Trap:** If your source is a `LinkedList`, partitioning is $O(n)$, making parallel streams **slower** than sequential. Always use `ArrayList` or arrays for parallel processing (constant-time splitting).
*   **Stateful Parallel Ops:** Operations like `sorted()` or `distinct()` on a parallel stream are extremely expensive because they require a **global synchronization point** where all threads must stop and merge their local segments.

### 6.4 The "Brain" of the Stream: Spliterator Characteristics
A senior must understand the **Spliterator Flags** that dictate optimization:
*   **`DISTINCT`**: If the source has this flag, the stream will **skip** your `.distinct()` call entirely.
*   **`SORTED`**: Same as above; it bypasses `.sorted()` if already ordered.
*   **`IMMUTABLE` / `CONCURRENT`**: Determines if the stream needs to freeze the source or can live-check it.
*   **`SIZED`**: Allows `Collectors.toSet()` to pre-size the internal `HashMap`, significantly reducing re-hash costs.

### 6.5 Custom Collectors (`Collector.of`)
Standard collectors like `toList()` are basic. For high-performance aggregation, use the 4-part `Collector` logic:
1.  **Supplier:** Initial results container (e.g., `StringBuilder::new`).
2.  **Accumulator:** Adds an element to the container.
3.  **Combiner:** Merges two containers (used in parallel streams).
4.  **Finisher:** Final transformation (e.g., `.toString()`).

### 6.6 The Non-interference Rule (The "Don't Touch" Rule)
*   **The Rule:** You must NOT modify the source collection during the execution of a stream pipeline.
*   **Result:** Doing so leads to `ConcurrentModificationException` or non-deterministic behavior.
*   **Exception:** This applies only from the moment the **terminal operation** starts until it finishes.

### 6.6 Stateless vs. Stateful Operations
    *   **Performance Hit:** These require an "Intermediate Buffer." `sorted()` must pull **all** data into memory before moving to the next step ($O(n \log n)$ complexity).

### 6.7 `Reduce` vs. `Collect`: The Core Distinction

**Core Idea:**
`Reduce` is for combining values into a new, **immutable** result (like sum of numbers). `Collect` is for modifying a **mutable** container (like adding to a List).

**Deep Dive:**
*   **`reduce(identity, accumulator, combiner)`**: Designed for **Immutable Reduction**. It expects a new result object at every step.
*   **`collect(supplier, accumulator, combiner)`**: Designed for **Mutable Reduction**. It modifies the existing container (like a `StringBuilder` or `ArrayList`).

**Advanced Insight:**
In parallel streams, the `combiner` is the most important part. It tells Java how to merge the results from two different threads. If your logic isn't "associative" ($ (a+b)+c = a+(b+c) $), your parallel stream will give wrong answers.

**Pitfall:**
Using `reduce` to add items to a `List`. This is a performance disaster ($O(n^2)$) in parallel, as it tries to copy the entire list at every step. **Always use `collect` for collections.**

**Production Tip:**
When using `parallelStream()`, always ensure you are using it for **CPU-bound** tasks. For IO-bound tasks (DB calls, API calls), parallel streams can block the `commonPool` and slow down your entire application.

**Interview Trap:**
"Why does `reduce` have a 'Combiner' parameter when used with three arguments, but not when used with one?"
**Answer:** The combiner is only needed for **Parallel processing** to combine results from different threads. The single-argument version is sequential by nature.

---

## 7. `map()` vs `flatMap()`

*   **`map`**: Use for simple 1:1 field mapping. Returns `Stream<R>`.
*   **`flatMap`**: Use to flatten `Optional<T>` or `List<List<T>>`.
*   > [!ADVANCED INSIGHT]
    *   **Advanced Insight:** `flatMap` is significantly more expensive in terms of object allocation. Each call to `flatMap` creates a new internal `Stream` object for every element in the pipe. For performance-critical hot paths, a standard `for` loop may be superior.

---

## 8. Defensive `Optional` Usage

*   **Real-world Tradeoff:** `Optional` is an object. Using it for millions of records in a Stream significantly increases heap pressure.
*   > [!PRODUCTION TIP]
    *   **Production Tip:** **Never use `Optional` for fields or parameters.** It is designed **only** as a return type to indicate a potential absence of value.
*   **Interface Trap:** `Optional` is **NOT Serializable**. Do not use it in DTOs that will be processed by Java Serialization (e.g., old RMI or Session persistence).

---

## 9. Common Mistakes & Anti-Patterns

| Mistake | Why it Fails in Production | Corrective Action |
|---|---|---|
| **Side Effects in `peek()`** | `peek()` is intended for debugging. Some JIT optimizations might skip `peek` entirely if the terminal operation doesn't need to process that shard. | Use `forEach` or `map` for modifications. |
| **Infinite Streams without limit** | Causes `OutOfMemoryError` or infinite loops in production. | Always accompany `Stream.iterate` with `.limit()` or a `takeWhile` guard. |
| **Blind Parallelism** | Causes context switching overhead that exceeds computation time on small lists. | Profile with JMH before committing to parallel. |

---

## 10. Real-World Architectural Scenarios

### 10.1 Spring Boot / JPA Integration
Using `Optional` with `findById()` prevents the "Empty Result" bug. 
```java
return userRepository.findById(id)
    .map(userMapper::toDTO)
    .orElseThrow(() -> new ResourceNotFoundException("User " + id));
```

### 10.2 Reactor / WebFlux (Reactive Programming)
Functional style is the foundation of Reactive programming. Understanding `Mono`/`Flux` is impossible without mastering Java Lambdas and Streams.

---

## 11. Interview Traps & Tricky Questions

*   **Q1:** "Can a Stream be used twice?" -> **Answer:** No. `IllegalStateException`.
*   **Q2:** "What happens if you modify the underlying List while a Stream is processing?" -> **Answer:** `ConcurrentModificationException`. Streams are fail-fast.
*   **Q3:** "Which is faster: `for` loop or `stream()`?" -> **Answer:** Generally, `for` loops are faster due to less object overhead and zero abstraction cost. Streams are chosen for **maintainability** and **readability**, not raw speed.
*   > [!INTERVIEW TRAP]
    *   **Interview Trap:** "What is the result of `Stream.of(null).count()`?" 
    *   **Answer:** **1**. `Stream.of(null)` creates a stream with one element (which happens to be null). To create an empty stream, you must use `Stream.empty()`.

---

## 12. Master Mental Models

*   **The Assembly Line:** Stateless ops are fast-moving belts; Stateful ops are storage bins where everything must wait.
*   **The Blueprint:** A stream is a "Plan." Nothing happens until the "Investor" (Terminal Operation) commits funds.
*   **The Monad:** Streams and Optionals are containers that wrap values and provide safe ways to transform them without "touching" the internal state directly.
