<!-- Part of Java Learning Roadmap — Section 5 -->

# ⚡ 5. Functional Programming in Java

---

## 1. Definition

**Functional Programming (FP)** is a declarative programming paradigm where applications are built by composing pure functions, avoiding shared state, mutable data, and side effects. 

Introduced in Java 8, it brings three core concepts to the language:
1.  **Lambdas:** Anonymous functions that can be passed around as data.
2.  **Functional Interfaces:** Interfaces with exactly one abstract method (SAM - Single Abstract Method), acting as types for Lambdas.
3.  **Streams API:** A declarative pipeline to process collections of objects in a functional style.

---

## 2. Why It Exists

*   **Conciseness (Boilerplate Reduction):** Replaces verbose Anonymous Inner Classes.
*   **Declarative Code:** You tell Java *what* you want to achieve (e.g., `filter -> map -> sum`), not *how* to achieve it (loops, counters, index checks).
*   **Easy Parallelism:** A `.stream()` can be instantly converted to `.parallelStream()` to utilize multi-core processors without writing raw thread management code, because FP assumes no shared mutable state.
*   **Null Safety:** `Optional<T>` forces developers to explicitly handle missing values instead of returning `null` blindly.

---

## 3. How It Works Internally

### 3.1 `invokedynamic` (Behind the scenes of Lambdas)
Unlike Anonymous Inner Classes which create a physical `.class` file on disk (like `MyClass$1.class`), Lambdas use the `invokedynamic` bytecode instruction. At runtime, the JVM dynamically generates the class and links it, reducing application size and memory overhead.

### 3.2 Stream Pipeline Execution (Lazy Evaluation)
A Stream does **not** process elements until a **Terminal Operation** (like `.collect()`, `.count()`, `.findFirst()`) is invoked.
*   **Intermediate Operations** (like `.filter()`, `.map()`) simply return a new Stream configuration.
*   When the terminal operation is called, the JVM performs "Loop Fusion" — processing elements down the entire pipeline in a single pass horizontally, rather than horizontally across each step.

### 4. Code Examples

### 4.1 Functional Interfaces & Lambdas
```java
// Predicate: takes T, returns boolean (used in filter)
Predicate<String> isLong = s -> s.length() > 5;

// Function: takes T, returns R (used in map)
Function<String, Integer> stringLength = s -> s.length();

// Consumer: takes T, returns nothing (used in forEach)
Consumer<String> printer = s -> System.out.println(s);

// Supplier: takes nothing, returns T (lazy loading)
Supplier<Double> randomGen = () -> Math.random();

// Method Reference shorthand (equivalent to printer above)
Consumer<String> cleanPrinter = System.out::println;
```

### 4.2 Stream Pipeline
```java
List<String> names = List.of("John", "Jane", "Tom", "Oliver", "Jake");

// Get all names starting with 'J', uppercase them, and collect to a Set
Set<String> jNames = names.stream()
    .filter(name -> name.startsWith("J"))   // Intermediate
    .map(String::toUpperCase)               // Intermediate
    .collect(Collectors.toSet());           // Terminal -> Triggers execution

System.out.println(jNames); // [JOHN, JANE, JAKE]
```

### 4.3 `map()` vs `flatMap()`
```java
// Map: 1-to-1 transformation
List<String> words = List.of("hello", "world");
List<Integer> lengths = words.stream()
    .map(String::length)
    .collect(Collectors.toList()); // [5, 5]

// flatMap: 1-to-Many transformation. Flattens nested streams.
List<List<Integer>> listOfLists = List.of(
    List.of(1, 2, 3), 
    List.of(4, 5)
);

List<Integer> flattened = listOfLists.stream()
    .flatMap(List::stream)  // Unpacks each inner list into the main stream
    .collect(Collectors.toList()); // [1, 2, 3, 4, 5]
```

