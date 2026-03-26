<!-- Part of Java Learning Roadmap — Section 13 -->

# 🌿 13. Spring Framework (Core)

---

## 1. Definition

**Spring Framework** is an open-source, enterprise-level application framework for Java. It is fundamentally an **Inversion of Control (IoC) Container** that manages the lifecycle, configuration, and dependencies of Java objects (called **Beans**).

The two core pillars of Spring are:
1.  **Dependency Injection (DI):** Instead of an object deciding what dependencies it needs and instantiating them (`new Service()`), the framework "injects" the required dependencies into the object at startup.
2.  **Aspect-Oriented Programming (AOP):** Extracting cross-cutting concerns (like logging, security, and transaction management) away from the core business logic.

---

## 2. Why It Exists

Before Spring, Enterprise Java Beans (EJB) were heavy, complex, and required application servers. Spring solved this by introducing:
*   **Loose Coupling:** Classes depend on abstractions (interfaces), and Spring decides which implementation to inject. Makes unit testing incredibly easy.
*   **Boilerplate Reduction:** Solved the nightmare of writing massive `try-catch-finally` blocks for JDBC, Transactions, and API error handling.
*   **AOP:** You no longer need to write `logger.info("started")` at the beginning of your 500 service methods. AOP does it invisibly.

---

## 3. How It Works Internally

### 3.1 The IoC Container (`ApplicationContext`)
When the application starts, Spring scans the classpath for classes annotated with stereotypes (`@Component`, `@Service`, `@Repository`). It uses the **Reflection API** to instantiate these classes, resolve their dependencies (constructor arguments), and wire them together. This "Graph of Beans" is stored in the `ApplicationContext` in memory.

### 3.2 Thread Safety and Bean Scopes
By default, every Spring Bean is a **Singleton**. Spring creates exactly **one** instance of `@Service UserService` and shares it across all threads rendering HTTP requests.
Because it's shared, **Spring Beans must be stateless**. If you put a class-level variable `private String currentUserId;` inside a `@Service`, Thread A will overwrite Thread B's user ID (Race Condition).

### 3.3 AOP (Dynamic Proxies)
When you apply an Aspect (like `@Transactional`) to a `UserService`, Spring does not hand you the actual `UserService` object. It uses **CGLIB** or **JDK Dynamic Proxies** to generate a fake subclass (a Proxy) of `UserService`. When the controller calls a method, it hits the Proxy. The Proxy starts the transaction, calls the real method, and then commits the transaction.

---

## 4. Code Examples

### 4.1 Dependency Injection Methods
```java
@Service
public class OrderService {
    
    // ❌ BAD: Field Injection. Cannot create OrderService in a Unit Test without Spring.
    // @Autowired 
    // private PaymentGateway gateway;

    // ✅ GOOD: Constructor Injection. Enforces immutability. No @Autowired needed in modern Spring.
    private final PaymentGateway gateway;

    public OrderService(PaymentGateway gateway) {
        this.gateway = gateway;
    }
}
```

### 4.2 Aspect-Oriented Programming (AOP)
```java
@Aspect
@Component
public class LoggingAspect {

    // Pointcut: "Run this around ANY method inside the 'service' package"
    @Around("execution(* com.myapp.service.*.*(..))")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        
        // Execute the actual actual target method
        Object proceed = joinPoint.proceed(); 
        
        long executionTime = System.currentTimeMillis() - start;
        System.out.println(joinPoint.getSignature() + " executed in " + executionTime + "ms");
        
        return proceed;
    }
}
```

