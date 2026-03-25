## 🚀 30 Days of Java Interview Questions – Day 11

💡 Question:
What is Singleton Design Pattern in Java?

🔹 What is Singleton?

Singleton Design Pattern ensures that a class has only one instance and provides a global point of access to it.

🔹 Key Features

- Only one object is created
- Global access to that instance
- Controlled object creation

🔹 Real World Use Cases

- Logger
- Database Connection
- Configuration Manager
- Caching

🔹 Implementation Example

```java
class Singleton {

 private static Singleton instance;

 private Singleton() {}

 public static Singleton getInstance() {
 if (instance == null) {
 instance = new Singleton();
 }
 return instance;
 }
}
```

🔹 Thread-Safe Singleton (Best Practice)

```java
class Singleton {

 private static volatile Singleton instance;

 private Singleton() {}

 public static Singleton getInstance() {
 if (instance == null) {
 synchronized (Singleton.class) {
 if (instance == null) {
 instance = new Singleton();
 }
 }
 }
 return instance;
 }
}
```

⚡ Quick Facts

- Supports lazy initialization
- Can be made thread-safe
- Used when only one instance is required

📌 Interview Tip

Singleton can break due to:

- Reflection
- Serialization
- Cloning

Always use proper handling to make it robust.
---
## 🧠 One Java Pattern That Makes Your Code Flexible: Strategy Pattern

One pattern I’ve found extremely useful in real-world Java applications is the Strategy Pattern.
It solves a common problem:
- Avoiding large if-else or switch blocks when behavior changes based on conditions.

Example without strategy:-
if (type.equals("PAYPAL")) {
 processPaypal();
} else if (type.equals("CARD")) {
 processCard();
} else if (type.equals("UPI")) {
 processUpi();
}

This works… until it doesn’t.
Every new case means modifying existing code, increasing risk.

With Strategy Pattern:-
interface PaymentStrategy {
 void process();
}

Different implementations:-
class CardPayment implements PaymentStrategy { ... }
class PaypalPayment implements PaymentStrategy { ... }
class UpiPayment implements PaymentStrategy { ... }

Usage:-
PaymentStrategy strategy = getStrategy(type);
strategy.process();

Why this pattern matters:
✅ Open for extension, closed for modification
 ✅ Cleaner and more maintainable code
 ✅ Easy to add new behaviors without touching existing logic
 ✅ Better testability

I’ve seen this pattern work really well in:
--> Payment systems
--> Notification handling
--> Pricing or discount engines
--> Feature toggles

Instead of asking “which condition?”, you start asking
 - “which behavior?”

That shift makes systems easier to scale and evolve.

What’s a place where you replaced condition-heavy code with a pattern?
---
## What if understanding a Java framework didn’t come from using it but by building it yourself? 😁

Aetheris comes from the Greek word “aether”, referring to the pure and invisible air of the gods.
I chose this name to represent a lightweight and transparent framework, quietly operating in the background and connecting the web to the core of the application. ⚙️

As part of an academic project, I built Aetheris, a lightweight Java MVC framework based solely on Jakarta Servlet.
The goal was not to compete with established frameworks but to really explore the inner workings of an MVC and learn by building each piece from scratch. 🛠️
Everything is implemented from scratch, no external dependencies:
- Controller and route scanning via annotations
- Static and dynamic routing with URI variables
- Automatic parameter binding for scalars, POJOs, collections and files
- Classic MVC support with JSP and REST endpoints in JSON
- Session handling, authorization and verification via annotations
- File uploads with metadata
- Custom JSON serialization using reflection

This project helped me understand the full HTTP request lifecycle, work with advanced Java reflection, and design a clean, maintainable architecture.
It is not production-ready but a true learning playground. Building your own tools completely changes how you use existing ones.

If you’re curious, a student, or a Java developer, come explore, test, critique, or just share your ideas.
I’d love to see how you would have built certain features or hear about your own experiments.