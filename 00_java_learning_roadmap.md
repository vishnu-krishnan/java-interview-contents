# ☕ Java Learning Roadmap

A structured, end-to-end roadmap to master Java — from basics to production-grade backend development.  
Built for **interview preparation** and **production engineering** at all levels.

---

## 📘 [1. Core Java](01_core_java.md)

- Introduction to Java — JVM, JRE, JDK differences
- Setting Up Java Development Environment (JDK, IntelliJ, VS Code)
- Java Syntax and Structure
- Data Types and Variables (Primitive vs Reference)
- Operators and Expressions
- Control Flow Statements (`if-else`, `switch`)
- Loops (`for`, `while`, `do-while`, enhanced `for`)
- Functions and Methods (varargs, recursion)
- **String Internals**
  - Immutability and String Pool
  - `==` vs `.equals()` vs `.compareTo()`
  - `String`, `StringBuilder`, `StringBuffer` — differences and performance
  - `intern()`, `concat()`, `replace()`, `split()`
- **Exception Handling**
  - Checked vs Unchecked Exceptions
  - `try-catch-finally`, `try-with-resources`
  - `throw` vs `throws`
  - Custom Exception design
  - Exception chaining
- **Keywords Deep Dive**
  - `final`, `static`, `transient`, `volatile`
  - `this` vs `super`
- **Type System**
  - Autoboxing / Unboxing
  - Type casting (widening, narrowing)
  - Generics and Type Erasure
  - Wildcards (`? extends T`, `? super T`)
- **Immutable Class Design**
  - `final` class + `final` fields + no setters + deep copy
- Serialization, Deserialization, `serialVersionUID`
  - `Serializable` marker interface — no methods, just opt-in
  - `transient` — field skipped during serialization, reset to default on deserialization
  - `Externalizable` — full custom control via `writeExternal()` + `readExternal()` + mandatory no-arg constructor
- **Wrapper Classes & Autoboxing**
  - Wrappers: `int→Integer`, `long→Long`, `double→Double`, `char→Character`, `boolean→Boolean`
  - Purpose: use primitives in Collections, provide utility methods, support `null`
  - Autoboxing: `Integer i = 42;` — auto-converts primitive to wrapper
  - Unboxing: `int j = i;` — auto-converts wrapper to primitive
  - Common methods: `Integer.parseInt()`, `Integer.valueOf()`, `Double.parseDouble()`
  - Pitfall: `Integer a = 127; Integer b = 127; a == b` → `true` (cache); `Integer.valueOf(200) == Integer.valueOf(200)` → `false`
- Soft, Weak, and Phantom References (`java.lang.ref`)
- `equals()` and `hashCode()` contract

---

## 🧱 [2. Object-Oriented Programming (OOP) in Java](02_oop_in_java.md)

- Classes and Objects
- Constructors (default, parameterized, copy)
- Inheritance — single, multilevel; why no multiple inheritance with classes
- Polymorphism — compile-time (overloading) vs runtime (overriding)
- Encapsulation — access modifiers, getters/setters
- Abstraction — Abstract Class vs Interface — when to choose which
- Interfaces vs Abstract Classes (Java 8+ default/static methods)
- `static` and `final` Keywords
- Inner Classes, Anonymous Classes, Local Classes
- **Aggregation vs Composition** — has-a relationship types
- Covariant return types and Method Hiding
- **SOLID Principles**
  - **S** — Single Responsibility Principle
  - **O** — Open/Closed Principle
  - **L** — Liskov Substitution Principle
  - **I** — Interface Segregation Principle
  - **D** — Dependency Inversion Principle
- `Comparable<T>` vs `Comparator<T>` — `compareTo()` vs `compare()`
- Enums — methods, constructors, `EnumSet`, `EnumMap`

---

## 📦 [3. Java Collections Framework](03_collections_framework.md)

- Arrays vs Collections
- **List**: `ArrayList`, `LinkedList`, `Vector`, `Stack`
  - `ArrayList` vs `LinkedList` — performance tradeoffs
- **Set**: `HashSet`, `LinkedHashSet`, `TreeSet`
- **Map**: `HashMap`, `LinkedHashMap`, `TreeMap`, `Hashtable`
  - **HashMap Internals**
    - Hashing, buckets, collision handling
    - Linked list → Red-Black Tree at threshold 8 (capacity ≥ 64)
    - Load factor (default 0.75), resizing/rehashing
    - `equals()` + `hashCode()` contract for keys
  - `LinkedHashMap` — insertion/access order
  - `TreeMap` — natural ordering, `Comparator`
- **Queue**: `PriorityQueue`, `Deque`, `ArrayDeque`
  - `BlockingQueue` — `LinkedBlockingQueue`, `ArrayBlockingQueue`
- **Concurrent Collections**
  - `ConcurrentHashMap` — segment locking / CAS, no null keys
  - `CopyOnWriteArrayList` — fail-safe iteration
  - `ConcurrentLinkedQueue`
- **Iterators**
  - Fail-Fast (`ConcurrentModificationException`) vs Fail-Safe (copy-on-read)
  - `Iterator` vs `ListIterator`
- Utility Classes
  - `Collections` — `sort()`, `synchronizedList()`, `unmodifiableList()`, `emptyList()`
  - `Arrays` — `sort()`, `binarySearch()`, `copyOf()`
- Special Maps
  - `WeakHashMap` — GC-eligible keys
  - `IdentityHashMap` — reference equality
- **LRU Cache** — implemented with `LinkedHashMap` (`accessOrder=true`)

---

## 🔀 [4. Java Concurrency & Multithreading](04_concurrency_and_multithreading.md)

- Thread Lifecycle — NEW → RUNNABLE → BLOCKED → WAITING → TIMED_WAITING → TERMINATED
- Creating Threads — `Thread` class, `Runnable`, `Callable`
  - `start()` vs `run()` — key difference
- **Synchronization**
  - `synchronized` — method-level and block-level
  - `volatile` — visibility only, no atomicity
  - `volatile` vs `synchronized` — key differences
  - `ReentrantLock`, `ReadWriteLock`, `StampedLock`
- **Java Memory Model (JMM)**
  - Happens-before relationship
  - Main memory vs CPU cache visibility
- **Common Concurrency Problems**
  - Race Condition — causes and fixes
  - Deadlock — causes, detection, prevention
  - Livelock — threads busy but making no progress
  - Starvation — thread never gets CPU time
- **Executor Framework**
  - `ExecutorService`, `ScheduledExecutorService`
  - Thread pool types: `newFixedThreadPool`, `newCachedThreadPool`, `newSingleThreadExecutor`
  - `submit()` vs `execute()`
- **`Future` and `CompletableFuture`**
  - `Future.get()` blocking behavior
  - `CompletableFuture.supplyAsync()`, `thenApply()`, `thenCompose()`, `thenCombine()`, `exceptionally()`, `allOf()`, `anyOf()`
- **Atomic Classes**
  - `AtomicInteger`, `AtomicLong`, `AtomicReference`
  - CAS (Compare-And-Swap) operations
- **`ThreadLocal`** — thread-scoped state, pitfalls with thread pools
- Synchronization Utilities
  - `CountDownLatch` — wait for N events
  - `CyclicBarrier` — N threads meet at a point
  - `Semaphore` — limit concurrent access
  - `Phaser` — flexible lifecycle
- `ForkJoinPool` — work-stealing, parallel streams
- Parallel Streams — when to use and when NOT to use
- Daemon Threads vs User Threads
- `wait()`, `notify()`, `notifyAll()` — inter-thread communication
- `sleep()` vs `wait()` — lock release behavior
- Connection Pool misconfiguration — thread pool vs DB pool mismatch
- Production scenarios — thread starvation, silent thread death, retry overload

---

## ⚡ [5. Functional Programming in Java](05_functional_programming.md)

- Lambda Expressions — `(params) -> expression`
- **Functional Interfaces** (`@FunctionalInterface`)
  - `Predicate<T>` — `test()`, `and()`, `or()`, `negate()`
  - `Function<T,R>` — `apply()`, `andThen()`, `compose()`
  - `Consumer<T>` — `accept()`, `andThen()`
  - `Supplier<T>` — `get()`
  - `BiFunction<T,U,R>`, `BinaryOperator<T>`, `UnaryOperator<T>`
- **Streams API**
  - Creating: `stream()`, `parallelStream()`, `Stream.of()`, `Stream.iterate()`
  - Intermediate: `filter()`, `map()`, `flatMap()`, `sorted()`, `distinct()`, `limit()`, `skip()`, `peek()`
  - Terminal: `collect()`, `forEach()`, `reduce()`, `count()`, `findFirst()`, `findAny()`, `anyMatch()`, `allMatch()`, `noneMatch()`
  - **Collectors**: `toList()`, `toSet()`, `toMap()`, `groupingBy()`, `partitioningBy()`, `joining()`, `counting()`, `collectingAndThen()`
  - Parallel Streams — pitfalls with shared mutable state
