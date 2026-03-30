<!-- Part of Java Learning Roadmap — Section 9 -->

# 🎨 9. Design Patterns

---

### 1.1 The Architect's Blueprint (Creational, Structural, Behavioral)

**Core Idea:**
Design Patterns are "Proven recipes for software architecture." They aren't code you Copy-Paste; they are templates you adapt to solve a specific problem (like object creation or communication).

**Why it matters:**
Patterns provide a **Common Language**. When an architect says "We should use an Adapter here," every developer instantly knows the goal is to bridge two incompatible systems without reading a single line of code.

**When to use:**
*   To decouple your code so that changing one part doesn't break everything else.
*   When your business logic becomes a "Spaghetti" of `if/else` statements.
*   When you need to optimize object creation (Singletons) or intercept method calls (Proxies).

**When NOT to use:**
*   **"Design Pattern Fever":** Don't force a pattern where a simple function would work. Patterns add classes and complexity.
*   When the problem is trivial. Over-engineering with patterns (using a Factory for a simple `new User()`) is a major anti-pattern.

**Example (Spring Boot):**
Every time you use `@Service`, you are using the **Singleton** pattern (managed by Spring). Every time you use `@Transactional`, you are using the **Proxy** pattern to wrap your database logic.

**Deep Dive:**
The "Gang of Four" (GoF) book categorized 23 patterns into three types:
1.  **Creational (Object Creation):** How do we make objects safely? (`Singleton`, `Factory`, `Builder`).
2.  **Structural (Object Composition):** How do we connect classes together? (`Adapter`, `Proxy`, `Facade`).
3.  **Behavioral (Object Communication):** How do objects talk to each other? (`Strategy`, `Observer`, `Template Method`).

**Advanced Insight:**
**Performance vs. Flexibility.** Most patterns trade **Speed** for **Maintenance**. A `Proxy` call is slightly slower than a direct call due to the extra layer, but it allows for "Magical" features like automatic logging, caching, and security checks.

**Pitfall:**
**The "Pattern-first" approach.** Developers often pick a pattern and then try to find a problem it solves. **Always start with the problem.** If your code starts violating **SOLID** principles, $then$ look for a pattern to fix it.

**Production Tip:**
In modern Java, many patterns are built-in. `Builder` is almost always handled by **Lombok (`@Builder`)**. `Singleton` is handled by **Spring's Bean Container**. Don't write these manually unless you have a very specific reason.

**Interview Trap:**
"Is a Singleton a Design Pattern or an Anti-pattern?"
**Answer:** **Both.** It's a pattern for resource management (DbPool), but it becomes an anti-pattern when used as a "Global Variable Container" that's impossible to unit test and creates hidden dependencies.

---

## 2. Why It Exists

*   **Common Vocabulary:** Saying "I used a Strategy Pattern here" instantly explains your architecture to another engineer without them reading the code.
*   **Time Saving:** Instead of reinventing the wheel to solve a dependency issue, you use an industry-standard best practice.
*   **Maintainability:** By decoupling object creation from business logic (Factory), or decoupling algorithms from their executing context (Strategy), code becomes much easier to test and extend.

---

## 3. How It Works Internally

### 3.1 Singleton (The Shared Instance)

**Core Idea:**
Exactly ONE copy of a class for the entire application. Like a "One-Way Street" or a "Unique Database Connection."

**Why it matters:**
Some resources (like a Database Pool, a Configuration File reader, or a Log Manager) should only have one instance. Creating 10,000 DB connections would crash your server.

**When to use:**
*   Managing shared resources (Thread Pools, Caches).
*   Logging frameworks (`Logger`).
*   Spring Beans (by default, everything in Spring is a Singleton).

**When NOT to use:**
*   To pass data between screens or components (use Parameters/Context).
*   For stateful objects that change for every user (use Prototype or request scope).

**Example (Production API):**
A `TokenGenerator` class in a security service that needs a single cryptographic key to sign all JWTs.

**Deep Dive:**
The primary challenge is **Thread-Safety**.
*   **Double-Checked Locking:** Checks if the instance is null *before* and *after* a `synchronized` block. Requires the `volatile` keyword to prevent the JVM from seeing a "partially initialized" object.
*   **Enum Singleton:** The "pro" way. Java guarantees that only one enum instance exists, it's thread-safe, and it protects against Reflection-based attacks.

