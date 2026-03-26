<!-- Part of Java Learning Roadmap — Section 1 -->

# 📘 1. Core Java

---

## 1. Definition

**Java** is a high-level, statically-typed, object-oriented, platform-independent programming language developed by Sun Microsystems (now Oracle) in 1995. It follows the **WORA** (Write Once, Run Anywhere) principle — Java source code is compiled to **bytecode** which runs on any platform that has a **JVM** installed.

| Component | Full Name | Role |
|---|---|---|
| **JDK** | Java Development Kit | Full toolkit — compiler (`javac`), debugger, JRE |
| **JRE** | Java Runtime Environment | Runtime only — JVM + core libraries |
| **JVM** | Java Virtual Machine | Executes bytecode; handles memory + GC |

---

## 2. Why It Exists

Java was designed to solve three key problems of earlier languages (C/C++):

| Problem | Java's Solution |
|---|---|
| Platform dependency | JVM abstracts the OS — same bytecode everywhere |
| Manual memory management | Automatic Garbage Collection |
| Unsafe pointer arithmetic | No raw pointers — reference types with bounds checking |
| Low code reuse | OOP with inheritance and interfaces |

**Key design goals:** Simple, Secure, Portable, Robust, Multithreaded, High-performance.

---

## 3. How It Works Internally

### 3.1 Compilation & Execution Flow
```
Source code (.java)
    ↓  javac (compiler)
Bytecode (.class)
    ↓  JVM (Class Loader → Bytecode Verifier → JIT Compiler)
Machine code (CPU executes)
```

### 3.2 JVM Memory Areas

| Area | What lives here |
|---|---|
| **Heap** | All objects, instance variables |
| **Stack** | Method call frames, local variables, primitive values |
| **Metaspace** | Class metadata, static variables (Java 8+ — replaced PermGen) |
| **Code Cache** | JIT-compiled native code |
| **PC Register** | Current instruction pointer per thread |

### 3.3 Data Types

**Primitives (stored on Stack):**

| Type | Size | Default | Range |
|---|---|---|---|
| `byte` | 1 byte | 0 | -128 to 127 |
| `short` | 2 bytes | 0 | -32,768 to 32,767 |
| `int` | 4 bytes | 0 | -2³¹ to 2³¹-1 |
| `long` | 8 bytes | 0L | -2⁶³ to 2⁶³-1 |
| `float` | 4 bytes | 0.0f | ~7 decimal digits |
| `double` | 8 bytes | 0.0d | ~15 decimal digits |
| `char` | 2 bytes | '\u0000' | 0 to 65,535 (Unicode) |
| `boolean` | ~1 bit | false | true / false |

**Reference types** (stored on Heap): `String`, arrays, all objects.

### 3.4 String Internals

- **Immutable** — once created, value never changes; "modifications" produce a new object
- **String Pool** — JVM keeps a pool in the Heap; `"hello"` literals are interned automatically
- `new String("hello")` bypasses the pool — creates a new object on the heap
- `intern()` — forces a string into the pool

```
String a = "hello";           // pool → single object
String b = "hello";           // same pool object → a == b is true
String c = new String("hello"); // new heap object → a == c is false
String d = c.intern();        // back to pool → a == d is true
```

### 3.5 Wrapper Classes & Integer Cache
- Wrappers: `int → Integer`, `long → Long`, `double → Double`, `char → Character`, `boolean → Boolean`
- **Integer cache (-128 to 127):** `Integer.valueOf(127) == Integer.valueOf(127)` is `true` (cached), but `Integer.valueOf(200) == Integer.valueOf(200)` is `false` (new objects)

---

## 4. Code Examples

### 4.1 JDK / JRE / JVM check
```java
// Check Java version at runtime
System.out.println(System.getProperty("java.version"));   // e.g. 21.0.2
System.out.println(Runtime.version().feature());           // e.g. 21
```