- **`Optional<T>`**
  - `of()`, `ofNullable()`, `empty()`
  - `isPresent()`, `isEmpty()`, `ifPresent()`, `orElse()`, `orElseGet()`, `orElseThrow()`, `map()`, `flatMap()`
- Method References — `Class::method`, `obj::method`, `Class::new`
- Default & Static Interface Methods

---

## 💾 [6. Java Input/Output (I/O)](06_java_io.md)

- File Handling (`FileReader`, `FileWriter`, `BufferedReader`, `BufferedWriter`)
- Byte Streams (`InputStream`, `OutputStream`)
- Character Streams (`Reader`, `Writer`)
- Serialization and Deserialization (`ObjectInputStream`, `ObjectOutputStream`)
- `serialVersionUID` — versioning and compatibility
- `NIO` (`java.nio`) — `Path`, `Files`, `Channels`, `ByteBuffer`
- `Files` utility — `readString()`, `writeString()`, `walk()`, `list()`

---

## ☕ [7. Java Version Features & Implementations](07_java_version_features.md)

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

## 🚀 [8. Advanced Java Topics](08_advanced_java_topics.md)

- **JVM Internals**
  - JVM Architecture — Class Loader, Runtime Data Areas, Execution Engine
  - Class Loading — Bootstrap, Platform, Application ClassLoader
  - Bytecode Verification
  - JIT Compilation — interpreted vs compiled
- **Memory Management**
  - Heap (Young Gen: Eden + Survivors, Old Gen), Stack, Metaspace, Code Cache
  - Stack Overflow — causes (deep recursion)
  - Memory Leak — objects retained via collections, caches, listeners
- **Garbage Collection**
  - GC Algorithms — Serial, Parallel, CMS, G1, ZGC, Shenandoah
  - GC Tuning — `-Xms`, `-Xmx`, `-XX:+UseG1GC`
  - GC Pause analysis — `OutOfMemoryError` types
- **Java Reflection API** — `Class<?>`, `Method`, `Field`, dynamic invocation
- **Annotations** — meta-annotations, custom annotation processing
- **Java Modules** (`module-info.java`) — JPMS (Java 9+)
- **Performance Anti-Patterns**
  - String concatenation in loops → use `StringBuilder`
  - Catching generic `Exception`
  - Returning `null` instead of empty collection
  - Magic numbers — use named constants
  - One method doing everything — Single Responsibility

---

## 🎨 [9. Design Patterns](09_design_patterns.md)

### Creational Patterns
- **Singleton** — lazy init, double-checked locking (`volatile`), thread-safe, Enum singleton
- **Factory Method** — decouple object creation from usage
- **Abstract Factory** — families of related objects
- **Builder** — step-by-step complex object construction
- **Prototype** — clone existing objects

### Structural Patterns
- **Adapter** — bridge between incompatible interfaces
- **Decorator** — add behavior dynamically
- **Proxy** — control access (Spring AOP uses proxy)
- **Facade** — simplified interface to a complex subsystem
- **Composite** — tree structures

### Behavioral Patterns
- **Strategy** — swap algorithms at runtime (e.g., payment methods)
- **Observer** — event/listener model (Spring Events)
- **Command** — encapsulate requests as objects
- **Template Method** — define skeleton, subclasses fill in steps
- **Chain of Responsibility** — pass request through handlers
- **Iterator** — traverse collections without exposing structure

### Patterns in Spring Boot
| Pattern | Spring Boot Usage |
|---|---|
| Singleton | Spring Beans (default scope) |
| Factory | `BeanFactory`, `ApplicationContext` |
| Proxy | AOP, `@Transactional`, `@Cacheable` |
| Template Method | `JdbcTemplate`, `RestTemplate` |
| Observer | `ApplicationEvent`, `@EventListener` |
| Strategy | `AuthenticationProvider`, `HandlerMapping` |

### LLD Practice Problems
- Parking Lot
- Notification Service (email/SMS/push)
- URL Shortener
- BookMyShow
- LRU Cache

---

## 🗄️ [10. Java Database Connectivity (JDBC)](10_jdbc.md)

- Connecting Java with Databases (`DriverManager`, `Connection`)
- `Statement` vs `PreparedStatement` vs `CallableStatement`
- CRUD Operations in JDBC
- Connection Pooling — HikariCP configuration and tuning
- Connection pool exhaustion — causes and fixes
- Transactions in JDBC — `commit()`, `rollback()`, `setAutoCommit(false)`

---

## 🗄️ [11. Databases (SQL & NoSQL)](11_databases_sql_nosql.md)

### 🗃️ SQL & Relational Databases

- Relational Database Concepts (Tables, Keys, Normalization — 1NF/2NF/3NF/BCNF)
- **Core SQL**
  - DDL: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
  - DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
  - `DELETE` vs `DROP` vs `TRUNCATE` — differences
  - Joins: `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, `SELF`, `CROSS`
  - Subqueries, Nested Queries, CTEs (`WITH` clause)
  - Aggregation: `GROUP BY`, `HAVING`, `ORDER BY`
  - `WHERE` vs `HAVING` — filtering rows vs groups
- **Window Functions**
  - `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`
  - `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`
- **Common SQL Interview Patterns**
  - 2nd / Nth highest salary — subquery + `LIMIT/OFFSET`
  - Find duplicates and delete keeping one
  - Top N records per group
  - Employees with no manager (self-join)
  - Average salary per department
- **Views** — virtual table, updatable views
- **Stored Procedures vs Functions**
- Indexing — B-Tree, Composite Index, Covering Index, `EXPLAIN` plan analysis
- Transactions — ACID properties, Isolation Levels (`READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`)
- **Database Design for Scale**
  - Sharding vs Partitioning (horizontal vs vertical)
  - Read-heavy vs Write-heavy system design
  - Read replicas
- Popular Databases: **MySQL**, **PostgreSQL**

### 🍃 NoSQL Databases

- Relational vs Non-Relational — when to choose
- Types of NoSQL
  - **Document Store**: MongoDB
  - **Key-Value Store**: Redis
  - **Column Family**: Apache Cassandra
  - **Graph DB**: Neo4j
- CAP Theorem — Consistency, Availability, Partition Tolerance
- **MongoDB**
  - Collections, Documents, BSON
  - CRUD Operations
  - Aggregation Pipeline
  - Indexing in MongoDB
- **Redis**
  - Caching Strategies — Cache-Aside, Write-Through, Write-Behind
  - Data Structures: Strings, Hashes, Lists, Sets, Sorted Sets
  - TTL (Time To Live) and Eviction Policies
  - Distributed Locking with Redis
- Consistent Hashing — distribution of data across nodes
- Database per Service pattern (Microservices)

---

## 🔗 [12. Hibernate & JPA](12_hibernate_and_jpa.md)

- ORM (Object-Relational Mapping) Concepts
- **JPA (Java Persistence API)**
  - `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`
  - `EntityManager` and Persistence Context
  - JPQL (Java Persistence Query Language)
  - Named Queries and Native Queries (`@Query`)
  - DTO Projection — read-only performance APIs
- **Hibernate as a JPA Implementation**
  - Hibernate Session and Session Factory
  - **Entity States**: Transient → Persistent → Detached → Removed
  - `save()` vs `persist()` vs `merge()` vs `saveAndFlush()`
  - First-Level Cache (Session) and Second-Level Cache (SessionFactory)
  - Lazy vs Eager Loading — performance implications
  - **N+1 Query Problem** — detection and fixes (JOIN FETCH, `@EntityGraph`, `@BatchSize`, DTO Projection, `SUBSELECT`)
  - Dirty Checking — how Hibernate detects changes automatically
- **Entity Relationships**
  - `@OneToOne`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`
  - Cascade Types (`PERSIST`, `MERGE`, `REMOVE`, `ALL`)
  - Fetch Types (`LAZY`, `EAGER`)
  - `@EmbeddedId` — composite keys
- HQL (Hibernate Query Language)
- Hibernate Criteria API
- **`@Transactional` Deep Dive**
  - Internal working (Spring proxy-based AOP)
  - Self-invocation pitfall — `this.method()` bypasses proxy; fix: inject self-reference
  - `rollbackFor = Exception.class` — by default only `RuntimeException` triggers rollback
  - `readOnly = true` — disables dirty checking, can use read replica
  - **Transaction Propagation Types**

    | Propagation | Behaviour |
    |---|---|
    | `REQUIRED` *(default)* | Join existing or create new |
    | `REQUIRES_NEW` | Always create new, suspend existing |
    | `NESTED` | Nested transaction — inner rollback doesn't affect parent |
    | `SUPPORTS` | Join existing if present, else no transaction |
    | `NOT_SUPPORTED` | Suspend existing, run without transaction |
    | `NEVER` | Must run without transaction — throws if one exists |
    | `MANDATORY` | Must run within existing transaction — throws if none |