**Advanced Insight:**
**Object Header Physics.** A Singleton helps reduce the **Memory Footprint** and **GC Pressure** because you aren't constantly creating and destroying object headers and metadata in the Heap.

**Pitfall:**
**The Reflection Break.** You can use the Reflection API to find the private constructor and create a second instance of a Singleton. Only **Enum Singletons** are naturally immune to this hack.

**Production Tip:**
In a Spring app, never write your own Singleton code unless you are building a low-level library. Let Spring's `@Service` or `@Component` annotations handle the lifecycle for you.

**Interview Trap:**
"Why is `volatile` necessary in a double-checked singleton?"
**Answer:** Because without `volatile`, the CPU/JIT might reorder the constructor steps. Thread B might see a non-null instance variable *before* the constructor has finished setting its internal values, leading to a crash.

---

### 3.2 Strategy Pattern (Algorithm Swapping)

**Core Idea:**
"If you have a lot of `if/else` statements for different ways to do the same thing (like paying or sorting), move each `if` branch into its own class."

**Why it matters:**
It adheres to the **Open/Closed Principle**. You can add a new Payment Method (e.g., Apple Pay) just by creating one new class, without touching the existing "Checkout" logic.

**When to use:**
*   Multiple ways to process data (Compression: ZIP vs GZIP vs RAR).
*   Dynamic behavior based on user choice (Payment: CreditCard vs PayPal vs Bitcoin).
*   Validation logic that changes based on country or region.

**When NOT to use:**
*   When there are only 2 simple strategies that will never change. Just use an `if/else`.
*   When the "strategies" are very similar and don't share an interface.

**Example (Logistics):**
A shipping calculator that switches between `OceanShipping`, `AirShipping`, and `GroundShipping` based on the weight and destination provided at the checkout screen.

**Deep Dive:**
It involves a **Context** class that holds a reference to a **Strategy Interface**. At runtime, you "inject" the specific implementation into the context. This decouples the "How" (Algorithm) from the "When" (Business Logic).

**Advanced Insight:**
**Lambda Strategy.** In Java 8+, if your strategies are simple one-liners, you don't even need separate classes. You can pass a **Lambda Expression** as a strategy directly into your methods.

**Pitfall:**
**Over-abstraction.** If you have 50 different strategies for a simple string formatter, the code becomes harder to navigate. New developers will have to open 50 files to understand the system.

**Production Tip:**
Combine Strategy with a **Factory Pattern**. Use a Factory to *pick* the right strategy from a `Map` based on a request parameter, then use the Strategy to execute the work.

**Interview Trap:**
"How is Strategy different from State pattern?"
**Answer:** They look identical in code. The difference is **Intent**. Strategy is about *choosing an algorithm* via external input; State is about an object *changing its own behavior* based on its internal state transitions.

---

## 4. Code Examples

### 4.1 Thread-Safe Singleton
```java
public class DatabaseConnection {
    // volatile ensures memory visibility across threads
    private static volatile DatabaseConnection instance;

    // Private constructor prevents new DatabaseConnection()
    private DatabaseConnection() {}

    public static DatabaseConnection getInstance() {
        if (instance == null) { // 1st check (no locking, fast)
            synchronized (DatabaseConnection.class) { // Lock only on first creation
                if (instance == null) { // 2nd check (safe)
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
}
### 3.3 Factory Method & Abstract Factory

**Core Idea:**
A "Virtual Vending Machine." You tell it what you want (e.g., "SMS"), and it handles the complex process of making the object and giving it to you.

**Why it matters:**
Centralizes object creation. If the way you create a `DatabaseConnection` changes, you only change it in the **Factory**, not in 50 different classes.

**When to use:**
*   When a class cannot anticipate the class of objects it must create.
*   When you want to keep your business logic unaware of the concrete "Implementation" classes.

**When NOT to use:**
*   For simple objects like `new ArrayList<>()` or `new User()`.
*   When the creation logic never changes.

**Example (Spring Boot):**
`BeanFactory` or `ApplicationContext`. When you call `context.getBean(MyService.class)`, Spring acts as a massive Abstract Factory that finds, instantiates, and wires your service for you.

**Deep Dive:**
*   **Factory Method:** A single method that returns an object of an interface type based on input strings or enums.
*   **Abstract Factory:** A "Factory of Factories." It produces families of related objects (e.g., a "DarkThemeFactory" that produces dark buttons, dark text, and dark menus).

**Advanced Insight:**
**Static Factory Methods.** Java's internal libraries use this instead of constructors (e.g., `List.of()`, `Optional.of()`, `Integer.valueOf()`). This allows the JVM to return a cached instance or a subclass without you knowing.

**Pitfall:**
**The Switch Statement Smell.** A Factory often has a large `switch` statement. If you add 1,000 types, the switch becomes a maintenance nightmare. **Solution:** Use a `Map<String, Supplier<T>>` to register types dynamically.

**Production Tip:**
Use Factory patterns when integrating with **Third-party APIs**. If you have 3 different payment providers (Stripe, PayPal, Adyen), a `PaymentProviderFactory` ensures your core app logic never knows which one is actually being used.

**Interview Trap:**
"Can a Factory be a Static class?"
**Answer:** **Yes.** We call it a "Static Factory." It's common in Java for performance and readability, though a non-static Factory allows for better Mocking in unit tests using Mockito.
```