### 4.2 Primitive vs Reference
```java
int x = 5;           // primitive — stored directly on stack
Integer y = 5;       // reference — points to Integer object on heap
Integer z = 5;
System.out.println(y == z);        // true  (Integer cache -128~127)
System.out.println(y.equals(z));   // true  (always use .equals() for objects)

Integer a = 200;
Integer b = 200;
System.out.println(a == b);        // false (outside cache range!)
System.out.println(a.equals(b));   // true
```

### 4.3 String Pool
```java
String s1 = "Java";
String s2 = "Java";
String s3 = new String("Java");

System.out.println(s1 == s2);        // true  — same pool reference
System.out.println(s1 == s3);        // false — s3 is a new heap object
System.out.println(s1.equals(s3));   // true  — same content
System.out.println(s3.intern() == s1); // true — intern() puts s3 into pool
```

### 4.4 StringBuilder vs StringBuffer vs String
```java
// BAD: String concatenation in loop — O(n²), creates n new String objects
String result = "";
for (int i = 0; i < 1000; i++) result += i;   // DON'T

// GOOD: StringBuilder — O(n), single mutable buffer
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) sb.append(i);
String result = sb.toString();   // DO

// StringBuffer — thread-safe (synchronized), use only when shared across threads
StringBuffer sbuf = new StringBuffer();
sbuf.append("safe");
```

### 4.5 Exception Handling
```java
// Checked exception — must handle or declare
public String readFile(String path) throws IOException {
    return Files.readString(Path.of(path));   // IOException is checked
}

// try-with-resources — auto-closes Closeable resources
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    return br.readLine();
} catch (IOException e) {
    throw new RuntimeException("File read failed", e);  // exception chaining
} finally {
    // runs ALWAYS — even if catch rethrows
    System.out.println("cleanup");
}

// Custom exception
class InsufficientFundsException extends RuntimeException {
    private final double amount;
    InsufficientFundsException(double amount) {
        super("Insufficient funds: needed " + amount);
        this.amount = amount;
    }
    double getAmount() { return amount; }
}
```

### 4.6 Keywords
```java
// final variable — constant
final int MAX = 100;
// MAX = 200;  // compile error

// final method — cannot be overridden
public final void log() { System.out.println("log"); }

// final class — cannot be extended (e.g., String itself is final)
public final class ImmutableConfig { ... }

// static — belongs to class, shared across all instances
public class Counter {
    private static int count = 0;   // shared
    private int id;                  // per-instance
    Counter() { this.id = ++count; }
}

// transient — excluded from serialization
class User implements Serializable {
    String name;
    transient String password;   // NOT saved to byte stream
}

// volatile — ensures visibility across threads, NOT atomicity
private volatile boolean running = true;
```

### 4.7 Serialization & Externalizable
```java
// Serializable — marker interface, JVM handles everything
class Person implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    transient String password;   // excluded
}

// Write
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("p.ser"));
oos.writeObject(person);

// Read
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("p.ser"));
Person p = (Person) ois.readObject();

// Externalizable — full manual control
class Config implements Externalizable {
    String host; int port;
    public Config() {}  // REQUIRED — must have no-arg constructor

    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeObject(host);
        out.writeInt(port);
    }
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        host = (String) in.readObject();
        port = in.readInt();
    }
}
```

---

## 5. Interview Questions

### Conceptual

| Question | Answer |
|---|---|
| JDK vs JRE vs JVM | JDK = JRE + dev tools; JRE = JVM + libraries; JVM = bytecode executor |
| What is WORA? | Bytecode compiled once, runs on any JVM-equipped platform |
| Why is Java not 100% OOP? | 8 primitive types exist outside the object system |
| Heap vs Stack | Heap: objects, long-lived; Stack: method frames, primitives, LIFO, per-thread |
| Why is `String` immutable? | Thread-safety, String Pool reuse, security (passwords, URLs), hashCode caching |
| `==` vs `equals()` | `==` compares references (or primitive values); `equals()` compares content |
| Checked vs Unchecked exception | Checked: compile-time; must handle/declare. Unchecked: runtime; usually programmer error |
| `throw` vs `throws` | `throw` throws an exception instance; `throws` declares a method may throw |
| `final` vs `finally` vs `finalize()` | `final`=keyword; `finally`=cleanup block; `finalize()`=deprecated GC hook |
| What is `serialVersionUID`? | Unique ID for class version — prevents `InvalidClassException` during deserialization if class changes |

