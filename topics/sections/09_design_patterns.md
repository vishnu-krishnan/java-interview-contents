<!-- Part of Java Learning Roadmap — Section 9 -->

## 🎨 17. Design Patterns

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