### 4.2 Factory Method (Java 17+)
```java
interface Notification { void notifyUser(); }
class EmailNotification implements Notification { public void notifyUser() { System.out.println("Email"); } }
class SMSNotification implements Notification { public void notifyUser() { System.out.println("SMS"); } }

// The Factory creates objects based on input, hiding the instantiation logic
public class NotificationFactory {
    public static Notification createNotification(String channel) {
        return switch (channel.toUpperCase()) {
            case "SMS" -> new SMSNotification();
            case "EMAIL" -> new EmailNotification();
            default -> throw new IllegalArgumentException("Unknown channel");
        };
    }
}
```

### 4.6 Adapter Pattern (Connecting Different Worlds)

**Core Idea:**
A "Travel Plug Converter." It allows an object designed for one interface to work with a system designed for a completely different one.

**Why it matters:**
You often use "Legacy" code or "Third-party" libraries that you cannot change. The Adapter lets you map their weird method names to your clean, internal system interface.

**When to use:**
*   Integrating a new API into an old system.
*   Wrapping a library so that your code doesn't depend directly on the library's specific method names.

**When NOT to use:**
*   When you have control over both pieces of code. In that case, just refactor the code to use a single interface!

**Example (Modern Java):**
`InputStreamReader`. It "adapts" a byte stream (raw file data) into a character stream (readable text), allowing a `BufferedReader` to read from it.