- **Optimistic vs Pessimistic Locking**
  - **Optimistic** — no DB lock taken; `@Version` field checked on update; `OptimisticLockException` if version mismatch; best for high-read, low-write
  - **Pessimistic** — DB row locked for transaction duration; `@Lock(LockModeType.PESSIMISTIC_WRITE)`; best for financial/inventory writes

---

## 🌿 [13. Spring Framework](13_spring_framework.md)

- **Spring Core**
  - Inversion of Control (IoC)
  - Dependency Injection — Constructor (recommended), Setter, Field
  - `@Autowired`, `@Qualifier`, `@Primary`, `@Lazy`
  - `@Component`, `@Service`, `@Repository`, `@Controller`
  - `@Configuration`, `@Bean`
  - Spring Bean Lifecycle — `@PostConstruct`, `@PreDestroy`, `InitializingBean`, `DisposableBean`
  - Bean Scopes — Singleton, Prototype, Request, Session, Application
  - `ApplicationContext` vs `BeanFactory`
  - `CommandLineRunner` / `ApplicationRunner`
  - `@Value` vs `@ConfigurationProperties`
  - `SpringFactoriesLoader` — auto-configuration mechanism
- **Spring AOP** (Aspect-Oriented Programming)
  - Advice types: `@Before`, `@After`, `@AfterReturning`, `@AfterThrowing`, `@Around`
  - Pointcuts and Joinpoints
  - Cross-cutting concerns: logging, security, transactions
- **Spring MVC**
  - `DispatcherServlet` and full Request Lifecycle
  - `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, `@PatchMapping`
  - `@RequestBody`, `@ResponseBody`, `@PathVariable`, `@RequestParam`
  - `@ResponseStatus`, HTTP status codes
  - View Resolvers (Thymeleaf, JSP)
  - `@RestController` vs `@Controller`
- **Spring Security**
  - Authentication vs Authorization
  - JWT-based stateless auth flow
  - OAuth2 — Authorization Code flow, Client Credentials
  - Method-Level Security (`@PreAuthorize`, `@PostAuthorize`)
  - RBAC (Role-Based Access Control)
- **Spring Data JPA**
  - `JpaRepository`, `CrudRepository`, `PagingAndSortingRepository`
  - Derived query methods
  - `@Query` (JPQL and native SQL)
  - Pagination (`Pageable`, `Page<T>`) and Sorting (`Sort`)
- **Spring WebFlux** (Reactive)
  - `Mono<T>`, `Flux<T>`
  - `WebClient` vs `RestTemplate`
  - Reactive vs traditional — when to choose

---

## 🚀 [14. Spring Boot](14_spring_boot.md)

- Spring Boot vs Spring Framework
- **`@SpringBootApplication` Deep Dive** — combines 3 annotations:
  - `@Configuration` — marks class as Spring config, enables `@Bean` methods
  - `@EnableAutoConfiguration` — auto-configures beans based on classpath (e.g., adds Tomcat if `spring-web` present)
  - `@ComponentScan` — scans package + sub-packages for all stereotype annotations
  - ⚠️ If `@Controller`/`@Service` outside base package: add `@ComponentScan(basePackages = {"..."})`
- **Spring Boot Startup Sequence** (9 steps)
  1. `SpringApplication.run()` called
  2. Creates `ApplicationContext` (IoC container)
  3. `@ComponentScan` discovers all beans
  4. `@EnableAutoConfiguration` reads `META-INF/spring/factories`
  5. All `@Bean`, `@Service`, `@Repository`, `@Controller` instantiated
  6. `@Autowired` dependencies injected
  7. `@PostConstruct` methods called
  8. Embedded Tomcat (or Jetty/Undertow) starts on port 8080
  9. Application ready to serve requests
- Auto-Configuration — how it works (`@EnableAutoConfiguration`, `spring.factories`)
- Starters — `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, etc.
- `application.properties` / `application.yml` — externalized config
- Spring Boot Profiles (`@Profile`, `spring.profiles.active`)
- **Request Flow Internals**
  - Client → DispatcherServlet → HandlerMapping → HandlerAdapter → Controller → Service → Repository → DB → Response (Jackson serialization)