### 4.3 Bean Scopes
```java
@Component
@Scope("prototype") // A brand new instance is created EVERY time this is injected
public class ReportGenerator {
    // Has state, so it must be prototype
    private List<String> lines = new ArrayList<>(); 
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `ApplicationContext` and `BeanFactory`? | `BeanFactory` is the basic IoC container (Lazy initialization). `ApplicationContext` extends it, adding AOP, event publishing, and eager initialization of singletons. Always use `ApplicationContext`. |
| Difference between `@Component`, `@Service`, `@Repository`? | Functionally identical to the IoC container. They are semantic markers. `@Repository` does have a special feature: it automatically catches DB-specific SQLExceptions and translates them into Spring's unified `DataAccessException`. |
| What is the problem with Field Injection `@Autowired`? | 1. Allows circular dependencies to pass compilation. 2. You cannot mock/inject the dependency easily in a pure JUnit test (you'd need Reflection). 3. The field cannot be `final`. |
| What happens if you inject a `Prototype` bean into a `Singleton` bean? | The Singleton is created only once. Therefore, the injection only happens once. The Prototype acts exactly like a Singleton! Fix it using `@Lookup` method injection or `ObjectFactory`. |
| What is a Circular Dependency? | Bean A requires Bean B in its constructor, but Bean B requires Bean A in its constructor. Spring fails to start. Fix: Redesign architecture to remove the cycle, or use `@Lazy` injection. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Adding state (class variables) to a `@Service` | Spring Beans are Singletons. Under load, 50 threads will read/write that variable simultaneously causing severe data corruption. | Keep Beans **stateless**. Pass state through method parameters. |
| Making AOP Aspect methods `private` | The Spring Proxy cannot intercept or override private, static, or final methods. The aspect will simply be ignored. | Component methods you want proxied must be `public` (or package-private minimally). |
| Overusing AOP | Makes the codebase "magical". Developers get confused reading the code because the execution flow jumps implicitly without explicit method calls. | Restrict AOP to true cross-cutting concerns: Logging, Security, and Transactions. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **IoC / DI** | Injecting AWS S3 clients, Database Repositories, and Email Senders into Business Logic services strictly via interfaces, allowing local mock environments. |
| **AOP** | `@Secured("ROLE_ADMIN")`. Spring Security intercepts the HTTP request, checks the JWT token authorities via AOP, and either allows the execution or throws a 403 Forbidden. |
| **`@Qualifier`** | When you have two `PaymentGateway` implementations (`Stripe` and `PayPal`), injecting it requires `@Qualifier("paypalGateway")` to tell Spring exactly which bean to grab. |

---

## 8. Practice Tasks

1.  **Constructor vs Field:** Write a `UserService` that depends on `UserRepository`. Do it with `@Autowired` field injection first. Then write a unit test without using `@SpringBootTest` (just `new UserService()`). Note the `NullPointerException`. Fix it by refactoring to Constructor injection.
2.  **AOP Timer:** Build a custom annotation `@LogExecutionTime`. Write an AOP `@Around` aspect that intercepts only methods tagged with this custom annotation, logs the time it took to complete, and prints it to the console.
3.  **Prototype Trap:** Create a Singleton `CounterService` and a Prototype `TicketComponent`. Inject the Ticket into the Counter. Call a method on Counter 5 times that increments the Ticket ID. Print the ID. Is it creating 5 tickets or modifying 1? Fix it using `@Lookup`.

---

## 9. Quick Revision

### Core Concepts
*   **IoC:** The Framework calls your code (You don't call `new()`).
*   **DI:** Passing dependencies into an object (Constructor injection enforced).
*   **AOP:** Intercepting method calls (Proxies) to add secondary logic (Logging/Security).

### Bean Scopes
| Scope | Lifespan | Use Case |
|---|---|---|
| **Singleton** | 1 per Application Context | Services, Repositories, Controllers |
| **Prototype** | 1 per requested Injection | Stateful helper objects |
| **Request** | 1 per HTTP Request | Web layer, keeping tracking of current user |
| **Session** | 1 per HTTP Session | Shopping cart data |

### Injection Priorities
1. `Primary` annotation.
2. `@Qualifier("beanName")`.
3. Fallback: matches field/parameter variable name to the bean name (lowerCamelCase).