### Tricky / Output-Based

**Q: What is the output?**
```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
System.out.println(a == b);   // true  (Integer cache)
System.out.println(c == d);   // false (outside cache)
```

**Q: What is the output?**
```java
String s = "hello";
s.toUpperCase();
System.out.println(s);   // "hello" — String is immutable; toUpperCase() returns new object
```

**Q: Does `finally` always run?**
```java
// NO — finally does NOT run if:
// 1. System.exit() is called in try/catch
// 2. JVM crashes
// 3. Thread is killed (stop())
// Otherwise YES — even if catch rethrows an exception
```

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `String s1 == s2` for equality | Compares references, not content | Use `s1.equals(s2)` |
| `String` concat in loop | O(n²) — creates N new objects | Use `StringBuilder.append()` |
| Catching `Exception` too broadly | Hides root cause, masks different errors | Catch specific exceptions |
| Not closing resources | File/DB connection leak | Use `try-with-resources` |
| Ignoring `serialVersionUID` | `InvalidClassException` on deserialization after class change | Always declare it explicitly |
| `Integer a = 200; a == 200` logic | Outside cache range — fails with `==` | Always use `equals()` |
| Calling `finalze()` manually | Deprecated, unreliable timing | Use `try-with-resources` or `Cleaner` |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **String immutability** | HashMap keys (hashCode cached), HTTP headers, JWT tokens |
| **`StringBuilder`** | SQL query builders, JSON/XML serialization, template engines |
| **Checked exceptions** | File I/O (IOException), JDBC (SQLException) — forced handling |
| **`transient`** | Password fields in `User` entity to skip serialization |
| **`volatile`** | `running` flag in background threads (stop signal) |
| **`serialVersionUID`** | Sending objects over network / to cache (Redis via Java serialization) |
| **`try-with-resources`** | Database connections, file streams, HTTP clients — always used |

---

## 8. Practice Tasks

1. **String Pool explorer** — write a program that proves when `==` is `true` vs `false` for Strings, using literals, `new`, and `intern()`
2. **StringBuilder benchmark** — compare time taken for 10,000 loop concatenations with `String`, `StringBuilder`, and `StringBuffer`
3. **Custom exception hierarchy** — create `AppException → ServiceException → ValidationException`; throw and catch at different layers
4. **Serialization round-trip** — serialize a `User` object (with `transient password`), deserialize and verify password is `null`
5. **`final` keyword matrix** — demonstrate `final` on a variable, method, and class; show what each blocks
6. **Integer cache puzzle** — predict the output of `==` comparisons for values -200, -127, 0, 127, 128, 200

---

## 9. Quick Revision

```
JVM → executes bytecode | JRE = JVM + libs | JDK = JRE + compiler/tools

Primitives: 8 types → stored on Stack | Objects → stored on Heap

String is IMMUTABLE → pool reuse → always use .equals() not ==
StringBuilder → mutable, not thread-safe → use in loops
StringBuffer   → mutable, thread-safe (synchronized) → slower

Integer cache: -128 to 127 → == works | outside range → == fails → use .equals()

Checked exceptions    → compile-time → must handle/declare (IOException, SQLException)
Unchecked exceptions  → runtime → programmer error (NPE, ArrayIndexOutOfBounds)
try-with-resources    → auto-closes Closeable → always use for IO/DB

final   → variable: constant | method: no override | class: no extend
static  → belongs to class, shared
transient → skipped during serialization
volatile  → visibility across threads (NOT atomicity)

serialVersionUID → prevents InvalidClassException on class change
Externalizable   → full manual control over what gets serialized
```