**Deep Dive:**
There are two types:
1.  **Class Adapter:** Uses inheritance (rarely used because it's tightly coupled).
2.  **Object Adapter:** Uses **Composition**. The Adapter holds a reference to the legacy object and maps calls to it.

**Advanced Insight:**
**Two-Way Adapters.** Sometimes you need an adapter to translate both ways. This requires the adapter to implement both the target and the source interfaces simultaneously.

**Pitfall:**
**The "Middleman" bloat.** If you have too many adapters, your code structure becomes a maze. If you find yourself writing adapters for your $own$ new code, you've designed the interfaces incorrectly.

**Production Tip:**
Use Adapters for **Data Mapping**. When your API receives a `UserDTO` from the frontend, an Adapter (often called a "Mapper" or "Assembler") converts it into a `UserEntity` for the Database.

**Interview Trap:**
"How is Adapter different from Facade?"
**Answer:** An `Adapter` changes an interface to **match another** (making things talk). A `Facade` **simplifies** a complex interface (making things easier to use).


### 4.7 Observer Pattern (The Foundation of Pub-Sub)

**Core Idea:**
A "Newsletter Subscription." When one object (the Subject) changes, all its "Subscribers" (the Observers) are notified automatically.

**Why it matters:**
This is the heart of **Decoupling**. The Subject doesn't need to know what the Observers do. It just shouts, "I changed!", and the Observers handle their own logic.

**When to use:**
*   UI buttons and listeners (`ActionListener`).
*   Logging systems where multiple loggers (File, Console, Cloud) listen for errors.
*   Real-time notifications (WebSockets, Price Trackers).

**When NOT to use:**
*   For simple request-response loops.
*   When the number of observers is huge and notifications happen every millisecond (this can cause "Notification Lag").

**Example (Spring Events):**
Using `ApplicationEventPublisher`. When a user registers, you publish a `UserRegisteredEvent`. Three separate observers (EmailService, AnalyticsService, RewardsService) catch the event and do their work independently.

**Deep Dive:**
The Subject maintains a `List<Observer>`. When a change occurs, it loops through the list and calls `observer.update()`. In Java, this is often implemented using the **Listener** pattern.

**Advanced Insight:**
**Memory Leaks (Lapsed Listeners).** If an Observer "subscribes" but never "unsubscribes," the Subject will keep a strong reference to it forever. This prevents the Observer from being Garbage Collected. **Always unsubscribe!**

**Production Tip:**
In distributed systems, we move from the Observer pattern to **Pub-Sub** using **Kafka** or **RabbitMQ**. This allows the "Subject" and "Observer" to be on completely different servers.

**Interview Trap:**
"What's the difference between Push and Pull models in Observer?"
**Answer:** In the **Push** model, the Subject sends the data directly to the observer. In the **Pull** model, the Subject only tells the observer "Something changed," and the observer has to query the subject to get the specific data it needs.

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| How can you break a Singleton? | 1. **Reflection** can change the private constructor to public. 2. **Serialization** will create a new instance when deserializing. 3. **Cloning**. Enum Singletons inherently prevent all three. |
| Difference between Factory and Abstract Factory? | `Factory Method` creates one type of object based on logic. `Abstract Factory` is a factory of factories — it creates families of related objects (e.g., MacUIFactory vs WindowsUIFactory). |
| What pattern does Spring's `@Transactional` use? | **Proxy Pattern**. Spring creates a dummy "Proxy" wrapper around your class. When you call the method, the Proxy intercepts it, opens a DB transaction, calls your real method, and then commits/rolls back. |
| Difference between Proxy and Decorator? | `Proxy` controls access to an object (lazy loading, security, transactions). `Decorator` adds new responsibilities to an object dynamically (e.g., wrapping a core `Coffee` object with `Caramel` and `Milk` decorators). |
### 4.4 Proxy Pattern (The Power Behind Frameworks)

**Core Idea:**
A "Middleman." Instead of talking to the real object, you talk to a "Substitute" that does some extra work (like checking security) before passing the message to the real object.

**Why it matters:**
This is the "Secret Sauce" of **Spring AOP**. It’s how `@Transactional` works. You don't have to write `connection.commit()` in 500 methods; the Proxy does it for you in one place.

**When to use:**
*   **Security:** To check permissions before calling a method.
*   **Lazy Loading:** To wait until the very last second to load a heavy object from the Database (used extensively by Hibernate).
*   **Remote Access:** To treat a remote API as if it were a local object (RPC).

**When NOT to use:**
*   When performance is absolutely critical (e.g., a tight gaming loop). Proxing adds a tiny bit of overhead.

**Example (Spring Hibernate):**
When you call `user.getOrders()`, Hibernate doesn't load all 1,000 orders from the DB immediately. It gives you a **Proxy List**. The moment you call `.size()` or `.get(0)`, the Proxy "wakes up," hits the DB, and fills the data.

**Deep Dive:**
Java has two ways to make Proxies:
1.  **JDK Dynamic Proxy:** Only works if your class implements an **Interface**.
2.  **CGLIB:** Uses bytecode manipulation to create a subclass. This works even for classes without interfaces (which is what Spring uses most of the time).

**Advanced Insight:**
**Self-Invocation Pitfall.** In Spring, if `methodA()` calls `methodB()` *inside the same class*, the Proxy is bypassed. The `@Transactional` on `methodB` will be ignored because the call stays "inside" the object and never hits the Proxy wrapper!

**Pitfall:**
**Final Methods.** You cannot Proxy a `final` class or a `final` method (because the Proxy needs to either implement the interface or extend the class).

**Production Tip:**
Be careful when logging Proxy objects. Some loggers might call `toString()` on a Hibernate proxy, accidentally triggering a massive Database query that you didn't want yet!

**Interview Trap:**
"Difference between Proxy and Decorator?"
**Answer:** A `Decorator` is used to add **features** to an object (e.g., adding `Milk` to `Coffee`). A `Proxy` is used to **control access** to an object (e.g., checking if the user can afford the `Coffee`).


### 4.5 Builder Pattern (Complex Object Assembly)

**Core Idea:**
Instead of a constructor with 20 parameters, you use a "Menu" to pick exactly what you want, one by one.

**Why it matters:**
Solve the **Telescoping Constructor Anti-pattern**. It’s impossible to read `new User(1, "A", "B", true, null, 10, "USA")`. The Builder makes it `User.builder().id(1).name("A").build()`.

**When to use:**
*   Classes with more than 5-7 parameters.
*   Classes with many optional fields.
*   Making immutable objects easily.

**When NOT to use:**
*   For small classes with only 2-3 mandatory fields. A simple constructor is better.

**Example (Production DTO):**
A `SearchQuery` object where a user might search by name, or date, or status, or price range—but almost never all of them at once.

**Deep Dive:**
The Builder is usually a `static inner class` that holds the temporary data and has a `.build()` method that returns the final, private-constructor-protected object.

**Advanced Insight:**
**State Validation.** The best place to check if an object is valid is inside the `.build()` method. This ensures that you never "leak" a partially incorrect object into your application.

**Pitfall:**
**Boilerplate.** Writing the Builder code manually is exhausting. If you change a field in the class, you have to update the builder too.

**Production Tip:**
**Use Lombok `@Builder`.** It generates the entire boilerplate at compile-time. Every senior Java dev uses this to keep their code clean and readable.

**Interview Trap:**
"Can a Builder be used for thread-safety?"
**Answer:** **Yes.** Because a Builder allows you to create **Immutable Objects** (all fields `final`), the resulting object is 100% thread-safe once it's built and published.

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Over-engineering with Patterns | Using a Strategy Pattern when a simple `if/else` on two conditions would suffice adds unnecessary classes and complexity. | Keep it Simple (KISS). Only refactor into patterns when the code starts violating SOLID principles. |
| The Global State Singleton | Using Singleton just to create a globally accessible variable holding application state (like a massive `HashMap`). | This creates tight coupling and makes unit testing a nightmare. Use dependency injection instead. |
| Forgetting `volatile` in Singleton | Without `volatile`, thread A might see a non-null instance pointer *before* the constructor has finished initializing the object's internal fields, leading to NullPointerExceptions later. | Always use `volatile` with Double-Checked Locking. |

---

## 7. Real-World Usage

| Pattern | Where it shows up in Frameworks |
|---|---|
| **Singleton** | In **Spring**, every Bean (`@Service`, `@Repository`) is a Singleton by default. You don't write the code; the `ApplicationContext` manages it. |
| **Proxy** | Spring AOP, `@Cacheable`, `@Transactional`, Hibernate Lazy Loading (it returns a proxy of a DB row, and only hits the DB if you call a getter). |
| **Template Method** | **Spring's `JdbcTemplate` or `RestTemplate`**. The framework defines the entire skeleton for opening a connection/socket, catching errors, and closing it. You only provide the specific query/mapping logic. |
| **Observer** | Message Brokers (`Kafka`, `RabbitMQ`) pushing data to listeners, or Spring's `ApplicationEventPublisher`. |
| **Adapter** | Wrapping `java.util.Date` into a third-party library that only accepts `Calendar` objects. |

---

## 8. Practice Tasks

1.  **Enum Singleton:** Implement a thread-safe Singleton using a Java `enum` instead of double-checked locking. Prove why it's better.
2.  **Notification Factory:** Expand the Factory example in section 4.2. Add a `PushNotification` type. Throw a custom exception if the type is unknown. Write unit tests.
3.  **Discount Strategy:** Write an E-commerce cart system. Use the Strategy pattern to apply different discounts at checkout: `NoDiscount`, `PercentageDiscount(10%)`, `FlatRateDiscount($50)`. 
4.  **Lombok Builder:** Create a `User` class with 10 fields (id, name, email, phone, age, etc.). Use the `@Builder` annotation from Lombok and instantiate the class setting only 4 of the fields.

---

## 9. Quick Revision

| Pattern | Type | Purpose / Keyword |
|---|---|---|
| **Singleton** | Creational | Exactly 1 shared instance. (DbConnection, Spring Beans) |
| **Factory** | Creational | Hides instantiation logic (e.g. `switch(type) -> new Object()`) |
| **Builder** | Creational | Step-by-step assembly of complex objects. Solves constructor bloat. |
| **Proxy** | Structural | Intercepts calls for a target object. (Lazy Load, Security, Spring @Transactional) |
| **Adapter** | Structural | Makes two incompatible interfaces talk. |
| **Facade** | Structural | Huge complex subsystem? Hide it behind one simple gateway method. |
| **Strategy** | Behavioral | Swap algorithms (if-else logic) at runtime via an interface. |
| **Observer** | Behavioral | Subscriptions (Pub-Sub). "Tell me when your state changes." |
| **Template Method** | Behavioral | Fixed skeleton workflow in parent, specific step execution in child. |
