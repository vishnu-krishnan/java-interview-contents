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

### 3.1 Object Creation & Lifecycle

**Core Idea:**
A class is just a set of instructions (blueprint), while an object is the actual "house" built on the heap memory.

**Deep Dive:**
When you write `new MyClass()`:
1.  **Memory Allocation:** The JVM allocates space on the Heap based on the class definition.
2.  **Zeroing:** All instance variables are set to defaults (`null`, `0`, `false`).
3.  **Constructor Chain:** The JVM calls the constructor. The first line of every constructor is an implicit `super()`, linking the child object to its parent's state.
4.  **Reference Assignment:** The memory address is returned and stored in a reference variable on the Stack.

**Advanced Insight:**
**Object Header.** Every object on the heap has a "Mark Word" (storing lock info and GC age) and a "Klass Pointer" (pointing to its class metadata). This header adds 12-16 bytes of overhead to every single object you create.

**Pitfall:**
**Leaking 'this' in a Constructor.** Never pass `this` to another method inside your constructor. The object is not fully initialized yet, and the other method might see partially initialized fields, leading to unpredictable bugs.

**Production Tip:**
Avoid creating large objects (like database connections or thread pools) inside loops. Use the **Singleton** or **Factory** pattern to reuse instances.

**Interview Trap:**
"Can a class have multiple constructors?"
**Answer:** Yes. This is **Constructor Overloading**. But remember, only one can be the "primary" one; others often call it using `this(...)`.

### 3.2 Polymorphism (Dynamic Method Dispatch)

**Core Idea:**
"One name, many forms." It allows you to treat specialized objects (Dog, Cat) as general ones (Animal) without losing their unique behaviors.

**Deep Dive:**
*   **Compile-time (Overloading):** The compiler decides which method to call based on the parameters.
*   **Runtime (Overriding):** The JVM decides which method to call based on the **actual object** on the heap, not the variable's type.

**Advanced Insight:**
**vtable (Virtual Method Table).** The JVM maintains a vtable for every class. When you call an overridden method, the JVM looks up the vtable of the object's class at runtime to find the correct memory address of the method implementation.

**Pitfall:**
**Overriding 'private' or 'static' methods.** You cannot override them. If you try, you are just "hiding" the parent method. The parent reference will still call the parent's version, which is a common source of bugs.

**Production Tip:**
Favor **Composition over Inheritance**. Inheritance creates tight coupling. If you just need a utility from another class, inject it as a field (Composition) rather than extending the entire class.

**Interview Trap:**
"If a parent class has a private method and the child 'overrides' it, which one is called?"
**Answer:** The parent's method is called through a parent reference. Private methods are not visible to subclasses, so polymorphism does not apply to them.

### 3.3 Method Overloading vs Overriding

| Feature | Overloading (Compile-time) | Overriding (Runtime) |
|---|---|---|
| **Location** | Same class | Subclass (Child class) |
| **Method Name** | Same | Same |
| **Parameters** | Must be different (type, number, order) | Must be exactly the same |
| **Return Type** | Can be different | Must be same (or covariant) |
| **Binding** | Static binding | Dynamic binding |

### 3.4 Abstraction (Abstract Class vs Interface)

**Core Idea:**
Defining "what" should be done without saying "how." An interface is a contract; an abstract class is a partial blueprint.

**Deep Dive:**
*   **Interface (Contract):** Use when you want to define a behavior that many unrelated classes can share (e.g., `Comparable`, `Serializable`).
*   **Abstract Class (Hierarchy):** Use when you want to share common state (fields) and core logic among closely related classes (e.g., `AbstractList`).

**Advanced Insight:**
**Default Methods (Java 8+).** Interfaces can now have logic. This was added to allow "Interface Evolution"—adding new functionality to an existing interface (like `Collection.stream()`) without breaking all existing implementations.

**Pitfall:**
Creating an interface with too many methods. This violates the **Interface Segregation Principle (ISP)**. Clients should not be forced to implement methods they don't need.

**Production Tip:**
Always program to an **Interface**, not an **Implementation**. Instead of `ArrayList<String> list = ...`, use `List<String> list = ...`. This makes your code modular and easy to mock during testing.

**Interview Trap:**
"Can an interface have instance variables?"
**Answer:** No. Variables in an interface are implicitly `public static final` (constants). They belong to the interface itself, not to any object that implements it.

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

### 4.4 SOLID Principles & The Architect's View

**Core Idea:**
Five rules that prevent your code from becoming a "Spaghetti Monster" as it grows.

**Deep Dive:**
1.  **S - Single Responsibility:** A class should have only one reason to change.
2.  **O - Open/Closed:** Open for extension, closed for modification (use Inheritance/Interfaces).
3.  **L - Liskov Substitution:** You should be able to replace a parent with a child without breaking the app.
4.  **I - Interface Segregation:** Small, specific interfaces are better than one "Fat" interface.
5.  **D - Dependency Inversion:** Depend on abstractions (Interfaces), not concrete classes.

**Advanced Insight:**
**Composition over Inheritance (Circular Dependencies).** Inheritance can lead to deep hierarchies that are impossible to test. Modern frameworks (like Spring) use **Dependency Injection (DI)** to handle "Composition" automatically for you.

**Pitfall:**
**Over-Engineering.** Don't apply all SOLID principles on Day 1 for a tiny 10-line script. Start simple and refactor into SOLID as the complexity grows.

**Production Tip:**
The **Dependency Inversion Principle** is the heart of Spring. By injecting interfaces, you can swap a `MockDatabase` for a `RealDatabase` without changing a single line of business logic.

**Interview Trap:**
"What happens if a Child class violates Liskov Substitution?"
**Answer:** It usually throws an `UnsupportedOperationException`. For example, if `Square` extends `Rectangle` but throws an error when you try to set height and width independently, it's a violation because it breaks the "Rectangle" contract.

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