### 4.4 Defensive `Optional` Usage
```java
public Optional<User> findUser(String email) {
    // Return Optional instead of null
    return database.find(email); 
}

// Client code: No NPE risk!
String userName = findUser("test@test.com")
    .map(User::getName)
    .orElse("Guest User"); 

// Throw exception if missing
User admin = findUser("admin@sys.com")
    .orElseThrow(() -> new RecordNotFoundException("Admin missing"));
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `map()` and `flatMap()`? | `map()` transforms each element into another object (One-to-One). `flatMap()` transforms each element into a Stream of objects, and then flattens all those streams into one single Stream (One-to-Many). |
| What is a Functional Interface? | An interface with EXACTLY one abstract method (SAM). It can have multiple `default` or `static` methods. Annotated with `@FunctionalInterface`. |
| Are Streams reusable? | **No**. Once a terminal operation is called, the stream is "closed". Reusing it throws `IllegalStateException: stream has already been operated upon or closed`. |
| Tell me the 4 core Functional Interfaces. | `Predicate` (Test), `Function` (Transform), `Consumer` (Side-effect), `Supplier` (Generate). |
| Difference between `Optional.of()` and `Optional.ofNullable()`? | `Optional.of(val)` throws a `NullPointerException` instantly if `val` is null (Fail-fast). `Optional.ofNullable(val)` safely returns an empty Optional if the value is null. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Modifying external variables inside a Lambda | Causes bugs, race conditions in parallel streams. Java requires external variables used in lambdas to be `final` or `effectively final`. | DO NOT use streams to modify external state. Return new collections using `collect()`. |
| Using `.get()` blindly on `Optional` | Can throw `NoSuchElementException` if the Optional is empty, defeating the entire purpose of Optional (avoiding exceptions). | Always use `.orElse()`, `.orElseThrow()`, or `ifPresent()`. |
| Putting heavy side effects in `.peek()` | `.peek()` should only be used for debugging/logging. It's an intermediate operation, meaning if a terminal operation optimizes the pipeline (like `.findFirst()`), peek won't run on all elements. | Use `.forEach()` at the end of the pipeline if you need true side effects. |
| Using `parallelStream()` blindly | Has massive overhead creating threads. Can actually be slower than sequential streams for small collections or I/O bound tasks. | Only use `parallelStream()` for massive CPU-intensive datasets. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **Streams + `filter/map`** | Extracting data from database DTOs to API Response Objects before sending them out to the frontend. |
| **`Collectors.groupingBy()`** | Generating reports. E.g., Grouping a List of `Transaction` objects by `Category` into a `Map<Category, List<Transaction>>`. |
| **`Optional`** | JPA/Spring Data Repository methods `findById(Long id)` return `Optional<T>` to force the developer to handle the "Not Found" 404 scenario properly. |
| **`Supplier`** | Lazy-loading heavy resources. Code block won't execute until `.get()` is called. |

---

## 8. Practice Tasks

1.  **Group and Count:** Take a list of Strings `["apple", "banana", "apple", "cherry"]`. Use Streams and `Collectors.groupingBy` with `Collectors.counting()` to generate a `Map<String, Long>` of word frequencies.
2.  **Chaining Optionals:** Create an `Order` object containing an `Optional<Customer>`, which contains an `Optional<Address>`, which contains an `Optional<String>` for ZipCode. Use deeply nested `.flatMap()` to safely extract the ZipCode without any null checks.
3.  **Custom Functional Interface:** Create a custom `@FunctionalInterface` called `TriFunction<A, B, C, R>`. Implement it with a lambda to add three integers and return the String result.
4.  **Infinite Stream:** Use `Stream.iterate(1, n -> n + 1)` combined with `.filter()` and `.limit(10)` to generate and print the first 10 even numbers.

---

## 9. Quick Revision

### Core API Mappings
| Interface | Method | Params | Returns | Use in Stream API |
|---|---|---|---|---|
| `Predicate<T>` | `.test(t)` | `T` | `boolean` | `.filter()` |
| `Function<T, R>`| `.apply(t)`| `T` | `R` | `.map()` |
| `Consumer<T>` | `.accept(t)`| `T` | `void` | `.forEach()`, `.peek()` |
| `Supplier<T>` | `.get()` | `None` | `T` | `orElseGet()`, `.generate()` |

### Key Stream Rules
*   **Lazy:** Data doesn't flow until the Terminal operation is hit.
*   **Single Use:** Streams cannot be traversed twice.
*   **Pure:** Never mutate the source collection inside the stream. 
*   **Flatten:** `flatMap()` is used to break down nested collections into a single horizontal stream.
*   **Optional:** `ofNullable()` safely handles nulls, never call `.get()` directly.