- **Building REST APIs**
  - `@RestController`, `@RequestMapping`
  - DTO pattern — Controller → DTO → Service → Mapper → Entity → Repository
  - Request Validation: `@Valid`, `@NotNull`, `@NotBlank`, `@Size`, `@Email`, `@Min`, `@Pattern`
  - Custom constraint validators (`@UniqueEmail`)
  - Exception Handling: `@ControllerAdvice`, `@ExceptionHandler`, structured error responses
  - `@ResponseStatus`, `ResponseEntity<T>`
  - HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE` — correct usage
  - Idempotency — `PUT`, `DELETE`, `GET` are idempotent
- **Caching**
  - `@Cacheable` — cache the result on first call
  - `@CacheEvict` — remove stale data
  - `@CachePut` — always update cache
  - Redis as distributed cache (`spring-boot-starter-data-redis`)
- **Scheduling**
  - `@Scheduled` — `fixedRate`, `fixedDelay`, `cron`
  - `@EnableScheduling`
- **Async Processing**
  - `@Async`, `@EnableAsync`
  - `CompletableFuture` in async service methods
- **Configuration**
  - `@ConditionalOnProperty`, `@ConditionalOnClass`
  - `@Value` and `@ConfigurationProperties`
- **Data Layer**
  - Spring Data JPA integration
  - Database Migrations: **Flyway** / **Liquibase**
  - HikariCP connection pool tuning — `maximum-pool-size`, `connection-timeout`, `idle-timeout`
- **Actuator & Monitoring**
  - Health checks (`/actuator/health`), metrics, info endpoints
  - Micrometer integration
  - Integration with Prometheus / Grafana
- **Security**
  - JWT + Spring Security full configuration
  - OAuth2 Resource Server
  - `NoSuchBeanDefinitionException` vs `NoUniqueBeanDefinitionException` — fixes
  - **CSRF** — Cross-Site Request Forgery; prevention: CSRF token, `SameSite` cookies, CORS headers
  - **Secrets Management** — never hardcode secrets; use HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Kubernetes Secrets
  - **mTLS** — Mutual TLS for service-to-service authentication in microservices
- **Testing**
  - `@SpringBootTest`, `@WebMvcTest`, `@DataJpaTest`
  - `@MockBean`, `@SpyBean`
  - `MockMvc` — controller testing
  - `Testcontainers` — real DB in tests
- **Packaging**
  - Embedded Tomcat — fat JAR
  - Building JAR / WAR
  - `spring.threads.virtual.enabled=true` — Virtual Thread support
  - Dockerizing a Spring Boot App
- **Production Issues & Real Fixes**
  1. **`OutOfMemoryError: Java heap space`** — Memory leak (unbounded static Map, `ThreadLocal` not cleared, cache without eviction). Fix: `jmap` heap dump → VisualVM/MAT analysis; use `WeakHashMap`, Caffeine cache with limits; always `ThreadLocal.remove()` in `finally`
  2. **`NullPointerException` in prod, not in dev** — Race condition, lazy bean not init'd, external API returns null. Fix: `Optional.ofNullable()`, `@NonNull` annotations
  3. **HikariPool connection timeout** — `@Transactional` holding connection too long, N+1 flooding DB, unclosed `ResultSet`. Fix: tune `maximum-pool-size`, reduce transaction scope, add pagination
  4. **`StackOverflowError` in JPA entity** — Bidirectional `@ManyToMany` with circular `toString()`/Jackson serialization. Fix: `@JsonManagedReference`/`@JsonBackReference` or `@JsonIgnore`
  5. **Slow API (latency spikes)** — N+1 queries, missing index, GC Full pause. Fix: `@EntityGraph`/`JOIN FETCH`, add index, switch to G1GC, use `@Async` for fire-and-forget
  6. **`ConcurrentModificationException`** — Modifying non-thread-safe collection during iteration. Fix: `CopyOnWriteArrayList`, `ConcurrentHashMap`, or `Iterator.remove()`
  7. **REST endpoints return 404** — Controller outside component scan path, wrong context path, wrong HTTP method. Fix: move to base package, check `server.servlet.context-path`
  8. **`@Transactional` not rolling back** — Self-invocation (`this.method()`) bypasses proxy, or checked exception used without `rollbackFor`. Fix: inject self; use `rollbackFor = Exception.class`
  9. **Kafka consumer lag keeps growing** — Consumer too slow, insufficient partitions, frequent rebalancing. Fix: increase `concurrency`, batch-process, add partitions
  10. **HTTP 500 prod but 200 dev** — Missing env variable, wrong DB URL, missing secret. Fix: validate with `@PostConstruct`, use Spring Cloud Config centralised config

---

## 🌐 [15. Web Development & API Design](15_web_development_and_api_design.md)

- Java Servlets, JavaServer Pages (JSP)
- **RESTful API Design Principles**
  - Statelessness, Uniform Interface, Resource-based URIs
  - HTTP Status Codes: 200, 201, 204, 400, 401, 403, 404, 409, 500, 503
  - HTTP Methods — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
  - Idempotency — which methods are idempotent
  - API Versioning — URI (`/v1/`), Header, Query Param
  - Pagination — `page`, `size`, `sort` parameters
  - HATEOAS
- **DTO Pattern** — separates API contract from domain model
- **Swagger / OpenAPI** documentation (`springdoc-openapi`)
- **Rate Limiting** — token bucket, sliding window
- GraphQL — alternative to REST for flexible queries
- **REST vs gRPC**

  | Feature | REST | gRPC |
  |---|---|---|
  | Protocol | HTTP/1.1 | HTTP/2 (multiplexing, streaming) |
  | Data Format | JSON (human-readable) | Protocol Buffers (binary, compact) |
  | Performance | Slower (JSON parsing) | Faster (binary serialization) |
  | Contract | OpenAPI/Swagger (optional) | `.proto` file (mandatory, strict) |
  | Browser Support | Excellent | Limited (needs gRPC-Web proxy) |
  | Streaming | Limited (SSE, WebSocket) | Native bi-directional streaming |
  | Best For | Public APIs, web clients | Internal microservice comms |

---

## 🧪 [16. Testing in Java](16_testing_in_java.md)

- **Unit Testing**
  - JUnit 5 — `@Test`, `@BeforeEach`, `@AfterEach`, `@Nested`, `@ParameterizedTest`
  - Mockito — `@Mock`, `@InjectMocks`, `when().thenReturn()`, `verify()`
  - `@ExtendWith(MockitoExtension.class)`
- **Integration Testing**
  - `@SpringBootTest` — full application context
  - `@WebMvcTest` — controller layer only
  - `@DataJpaTest` — repository layer with in-memory DB
  - `MockMvc` — HTTP request simulation
- **Test Doubles** — `@MockBean`, `@SpyBean`
- **Testcontainers** — spin up real Docker containers (Postgres, Redis, Kafka) in tests
- **TDD** (Test-Driven Development) — Red → Green → Refactor cycle
- **Test Best Practices**
  - Field injection → constructor injection for testability
  - Avoid `Optional.get()` without checking
  - No magic numbers — named constants
  - Single responsibility per method

---

## 🔧 [17. Java Build Tools & DevOps Basics](17_build_tools_and_devops.md)

- **Maven** — POM, lifecycle, plugins, dependency scopes
- **Gradle** — `build.gradle`, task system, incremental builds
- **Git** — `commit`, `branch`, `merge`, `rebase`, `cherry-pick`, `stash`, `reset`, `revert`
  - Branching strategies — Gitflow, trunk-based
- **CI/CD**
  - Jenkins — pipeline stages, `Jenkinsfile`
  - GitHub Actions — workflow YAML
  - SonarQube — static analysis, code coverage

---

## 🐳 [18. Docker & Kubernetes](18_docker_and_kubernetes.md)

- **Docker**
  - Image vs Container
  - `Dockerfile` — `FROM`, `RUN`, `COPY`, `EXPOSE`, `ENTRYPOINT`, `CMD`
  - Multi-stage builds
  - Docker Compose — multi-container apps
  - Dockerizing a Spring Boot App
- **JVM in Containers**
  - JVM ergonomics — heap sized to host, not container
  - `-XX:MaxRAMPercentage=75` — container-aware heap
  - JVM GC behavior under OOMKill
- **Kubernetes**
  - Pods, Deployments, Services, ConfigMaps, Secrets
  - Liveness & Readiness Probes — `/actuator/health`
  - Horizontal Pod Autoscaler (HPA)
  - Resource limits (`requests` and `limits`)
  - Blue-Green Deployment, Rolling Updates, Canary
- **Cloud Platforms**
  - AWS — EC2, S3, RDS, ECS, Lambda, ELB, IAM, CloudWatch
  - Azure, GCP basics

---

## ☁️ [19. Deployment and Cloud](19_deployment_and_cloud.md)

- Deploying Java Applications — JAR, WAR, containerized
- **Docker** — (see Section 14)
- **CI/CD** — Jenkins, GitHub Actions, GitLab CI
- **Cloud Platforms**
  - **AWS** — EC2, S3, RDS, ECS/EKS, Lambda, ELB, IAM, CloudWatch, SQS/SNS
  - **Azure** — App Service, Azure DevOps, AKS
  - **GCP** — Cloud Run, GKE, Cloud SQL
- Serverless — AWS Lambda + Spring Boot (SnapStart, AOT)
- Auto-Scaling — horizontal pod autoscaler, EC2 auto-scaling groups
- Blue-Green Deployment, Canary Releases, Rolling Updates

---

## 🌐 [20. Microservices Architecture](20_microservices_architecture.md)

- **Monolith vs Microservices** — tradeoffs, when to choose
- **Core Principles** — single responsibility, loose coupling, independent deployment
- **Service Communication**
  - Synchronous: REST (`RestTemplate`, `WebClient`), **Feign Client**
  - Asynchronous: Kafka, RabbitMQ, JMS
  - gRPC — high-performance RPC
- **API Gateway**
  - Spring Cloud Gateway, Nginx
  - Routing, rate limiting, auth enforcement, load balancing
- **Service Discovery**
  - Eureka (Netflix OSS), Consul
  - Client-side vs server-side discovery
- **Resilience Patterns**
  - **Circuit Breaker** — Resilience4j (`@CircuitBreaker`, CLOSED → OPEN → HALF-OPEN)
  - **Retry** with exponential backoff
  - **Bulkhead** — isolate failures
  - **Timeout** — prevent thread blocking
  - **Fallback** — graceful degradation
- **Distributed Transactions**
  - Why 2PC (Two-Phase Commit) is hard in microservices
  - **Saga Pattern**
    - Choreography — event-driven, no central coordinator
    - Orchestration — central saga orchestrator
- **CQRS** (Command Query Responsibility Segregation) — separate read/write models
- **Event-Driven Architecture**
  - Event sourcing — store events as source of truth
- **Data Management**
  - Database per Service pattern
  - Eventual consistency
  - Distributed Locking (Redis `SETNX`, Redisson)
- **Security in Microservices**
  - JWT + OAuth2 (Authorization Server, Resource Server)
  - API Gateway-level auth
  - mTLS (Mutual TLS) for service-to-service
- **Configuration Management**
  - Spring Cloud Config Server
  - Centralized vs per-service config
- **Distributed Tracing**
  - Zipkin, Jaeger, OpenTelemetry
  - Correlation IDs, trace/span IDs
- **Idempotency** — ensure exactly-once processing
- **Rate Limiting & Throttling** — token bucket, sliding window

---

## 📨 [21. Apache Kafka & Messaging](21_apache_kafka_and_messaging.md)

### Apache Kafka

- **Architecture**
  - Broker, Topic, Partition, Offset, Producer, Consumer, Consumer Group
  - Replication Factor and ISR (In-Sync Replicas)
  - Zookeeper vs KRaft (Kafka Raft — modern mode)
- **Producer**
  - `KafkaProducer`, `ProducerRecord`
  - Acks — `0` (fire-and-forget), `1` (leader), `all` (all ISR)
  - Idempotent producer
- **Consumer**
  - `KafkaConsumer`, `@KafkaListener` in Spring Boot
  - Consumer groups — partition assignment
  - Offset management — auto commit vs manual commit
  - Rebalancing — what happens to offsets
- **Delivery Semantics**
  - At-most-once — message may be lost
  - At-least-once — message may duplicate
  - Exactly-once — idempotent + transactional
- **Dead Letter Queue (DLQ)** — handling poison messages
- **Kafka Streams** — real-time stream processing
- **Schema Registry + Avro** — schema evolution
- **Kafka Lag** — difference between produced and consumed offsets
- **Retention Policy** — time-based or size-based
- **Spring Boot Kafka Integration**
  - `spring-kafka`, `spring.kafka.bootstrap-servers`
  - `@KafkaListener`, `KafkaTemplate`
  - Error handling, retry, DLQ configuration

### RabbitMQ vs Kafka

| Aspect | RabbitMQ | Kafka |
|---|---|---|
| Role | Message Broker | Event Streaming Platform |
| Storage | Temporary | Persistent (retention-based) |
| Replay | Limited | Native (replay anytime) |
| Throughput | Medium | Extremely High |
| Routing | Strong (Exchanges) | Simple (Topics + Partitions) |
| Consumer Model | Push-based | Pull-based |
| Best For | Task queues, workflows | Streaming, analytics, event sourcing |

### Other Messaging
- **JMS** (Java Message Service) — `ActiveMQ`
- **RabbitMQ** — Exchanges (direct, topic, fanout), Queues, AMQP

---

## 🔭 [22. Observability & Monitoring](22_observability_and_monitoring.md)

- **Logging**
  - SLF4J + Logback / Log4j2
  - Structured logging — JSON format
  - Log levels — TRACE, DEBUG, INFO, WARN, ERROR
  - Async logging — don't block request threads
  - MDC (Mapped Diagnostic Context) — correlation IDs per thread
- **Metrics**
  - Micrometer — metrics facade for Spring Boot
  - **Prometheus** — pull-based metrics collection
  - **Grafana** — dashboards and alerting
  - Key metrics: JVM heap, GC pauses, thread count, HTTP request latency, error rate
- **Distributed Tracing**
  - OpenTelemetry (vendor-neutral)
  - Zipkin, Jaeger — trace visualization
  - Trace ID + Span ID propagation across services
- **Log Aggregation**
  - ELK Stack — Elasticsearch + Logstash + Kibana
  - EFK Stack — Elasticsearch + Fluentd + Kibana
- **Health Checks**
  - Spring Boot Actuator — `/health`, `/metrics`, `/info`, `/env`
  - Kubernetes Liveness & Readiness Probes
- **APM Tools** — Dynatrace, New Relic, Datadog, Splunk
- **Code Quality**
  - SonarQube — static analysis, coverage, code smells
  - PMD, Checkstyle, SpotBugs

---

## 🏗️ [23. System Design (HLD)](23_system_design_hld.md)

- **Core Concepts**
  - Horizontal vs Vertical Scaling
  - Load Balancing — round-robin, least connections, consistent hashing
  - CDN — static asset distribution
  - **Caching** — Cache-Aside, Write-Through, Write-Behind, Read-Through
  - Message Queues — decouple producers and consumers
  - **API Gateway** — single entry point, routing, auth, rate limiting
  - **Circuit Breaker** — prevent cascading failures
  - Service Discovery — dynamic service location
- **Database Design for Scale**
  - Sharding (horizontal partitioning) — shard key selection
  - Partitioning — range, hash, list
  - Read replicas — scale reads
  - Consistent Hashing — minimize resharding on node change
  - Rate Limiting design — token bucket, sliding window log
- **CAP Theorem** — tradeoffs in distributed systems
- **Design Principles**
  - Idempotency — safe to retry
  - Exactly-once processing
  - Backpressure — producer vs consumer speed mismatch
  - Graceful degradation
- **Common HLD Interview Problems**
  - URL Shortener (TinyURL)
  - Notification System (email/SMS/push at scale)
  - Chat Application (WhatsApp-like)
  - Payment Processing System
  - Rate Limiter
  - Distributed Job Scheduler
  - Real-time Analytics Platform
  - API Gateway design

---

## 🏆 [24. Competitive Programming & DSA in Java](24_dsa_and_competitive_programming.md)

- **Patterns for Problem Solving**
  - Two Pointers — sorted arrays, palindrome
  - Sliding Window — subarray/substring problems
  - Fast & Slow Pointer — linked list cycle detection
  - Binary Search — `O(log n)` search on sorted data
  - Backtracking — combinations, permutations
  - BFS / DFS — trees and graphs
  - Dynamic Programming — memoization, tabulation
  - Heap — Top K problems
  - Trie — string search / prefix matching
- **Data Structures**
  - Arrays, Strings, Linked Lists (single, double, circular)
  - Stacks and Queues
  - Trees (BST, AVL, Red-Black), Heaps
  - Graphs — adjacency list/matrix, BFS, DFS, Dijkstra, Topological Sort
- **Common Interview Problems**
  - Two Sum, Three Sum
  - Reverse a linked list (iterative + recursive)
  - Balanced parentheses
  - Infix to Postfix
  - LRU Cache (`LinkedHashMap`)
  - Binary search variants
  - Anagram check using Streams
- DSA with Java 8 — Streams for solving coding problems
- **Common Coding Patterns**
  - Palindrome check — reverse and compare, or two-pointer
  - Anagram check — sort both strings or `HashMap` character frequency
  - First non-repeating character — `LinkedHashMap` for insertion-order frequency
  - String compression — count consecutive chars
  - Balanced parentheses — Stack-based validation
  - Word frequency count — `Collectors.groupingBy()`
  - Fibonacci — iterative, recursive, memoized, stream-based
  - Prime check — trial division up to `√n`
  - Armstrong number — sum of each digit raised to power of digit count
  - GCD / LCM — Euclidean algorithm
  - Missing number — XOR trick or sum formula `n*(n+1)/2 - sum`
  - Sliding window max sum — `O(n)` single-pass

---

## 🗓️ [25. Agile, Scrum & Project Management](25_agile_scrum_project_management.md)

- **Agile Manifesto** (4 values — left side valued MORE, right side still matters)
  - Individuals & interactions > processes & tools
  - Working software > comprehensive documentation
  - Customer collaboration > contract negotiation
  - Responding to change > following a plan
- **Scrum Framework**
  - **Roles**: Product Owner (owns backlog, voice of customer), Scrum Master (facilitator, removes impediments), Dev Team (self-organising, 3-9 members)
  - **Artefacts**: Product Backlog, Sprint Backlog, Increment (must meet Definition of Done)
  - **Sprint** — fixed time-box 1-4 weeks, delivers potentially shippable increment
  - **Ceremonies**
    - Sprint Planning (2-4 hrs) — select backlog items, plan sprint
    - Daily Scrum (15 mins) — what did I do / will do / blockers?
    - Sprint Review (1-2 hrs) — demo increment, stakeholder feedback
    - Sprint Retrospective (1-2 hrs) — what went well, what to improve
- **Scrum vs Kanban**

  | Feature | Scrum | Kanban |
  |---|---|---|
  | Cadence | Fixed sprints (1-4 wks) | Continuous flow |
  | Roles | PO, SM, Dev Team | No prescribed roles |
  | WIP Limits | Implicit (sprint capacity) | Explicit WIP limits |
  | Change | Discouraged mid-sprint | Welcome anytime |
  | Best For | Complex product iterations | Ongoing support/maintenance |

- **Tools** — Jira (Epic → Story → Task → Bug, Scrum/Kanban boards), Confluence (wiki/runbooks), Trello (simple Kanban)
- **Waterfall vs Agile** — linear/single-delivery vs iterative/frequent-delivery; Agile surfaces risk early

---

## 🧭 [26. Interview Preparation Strategy](26_interview_preparation_strategy.md)

- **3-Month Preparation Plan**
  - **Month 1 — Core DSA Foundations**
    - Arrays, Strings, Recursion, Sorting, Searching
    - Solve LeetCode Easy → Medium (quality over quantity)
    - Understand time/space complexity for every solution
  - **Month 2 — System Design & Advanced Topics**
    - System design basics: requirements → capacity estimation → API design → DB → scale
    - LLD problems: Parking Lot, Elevator, ATM, Library
    - HLD concepts: DB, Distributed Systems, Hashing, Load Balancer, Performance
  - **Month 3 — Mock Interviews & Refinement**
    - Timed mock interviews — no hints, explain thought process out loud
    - Review company-specific previously asked questions
    - Start applying at 70% ready — you'll never feel 100%
- **10 Must-Master Skills for 2026**

  | Skill | What to Learn |
  |---|---|
  | System Design | APIs, DBs, caching, scalability, distributed systems |
  | Java 21/25 | Virtual threads, records, sealed classes, pattern matching |
  | Spring Boot 4 | Framework 7, enterprise-grade production patterns |
  | DevOps Basics | Docker, Kubernetes, CI/CD, monitoring |
  | Advanced Git | Rebase, cherry-pick, bisect, branching strategies |
  | REST + GraphQL | Design and secure APIs, versioning |
  | Testing Mastery | JUnit 5, Mockito, Testcontainers, mutation testing |
  | Microservices | Spring Cloud, resilience patterns, distributed tracing |
  | Event-Driven | Kafka/RabbitMQ, event sourcing, CQRS |
  | AI/LLM Integration | Spring AI, LangChain4j — next competitive edge |

- **Phase-Based Job Cracking Roadmap**
  - **Phase 1 (Weeks 1-6)**: Build foundations in DSA (Arrays, Strings, LL, Stacks, Queues), CS fundamentals (OS, DBMS, Networks, OOP)
  - **Phase 2 (Weeks 7-14)**: Master coding patterns (DP, Graphs, Greedy, Binary Search); time-bound mock practice (30 min Medium, 45 min Hard)
  - **Phase 3 (Weeks 15+)**: Build 2-3 production-quality projects (e-commerce with JWT + Redis + Kafka, social media with WebSockets + S3, system design demo)
- **Spring Boot Annotations Quick Reference**

  | Annotation | Purpose |
  |---|---|
  | `@SpringBootApplication` | `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan` |
  | `@RestController` | `@Controller` + `@ResponseBody` — returns JSON directly |
  | `@Service` | Business logic layer |
  | `@Repository` | Data access layer — wraps persistence exceptions |
  | `@Transactional` | AOP-managed DB transaction — rollback on RuntimeException |
  | `@Cacheable` | Cache result on first call; skip DB on repeat |
  | `@CacheEvict` | Remove stale cache entry |
  | `@Async` | Run method in background thread; returns `void`/`CompletableFuture` |
  | `@Scheduled` | Cron/fixedRate/fixedDelay — requires `@EnableScheduling` |
  | `@Profile` | Activate bean only in specific environment |
  | `@ConditionalOnProperty` | Conditionally create bean based on config property |
  | `@WebMvcTest` | Test controller layer only (no DB) |
  | `@DataJpaTest` | Test JPA layer with in-memory H2 |
  | `@SpringBootTest` | Full application context integration test |

---

## 💻 [27. Coding Programs & Interview Examples](27_coding_programs_and_examples.md)

> Hands-on code problems asked in real Java backend interviews. Organized by topic.

### 🔷 A. Java 8 Streams — Most Asked Programs

#### 1. Find duplicate elements in a list
```java
List<Integer> nums = List.of(1, 2, 3, 2, 4, 3, 5);
Set<Integer> seen = new HashSet<>();
List<Integer> duplicates = nums.stream()
    .filter(n -> !seen.add(n))
    .distinct()
    .collect(Collectors.toList());
