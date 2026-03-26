<!-- Part of Java Learning Roadmap — Section 2 -->

# 🧱 2. Object-Oriented Programming (OOP) in Java

---

## 1. Definition

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **objects** (data structures consisting of fields/attributes and methods/behaviors) rather than functions and logic. 

Java's OOP model is built on four core pillars:
1.  **Encapsulation:** Wrapping data (variables) and code acting on the data (methods) together as a single unit, restricting direct access.
2.  **Abstraction:** Hiding complex implementation details and exposing only the essential features of an object.
3.  **Inheritance:** A mechanism where a new class (subclass) acquires the properties and behaviors of an existing class (parent class).
4.  **Polymorphism:** The ability of a single interface or method to take on multiple forms (compile-time overloading and runtime overriding).

---

## 2. Why It Exists

*   **Modularity:** Code is organized into independent, reusable objects.
*   **Maintainability:** Changes in one object's internal implementation do not break other parts of the system (Encapsulation).
*   **Reusability:** Inheritance allows developers to reuse heavily tested baseline code.
*   **Flexibility:** Polymorphism allows a single interface to drive different underlying implementations dynamically at runtime.

---

## 3. How It Works Internally

### 3.1 Object Creation Flow
When you write `new MyClass()`:
1.  **Memory Allocation:** The JVM allocates memory on the Heap for the new object.
2.  **Zeroing:** All instance variables are set to their default values (`null`, `0`, `false`).
3.  **Constructor Execution:** The constructor is called to execute initialization logic.
4.  **Reference Assignment:** The memory address of the new object on the Heap is assigned to the reference variable on the Stack.

### 3.2 Dynamic Method Dispatch (Runtime Polymorphism)
During runtime, if an overridden method is called through a parent class reference, the JVM looks at the **actual object type** on the heap, not the reference type. It uses the **vtable** (virtual method table) to resolve which method implementation to execute.

### 3.3 Method Overloading vs Overriding

| Feature | Overloading (Compile-time) | Overriding (Runtime) |
|---|---|---|
| **Location** | Same class | Subclass (Child class) |
| **Method Name** | Same | Same |
| **Parameters** | Must be different (type, number, order) | Must be exactly the same |
| **Return Type** | Can be different | Must be same (or covariant) |
| **Binding** | Static binding | Dynamic binding |

### 3.4 Abstract Class vs Interface (Java 8+)

| Feature | Abstract Class | Interface |
|---|---|---|
| **State** | Can have instance variables (state) | Variables are inherently `public static final` |
| **Constructors** | Can have constructors | Cannot have constructors |
| **Methods** | Abstract + Concrete methods | Abstract + `default` + `static` methods (Java 8) |
| **Inheritance**| A class can extend only ONE abstract class | A class can implement MULTIPLE interfaces |
| **Use Case** | Share core logic/state among related classes | Define a contract for completely unrelated classes |

---

## 4. Code Examples

### 4.1 Encapsulation
```java
public class BankAccount {
    // Hidden internal state
    private double balance;

    // Public API to interact with the state safely
    public void deposit(double amount) {
        if (amount > 0) this.balance += amount;
    }
    
    public double getBalance() {
        return this.balance;
    }
}
```

### 4.2 Inheritance and Polymorphism
```java
// Parent
class Animal {
    void makeSound() { System.out.println("Animal sound"); }
}

// Child
class Dog extends Animal {
    @Override // Annotation ensures we actually mapped the method correctly
    void makeSound() { System.out.println("Bark"); }
    void fetch() { System.out.println("Fetching ball"); }
}

public class Main {
    public static void main(String[] args) {
        // Upcasting: Parent reference referencing a Child object
        Animal myAnimal = new Dog(); 
        
        myAnimal.makeSound(); // Prints "Bark" (Runtime Polymorphism)
        // myAnimal.fetch();  // Compile Error: Reference type Animal doesn't know about fetch()
        
        // Downcasting back to Dog to access child-specific methods
        if (myAnimal instanceof Dog d) { // Java 16 Pattern Matching
            d.fetch();
        }
    }
}
```

