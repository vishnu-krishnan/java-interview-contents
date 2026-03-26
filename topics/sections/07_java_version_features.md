<!-- Part of Java Learning Roadmap — Section 7 -->

## ☕ 16. Java Version Features & Implementations

### ☕ Java 8

- **Lambda Expressions** — `(params) -> expression`, replaces anonymous inner classes
- **Functional Interfaces** — `Predicate`, `Function`, `Consumer`, `Supplier`, `BiFunction`, `UnaryOperator`
  - Predicate chaining: `and()`, `or()`, `negate()`
  - Function chaining: `andThen()`, `compose()`
- **Streams API** — intermediate + terminal ops, `Collectors`
- **Optional\<T\>** — `orElse`, `orElseThrow`, `ifPresent`, `map`, `flatMap`
- **Default & Static Methods in Interfaces**
- **Method References** — static, instance, constructor
- **New Date/Time API** (`java.time`) — `LocalDate`, `LocalDateTime`, `ZonedDateTime`, `DateTimeFormatter`
- **Base64** Encoding/Decoding
- **CompletableFuture** — `supplyAsync`, `thenApply`, `thenCombine`, `exceptionally`
- **HashMap treeification** — linked list → Red-Black Tree at bucket size 8

### ☕ Java 11 *(First LTS after Java 8)*

- String methods: `isBlank()`, `strip()`, `lines()`, `repeat()`
- `var` in lambda parameters: `(var x, var y) -> x + y`
- Local-Variable Type Inference (`var`)
- **HTTP Client API** (`java.net.http`) — HTTP/1.1 & HTTP/2, sync + async
- `Files.readString()` / `Files.writeString()`
- `Optional.isEmpty()`
- Run single-file programs: `java HelloWorld.java`
- ZGC *(experimental)* — low-latency GC
- Epsilon GC *(experimental)* — no-op GC for perf testing
- Removal: Java EE, CORBA, `Thread.destroy()`, `Thread.stop()`

### ☕ Java 17 *(LTS)*

- **Sealed Classes** (`sealed`, `permits`) — restrict class hierarchy
- **Records** — immutable data classes, auto-generated boilerplate
- **Pattern Matching for `instanceof`** — eliminates explicit cast
- **Text Blocks** (`"""`) — multi-line strings
- **Switch Expressions** — value-returning `switch`, arrow syntax
- `Stream.toList()` — shorthand for `collect(Collectors.toList())`
- Pattern Matching in Switch *(preview)*
- Strong encapsulation of JDK internals
- Enhanced PRNG — `RandomGenerator` interface
- Deprecations: Applet API, Security Manager; Removed: RMI Activation

### ☕ Java 21 *(Latest LTS)*

- **Virtual Threads** (Project Loom)
  - `Thread.startVirtualThread(() -> ...)` — lightweight JVM-managed threads
  - Platform threads vs Virtual threads — 1 OS thread = ~1MB; 1 Virtual thread = ~few KB
  - 1,000,000 virtual threads possible with low memory
  - `spring.threads.virtual.enabled=true` in Spring Boot 3.2+
  - Pitfall: `synchronized` blocks pin carrier thread — use `ReentrantLock`
- **Structured Concurrency** *(preview)* — `StructuredTaskScope`
- **Sequenced Collections** — `SequencedCollection`, `SequencedMap`
- Pattern Matching in `switch` *(finalized)*
- Record Patterns *(finalized)*
- `String Templates` *(preview)*
- `Unnamed Classes` *(preview)*

---