// Output: [2, 3]
```

#### 2. Find the second highest number
```java
Optional<Integer> second = nums.stream()
    .distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1)
    .findFirst();
```

#### 3. First non-repeating character in a string
```java
String input = "swiss";
Character result = input.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
    .entrySet().stream()
    .filter(e -> e.getValue() == 1)
    .map(Map.Entry::getKey)
    .findFirst()
    .orElse(null);
// Output: 'w'
```

#### 4. Count character frequency in a string
```java
String s = "hello world";
Map<Character, Long> freq = s.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
```

#### 5. Group employees by department & find max salary per dept
```java
Map<String, Optional<Employee>> maxByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment,
             Collectors.maxBy(Comparator.comparingDouble(Employee::getSalary))));

// Average salary per department
Map<String, Double> avgByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment,
             Collectors.averagingDouble(Employee::getSalary)));

// Count per department
Map<String, Long> countByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
```

#### 6. Sort employees: first by name, then by marks descending
```java
employees.stream()
    .sorted(Comparator.comparing(Employee::getName)
        .thenComparing(Comparator.comparingDouble(Employee::getSalary).reversed()))
    .collect(Collectors.toList());
```

#### 7. Reverse words in a sentence
```java
String sentence = "My name is Tom";
String reversed = Arrays.stream(sentence.split(" "))
    .collect(Collectors.collectingAndThen(Collectors.toList(), list -> {
        Collections.reverse(list);
        return String.join(" ", list);
    }));