### 4.3 SOLID Principles Example (Dependency Inversion)
```java
// BAD: High-level class tightly coupled to a low-level implementation
class PaymentService {
    private StripeGateway gateway = new StripeGateway(); 
}

// GOOD: Depend on abstractions (Interface)
interface PaymentGateway { void process(); }
class StripeGateway implements PaymentGateway { public void process() {} }
class PayPalGateway implements PaymentGateway { public void process() {} }

class PaymentService {
    private PaymentGateway gateway;
    // Dependency Injection allows easy swapping of implementations
    public PaymentService(PaymentGateway gateway) { 
        this.gateway = gateway; 
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Why does Java not support multiple inheritance with classes? | **The Diamond Problem**. If Class C extends A and B, and A and B both have a `doWork()` method, C wouldn't know which one to inherit. Java resolves this by allowing multiple interfaces instead. |
| What is the difference between `this` and `super`? | `this` refers to the current object instance. `super` refers to the immediate parent class, used to access parent methods/constructors masked by child class. |
| Can you override a `static` method? | **No**. Static methods belong to the class, not the object. If a child class has a static method with the same signature, it is **method hiding**, not overriding. |
| What is Covariant Return Type? | When an overridden method in a child class returns a narrower type (a subclass) of the type returned by the parent method. |
| What is the difference between Aggregation and Composition? | Both represent "HAS-A" relationships. **Aggregation** is a weak association (Department has Teachers — Teachers exist without Dept). **Composition** is strong association (House has Rooms — Rooms die if House dies). |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Extending a class just to reuse a utility method | Violates "IS-A" design. Tight coupling. | Use Composition ("HAS-A") or Static utility classes. Prefer Composition over Inheritance. |
| Changing method signature while attempting to override | The child will silently just Overload the method, meaning it won't be called polymorphically. | ALWAYS use the `@Override` annotation. It forces a compilation error if the signatures don't match. |
| Returning mutable objects from getters in an encapsulated class | Calling code can modify the object, breaking encapsulation (e.g., returning a `Date` or `List`). | Return defensive copies (`new Date(date.getTime())` or `List.copyOf()`). |
| Putting logic in constructors | Makes unit testing difficult and causes slow instantiation. | Constructors should only assign dependencies/state. Put heavy lifting in `init()` methods. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **Polymorphism** | Spring Security allowing you to inject different `AuthenticationProvider` implementations interchangeably. |
| **Interfaces** | Java Collections Framework (`List`, `Set`, `Map`). JDBC (`Connection`, `Statement` handles different database drivers). |
| **Encapsulation** | JPA Entities/DTOs wrapping database columns with strict validation rules in the setters. |
| **Inheritance** | Custom UI standard components mapping to base classes (e.g., `CustomButton extends JButton`). |

---

## 8. Practice Tasks

1.  **Shape abstract class**: Create an abstract class `Shape` with abstract method `calculateArea()`. Implement `Circle` and `Rectangle`. Put them in a `List<Shape>` and loop through to sum the total area.
2.  **Bank Interface**: Design a `BankAccount` interface with deposits/withdrawals, and implement `SavingsAccount` and `CurrentAccount` (with overdraft logic).
3.  **Refactor violations**: Take an existing code snippet that violates the Single Responsibility Principle (e.g., an `Order` class that also sends emails and saves to DB) and refactor it into proper separated classes.
4.  **Immutability challenge**: Write a perfectly immutable `Student` class that has a `String` name, `int` id, and a `List<String>` of courses. Prove it cannot be mutated after creation.

---

## 9. Quick Revision

```
OOP Pillars:
1. Encapsulation → Hide state, expose behaviors (getters/setters).
2. Abstraction → Hide how it works, expose what it does (Interfaces/Abstract classes).
3. Inheritance → IS-A relationship (extends). Code reuse.
4. Polymorphism → One name, many forms. 
   - Compile-time (Overloading: same name, different params)
   - Run-time (Overriding: exact same signature, dynamic dispatch)

Classes vs Objects: Class is the blueprint. Object is the instance on the Heap.

Interfaces: Contract. Classes can implement multiple. Can have default/static methods.
Abstract Classes: Partial implementation. Classes can extend only one. Has state.

Constructors: No return type, matches class name. Can be overloaded. `super()` calls parent constructor.

SOLID:
S - Single Responsibility
O - Open/Closed (Open for extension, closed for modification)
L - Liskov Substitution (Child can replace Parent seamlessly)
I - Interface Segregation (Small, focused interfaces)
D - Dependency Inversion (Depend on abstractions, not concretions)
```
