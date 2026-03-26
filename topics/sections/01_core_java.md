<!-- Part of Java Learning Roadmap — Section 1 -->

## 📘 1. Core Java

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