// Output: "Tom is name My"
```

#### 8. Fibonacci using Stream.iterate (Java 8)
```java
Stream.iterate(new long[]{0, 1}, f -> new long[]{f[1], f[0] + f[1]})
    .limit(10)
    .map(f -> f[0])
    .forEach(System.out::println);
// Output: 0 1 1 2 3 5 8 13 21 34
```

#### 9. Flatten a list of lists
```java
List<List<Integer>> nested = List.of(List.of(1, 2), List.of(3, 4), List.of(5));
List<Integer> flat = nested.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());
```

#### 10. Partition numbers into even and odd
```java
Map<Boolean, List<Integer>> partitioned = nums.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// true  → [2, 4]   false → [1, 3, 5]
```

---

### 🔷 B. String Programs

#### 11. Palindrome check — recursive
```java
public boolean isPalindrome(String s, int left, int right) {
    if (left >= right) return true;
    if (s.charAt(left) != s.charAt(right)) return false;
    return isPalindrome(s, left + 1, right - 1);
}
// Call: isPalindrome("racecar", 0, s.length() - 1) → true
```

#### 12. Anagram check
```java
public boolean isAnagram(String a, String b) {
    char[] ca = a.toCharArray(); char[] cb = b.toCharArray();
    Arrays.sort(ca); Arrays.sort(cb);
    return Arrays.equals(ca, cb);
}
// HashMap approach: O(n) time, O(1) space (limited alphabet)
```

#### 13. Count character occurrences
```java
Map<Character, Integer> map = new LinkedHashMap<>();
for (char c : "hello world".toCharArray())
    map.merge(c, 1, Integer::sum);
// Output: h=1, e=1, l=3, o=2, ' '=1, w=1, r=1, d=1
```

#### 14. String compression ("aaabbc" → "a3b2c1")
```java
public String compress(String s) {
    StringBuilder sb = new StringBuilder();
    int i = 0;
    while (i < s.length()) {
        char c = s.charAt(i); int count = 0;
        while (i < s.length() && s.charAt(i) == c) { i++; count++; }
        sb.append(c).append(count);
    }
    return sb.toString();
}
```

#### 15. Balanced parentheses
```java
public boolean isBalanced(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if ("({[".indexOf(c) >= 0) stack.push(c);
        else {
            if (stack.isEmpty()) return false;
            char top = stack.pop();
            if (c == ')' && top != '(') return false;
            if (c == '}' && top != '{') return false;
            if (c == ']' && top != '[') return false;
        }
    }
    return stack.isEmpty();
}
```

---

### 🔷 C. Collections & Data Structures

#### 16. LRU Cache using LinkedHashMap
```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    LRUCache(int capacity) {
        super(capacity, 0.75f, true); // accessOrder = true
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}
```

#### 17. Remove duplicates from a list (preserve order)
```java
List<Integer> unique = new ArrayList<>(new LinkedHashSet<>(list));
// Or with streams:
List<Integer> unique2 = list.stream().distinct().collect(Collectors.toList());
```

#### 18. Sort a Map by value
```java
Map<String, Integer> sorted = map.entrySet().stream()
    .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
    .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
             (e1, e2) -> e1, LinkedHashMap::new));
```

#### 19. Find common elements between two lists
```java
List<Integer> common = list1.stream()
    .filter(new HashSet<>(list2)::contains)
    .collect(Collectors.toList());
```

#### 20. Comparable vs Comparator
```java
// Comparable — natural order INSIDE the class
class Person implements Comparable<Person> {
    public int compareTo(Person o) { return this.age - o.age; }
}

// Comparator — external/multiple sort orders
list.sort(Comparator.comparing(Person::getName)
    .thenComparing(Comparator.comparingInt(Person::getAge).reversed()));
```

---

### 🔷 D. DSA Classics

#### 21. Two Sum — O(n) with HashMap
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>(); // value → index
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement))
            return new int[]{map.get(complement), i};
        map.put(nums[i], i);
    }
    return new int[]{};
}
// Time: O(n) | Space: O(n)
```

