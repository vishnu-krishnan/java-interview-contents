<!-- Part of Java Learning Roadmap — Section 9 -->

# 🎨 9. Design Patterns

---

## 1. Definition

**Design Patterns** are reusable, proven solutions to commonly occurring problems in software design. They are not specific blocks of code, but rather general concepts (blueprints) for solving a problem that can be implemented in many different ways.
They were popularized by the "Gang of Four" (GoF) book, which categorized them into three types:
1.  **Creational:** Deals with object creation mechanisms (`Singleton`, `Factory`, `Builder`).
2.  **Structural:** Deals with object composition and relationships (`Adapter`, `Proxy`, `Facade`).
3.  **Behavioral:** Deals with communication and assignment of responsibilities between objects (`Strategy`, `Observer`, `Template Method`).

---

## 2. Why It Exists

*   **Common Vocabulary:** Saying "I used a Strategy Pattern here" instantly explains your architecture to another engineer without them reading the code.
*   **Time Saving:** Instead of reinventing the wheel to solve a dependency issue, you use an industry-standard best practice.
*   **Maintainability:** By decoupling object creation from business logic (Factory), or decoupling algorithms from their executing context (Strategy), code becomes much easier to test and extend.

---

## 3. How It Works Internally

### 3.1 Singleton (Thread-Safe Double-Checked Locking)
The naive Singleton approach fails in multithreading because two threads can check `if (instance == null)` at the exact same time and create *two* instances.
**Double-Checked Locking** forces threads to serialize *only* when the object is null. Once created, future threads bypass the `synchronized` block completely, ensuring high performance. The `volatile` keyword ensures that the half-initialized object isn't published to other threads before the constructor finishes.

### 3.2 Strategy Pattern (Runtime algorithm swapping)
Instead of a massive `if/else` block based on a type (e.g., `if (type == CREDIT_CARD)`), the context class delegates the algorithm to a `Strategy` interface. You inject the specific strategy implementation into the context at runtime, adhering entirely to the **Open/Closed Principle** (you can add new payment methods without ever touching the core context logic).

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
// Note: In modern Java, using an Enum is the safest way to create a Singleton.
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

### 4.3 Strategy Pattern
```java
interface PaymentStrategy { void pay(int amount); }

class CreditCardStrategy implements PaymentStrategy {
    public void pay(int amount) { System.out.println("Paid " + amount + " via Credit Card"); }
}
class PayPalStrategy implements PaymentStrategy {
    public void pay(int amount) { System.out.println("Paid " + amount + " via PayPal"); }
}

// Context
class ShoppingCart {
    public void checkout(int amount, PaymentStrategy strategy) {
        // Delegates the work. Does not care HOW it pays.
        strategy.pay(amount); 
    }
}

// Client
public class Main {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.checkout(100, new PayPalStrategy()); // Swap out algorithms dynamically!
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| How can you break a Singleton? | 1. **Reflection** can change the private constructor to public. 2. **Serialization** will create a new instance when deserializing. 3. **Cloning**. Enum Singletons inherently prevent all three. |
| Difference between Factory and Abstract Factory? | `Factory Method` creates one type of object based on logic. `Abstract Factory` is a factory of factories — it creates families of related objects (e.g., MacUIFactory vs WindowsUIFactory). |
| What pattern does Spring's `@Transactional` use? | **Proxy Pattern**. Spring creates a dummy "Proxy" wrapper around your class. When you call the method, the Proxy intercepts it, opens a DB transaction, calls your real method, and then commits/rolls back. |
| Difference between Proxy and Decorator? | `Proxy` controls access to an object (lazy loading, security, transactions). `Decorator` adds new responsibilities to an object dynamically (e.g., wrapping a core `Coffee` object with `Caramel` and `Milk` decorators). |
| What is the Builder pattern used for? | Creating complex objects with dozens of optional parameters. It prevents the "Telescoping Constructor Anti-Pattern" (where you have 15 different overloaded constructors). (Often auto-generated using Lombok `@Builder`). |

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