#### 22. Three Sum — O(n²) with sort + two pointers
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) { result.add(List.of(nums[i], nums[left++], nums[right--])); }
            else if (sum < 0) left++;
            else right--;
        }
    }
    return result;
}
```

#### 23. Binary Search
```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2; // avoids overflow
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // not found
}
```

#### 24. Find missing number (XOR trick)
```java
public int missingNumber(int[] nums) {
    int xor = nums.length;
    for (int i = 0; i < nums.length; i++)
        xor ^= i ^ nums[i];
    return xor;
}
// Alternative: n*(n+1)/2 - Arrays.stream(nums).sum()
```

#### 25. Sliding window — maximum subarray sum of size k
```java
public int maxSum(int[] arr, int k) {
    int windowSum = 0, maxSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    maxSum = windowSum;
    for (int i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

---

### 🔷 E. Concurrency Programs

#### 26. Deadlock — example and fix
```java
// DEADLOCK: Thread1 locks A→B, Thread2 locks B→A
synchronized(lockA) { synchronized(lockB) { /* Thread 1 */ } }
synchronized(lockB) { synchronized(lockA) { /* Thread 2 */ } }

// FIX: Always acquire locks in the SAME order
synchronized(lockA) { synchronized(lockB) { /* both threads */ } }

// Or use tryLock with timeout (no indefinite blocking)
if (lockA.tryLock(50, MILLISECONDS) && lockB.tryLock(50, MILLISECONDS)) {
    try { doWork(); } finally { lockA.unlock(); lockB.unlock(); }
}
```

#### 27. ThreadLocal — proper usage with cleanup
```java
static ThreadLocal<MyObject> tl = new ThreadLocal<>();

// BAD: no cleanup → memory leak in thread pools
tl.set(new MyObject()); doWork();

// GOOD: always remove in finally
try {
    tl.set(new MyObject());
    doWork();
} finally {
    tl.remove(); // critical — prevents memory leak
}
```

#### 28. Virtual Threads (Java 21) — 1 million tasks
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 1_000_000).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1)); // blocks cheaply
            return i;
        })
    );
} // 1 million virtual threads, NOT 1 million OS threads
```

---

### 🔷 F. Spring Boot REST API Programs

#### 29. REST controller — GET by ID and search by name
```java
@RestController
@RequestMapping("/api/persons")
public class PersonController {
    @Autowired private PersonRepository repo;

    @GetMapping("/{id}")
    public ResponseEntity<Person> getById(@PathVariable Long id) {
        return repo.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/search")
    public List<Person> getByName(@RequestParam String name) {
        return repo.findByNameContainingIgnoreCase(name);
    }
}
```

#### 30. Immutable class using Java 16+ Record
```java
public record Employee(String name, List<String> roles) {
    public Employee {
        if (name == null || name.isBlank())
            throw new IllegalArgumentException("Name required");
        roles = List.copyOf(roles); // defensive copy — immutable
    }
}
// Usage:
Employee e = new Employee("Alice", List.of("Dev", "Lead"));
e.roles().add("PM"); // throws UnsupportedOperationException ✅
```

#### 31. Factory Pattern with switch expression (Java 17+)
```java
class ShapeFactory {
    public Shape get(String type) {
        return switch (type) {
            case "CIRCLE"   -> new Circle();
            case "RECTANGLE"-> new Rectangle();
            default         -> throw new IllegalArgumentException("Unknown: " + type);
        };
    }
}
```

---

### 🔷 G. Golden Rules for Coding Problems

---

#### 🏆 G1. DSA Pattern Recognition — 10 Rules

> Hear the problem → recognize the pattern → pick the right tool. Every time.

| # | If the problem says... | Use this |
|---|---|---|
| 1 | Top / min / max **K elements** among N | **Heap** (`PriorityQueue`) |
| 2 | Input is **sorted** (array or list) | **Binary Search** or **Two Pointers** |
| 3 | Need **all combinations** or **permutations** | **Backtracking** or **BFS** |
| 4 | **Tree** or **Graph** traversal | **BFS** (level-order) or **DFS** (depth-first) |
| 5 | Recursive solution exists | Convert to iterative using a **Stack** |
| 6 | O(n²) brute force exists | Look for **HashMap** O(n)/O(n) or **sorting** O(n log n)/O(1) |
| 7 | **Maximize or minimize** something | **Dynamic Programming** (memoization / tabulation) |
| 8 | Find **common substring** across strings | **HashMap** or **Trie** |
| 9 | **Search or manipulate** a set of strings | **Trie** is the best structure |
| 10 | LinkedList, **no extra space** allowed | **Fast & Slow Pointer** approach |

---

#### ⚡ G2. Java Streams — Golden Rules

| # | Rule | Reason |
|---|---|---|
| 1 | **Never modify the source** inside a stream | Causes `ConcurrentModificationException` |
| 2 | Use `.distinct()` before `.sorted()`  | Saves sorting duplicates — cheaper |
| 3 | Use `filter()` as early as possible | Reduces elements flowing through pipeline |
| 4 | Prefer `.findFirst()` over `.collect().get(0)` | Short-circuits — stops at first match |
| 5 | Use `mapToInt/mapToDouble` for numeric ops | Avoids boxing overhead of `map()` |
| 6 | **Never use** `parallelStream()` with shared mutable state | Race conditions — use `ConcurrentHashMap` instead |
| 7 | Use `Collectors.groupingBy()` for any group-by problem | Replaces nested loops + maps |
| 8 | Use `Collectors.joining()` for string joining | Much faster than `+` concatenation in loops |
| 9 | `flatMap()` = map + flatten | Use when each element maps to a collection |
| 10 | Chain `Comparator.comparing().thenComparing()` | Multi-field sorting with no `if-else` |
| 11 | `Stream.iterate()` for infinite/generated sequences | Fibonacci, number ranges, sequences |
| 12 | Use `collectors.collectingAndThen()` to post-process | E.g., reverse a list after collecting |
| 13 | Use `Optional.map().orElse()` — **never** `.get()` without check | `.get()` on empty Optional throws exception |
| 14 | `peek()` is for debugging only — never business logic | Terminal ops may not run on all elements |
| 15 | `reduce(identity, accumulator)` for fold operations | Sum, product, max without boxing |

---

#### 🔤 G3. String Problems — Golden Rules

| # | Rule | Example / Hint |
|---|---|---|
| 1 | Use `StringBuilder` for building strings in loops | `String +` in loop = O(n²), `StringBuilder` = O(n) |
| 2 | Anagram check → sort both, or use `int[26]` freq array | `Arrays.sort(a) == Arrays.sort(b)` |
| 3 | Palindrome → **two pointers** (left, right converging) | Avoids creating a reversed copy |
| 4 | First non-repeating → `LinkedHashMap` (insertion-order + count) | Preserves order while counting |
| 5 | Duplicate characters → `HashSet.add()` returns `false` if duplicate | `if (!seen.add(c)) duplicates.add(c)` |
| 6 | Substring search → use `String.contains()` or `indexOf()` | Don't write KMP for interviews unless asked |
| 7 | Word frequency → `Map.merge(word, 1, Integer::sum)` | Cleaner than `getOrDefault + put` |
| 8 | Reverse words → `split(" ")` + reverse array + `String.join` | Or use `Deque` as a stack |
| 9 | Remove duplicate chars preserving order → `LinkedHashSet` | `new LinkedHashSet<>(Arrays.asList(chars))` |
| 10 | char↔int conversion → `(char) c` and `c - 'a'` for indexing | `'a'` = 97; use for freq array indexing |
| 11 | **Never** compare Strings with `==` — always `.equals()` | `==` checks reference, not content |
| 12 | `s.chars()` returns `IntStream` — cast to `(char)` for Stream ops | `s.chars().mapToObj(c -> (char) c)` |

---

#### 📦 G4. Collections — Golden Rules

| # | Rule | Why |
|---|---|---|
| 1 | **HashMap** for O(1) lookup, **TreeMap** for sorted order | Don't use TreeMap when order doesn't matter — 5× slower |
| 2 | **LinkedHashMap** when you need insertion order + O(1) | Foundation for LRU Cache |
| 3 | **HashSet** to track seen elements in O(1) | Replaces nested loops for duplicates |
| 4 | `computeIfAbsent(key, k -> new ArrayList<>())` for grouping | Cleaner than `getOrDefault + put` |
| 5 | `Map.merge(key, 1, Integer::sum)` for counting | Replaces 3-line `getOrDefault` pattern |
| 6 | Use **`Deque`** (`ArrayDeque`) instead of `Stack` | `Stack` is legacy + synchronized |
| 7 | Fail-fast iterators → never `list.remove()` inside `for-each` | Use `Iterator.remove()` or `removeIf()` |
| 8 | `Collections.unmodifiableList()` vs `List.of()` | `List.of()` throws on add/set, `unmodifiable` wraps existing |
| 9 | **`ConcurrentHashMap`** for multi-threaded maps | `HashMap` is not thread-safe; `Hashtable` is deprecated |
| 10 | **`CopyOnWriteArrayList`** for read-heavy, write-rare concurrent lists | Safe iteration; writes create a full copy |
| 11 | `PriorityQueue` default = min-heap; reverse for max-heap | `new PriorityQueue<>(Comparator.reverseOrder())` |
| 12 | `equals()` + `hashCode()` must be consistent for Map keys | If `equals()` is overridden, override `hashCode()` too |

---

#### 🔀 G5. Concurrency — Golden Rules

| # | Rule | Why |
|---|---|---|
| 1 | **Prefer `ReentrantLock` over `synchronized`** for complex locking | Supports `tryLock`, `lockInterruptibly`, fairness |
| 2 | **Always** call `ThreadLocal.remove()` in `finally` | Thread pools reuse threads → stale data leak |
| 3 | **`volatile`** = visibility only, NOT atomicity | Use `AtomicInteger` for atomic increments |
| 4 | **Lock ordering** prevents deadlock | Always acquire `lockA` before `lockB` in all threads |
| 5 | Use `ConcurrentHashMap` — never `Collections.synchronizedMap()` | `synchronizedMap` locks entire map; CHM is segment-locked |
| 6 | Use **`CompletableFuture`** for async pipelines | Avoid raw `Thread` or legacy `Future.get()` blocking |
| 7 | `parallelStream()` uses **ForkJoinPool** (shared) | Can starve other tasks; use custom pool for isolation |
| 8 | **Virtual Threads** (Java 21) — never use `synchronized` inside | Pins the carrier thread; use `ReentrantLock` instead |
| 9 | `CountDownLatch` = wait for N events (one-time); `CyclicBarrier` = N threads meet repeatedly | Choose based on reuse need |
| 10 | Design stateless services whenever possible | No shared state = no concurrency bugs |

---

#### 🗄️ G6. SQL Interview — Golden Rules

| # | Rule | Hint |
|---|---|---|
| 1 | **Nth highest salary** → `DENSE_RANK()` or subquery with `LIMIT OFFSET` | `DENSE_RANK() OVER (ORDER BY salary DESC) = N` |
| 2 | **Duplicates** → `GROUP BY + HAVING COUNT(*) > 1` | Never `DISTINCT` to find duplicates |
| 3 | **Find employees with no manager** → `LEFT JOIN + IS NULL` | Or `NOT IN (SELECT manager_id ...)` |
| 4 | **Running total / cumulative sum** → `SUM() OVER (ORDER BY ...)` | Window function, not grouped |
| 5 | **Rank with gaps** → `RANK()`; **no gaps** → `DENSE_RANK()` | `ROW_NUMBER()` = always unique |
| 6 | **Delete duplicates, keep one** → `DELETE WHERE id NOT IN (SELECT MIN(id) GROUP BY ...)` | Use CTE for clarity |
| 7 | **Self join** for hierarchical data | `e1 JOIN e2 ON e1.manager_id = e2.id` |
| 8 | `WHERE` filters **rows**; `HAVING` filters **groups** | `HAVING` runs after `GROUP BY` |
| 9 | **Index** on columns used in `WHERE`, `JOIN`, `ORDER BY` | Never index low-cardinality columns (like boolean) |
| 10 | `EXPLAIN` / `EXPLAIN ANALYZE` before optimizing | See the query plan — find seq scans to fix |



### 🔷 H. Top 50 Coding Programs — Quick Reference List (Java 8+)

> Practice these in order. All solvable with Streams + Collections.

| # | Problem | Key API/Pattern |
|---|---|---|
| 1 | Find duplicates in a list | `filter(!seen.add(n))` |
| 2 | Remove duplicates | `.distinct()` or `LinkedHashSet` |
| 3 | First non-repeating character | `groupingBy` + `LinkedHashMap` + `counting()` |
| 4 | Frequency of each character | `chars().mapToObj().groupingBy()` |
| 5 | Reverse a string | `new StringBuilder(s).reverse()` |
| 6 | Sort list of integers | `.sorted()` |
| 7 | Sort employees by salary | `Comparator.comparingDouble()` |
| 8 | Second highest number | `.distinct().sorted(reversed).skip(1).findFirst()` |
| 9 | Filter even numbers | `.filter(n -> n % 2 == 0)` |
| 10 | Filter odd numbers | `.filter(n -> n % 2 != 0)` |
| 11 | Convert list to uppercase | `.map(String::toUpperCase)` |
| 12 | Flatten list of lists | `.flatMap(Collection::stream)` |
| 13 | Join strings with delimiter | `Collectors.joining(", ")` |
| 14 | Find longest string | `.max(Comparator.comparingInt(String::length))` |
| 15 | Group by department | `Collectors.groupingBy(Employee::getDept)` |
| 16 | Count per department | `groupingBy + counting()` |
| 17 | Max salary per department | `groupingBy + maxBy()` |
| 18 | Avg salary per department | `groupingBy + averagingDouble()` |
| 19 | Partition even/odd | `Collectors.partitioningBy(n -> n % 2 == 0)` |
| 20 | Top 3 earners | `.sorted(reversed).limit(3)` |
| 21 | Calculate sum | `.mapToInt(i -> i).sum()` or `reduce(0, Integer::sum)` |
| 22 | Check contains duplicates | `stream().count() != distinct().count()` |
| 23 | Find common elements | `.filter(new HashSet<>(list2)::contains)` |
| 24 | Convert list to map | `Collectors.toMap(key, value)` |
| 25 | Sort map by value | `.sorted(Map.Entry.comparingByValue())` |
| 26 | Filter nulls | `.filter(Objects::nonNull)` |
| 27 | Count words in sentence | `s.trim().split("\\s+").length` |
| 28 | Reverse words in sentence | `Stream.of(split).collect + Collections.reverse` |
| 29 | Group strings by length | `groupingBy(String::length)` |
| 30 | Merge two lists | `Stream.concat(l1.stream(), l2.stream())` |
| 31 | Find missing number | XOR trick or `n*(n+1)/2 - sum` |
| 32 | Two Sum | `HashMap<value, index>` — O(n) |
| 33 | Binary Search | Left/right pointers — O(log n) |
| 34 | Palindrome check | Two-pointer or recursive |
| 35 | Anagram check | `Arrays.sort` both or `HashMap` frequency |
| 36 | Balanced parentheses | Stack-based |
| 37 | LRU Cache | `LinkedHashMap(capacity, 0.75f, true)` |
| 38 | Fibonacci (Stream) | `Stream.iterate(new long[]{0,1}, ...)` |
| 39 | Sliding window max sum | Single-pass O(n) |
| 40 | String compression | Pointer-based counter |
| 41 | Deadlock example + fix | Lock ordering / `tryLock` |
| 42 | Thread-safe Singleton | `volatile` + double-checked locking or Enum |
| 43 | Immutable class | `final` class + `final` fields + `List.copyOf()` |
| 44 | Custom Comparator chaining | `comparing().thenComparing()` |
| 45 | Parallel stream pitfall | Shared mutable state → `ConcurrentHashMap` |
| 46 | `Optional` chaining | `ofNullable().map().orElse()` |
| 47 | `CompletableFuture` chain | `supplyAsync().thenApply().exceptionally()` |
| 48 | Virtual Threads (Java 21) | `Executors.newVirtualThreadPerTaskExecutor()` |
| 49 | Record as DTO | `record UserDTO(String name, String email) {}` |
| 50 | Spring Boot REST GET+SEARCH | `@GetMapping + ResponseEntity + @RequestParam` |

---

## 📈 [28. Time and Space Complexity in Java](28_complexity_analysis.md)

- Introduction to Big O notation — growth rate vs speed (Good vs Bad)
- **Time Complexity** — $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$
- **Space Complexity** — Heap vs Stack memory, Object Overhead
- Complexity of Java Collections (`ArrayList`, `HashMap`, etc.)
- Complexity of Sorting and Searching (`Arrays.sort`, `binarySearch`)
- **Amortized Analysis** — `ArrayList.add()` mechanics
- Production scenarios — hidden $O(n^2)$ and `Memory Leak` patterns

---

## 📚 [29. Java Learning Resources](29_learning_resources.md)

| Type | Resource |
|---|---|
| 📖 Books | *Effective Java* by Joshua Bloch |
| 📖 Books | *Java: The Complete Reference* by Herbert Schildt |
| 📖 Books | *Clean Code* by Robert C. Martin |
| 📖 Books | *Designing Data-Intensive Applications* by Martin Kleppmann |
| 🌐 Online | [Oracle Java Docs](https://docs.oracle.com/en/java/) |
| 🌐 Online | [Spring Docs](https://docs.spring.io/spring-boot/docs/current/reference/html/) |
| 🌐 Online | [Neetcode.io](https://neetcode.io) — 150 curated LeetCode patterns |
| 🎓 Courses | Udemy — Java Masterclass, Spring Boot Microservices |
| 🎓 Courses | CS50 Harvard (OS/Networks theory) |
| 💻 Practice | [LeetCode](https://leetcode.com) — DSA problems |
| 💻 Practice | [HackerRank Java](https://hackerrank.com/domains/java) |
| 💻 Practice | [InterviewBit](https://interviewbit.com) — structured mock assessments |
| 🛠️ Tools | IntelliJ IDEA, Postman, DBeaver, Docker Desktop, VisualVM/Eclipse MAT |

---

> **Tip:** Work through this roadmap in order. Sections 1–7 are the foundation. Sections 8–15 are the interview core. Sections 16–21 are what separate **senior engineers** from the rest.
