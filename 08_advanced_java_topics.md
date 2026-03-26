<!-- Part of Java Learning Roadmap — Section 8 -->

# 🚀 8. Advanced Java Topics (JVM, GC, Reflection)

---

## 1. Definition

Java's advanced concepts define how the language executes under the hood. 
*   **JVM Architecture:** The structure of the Java Virtual Machine that loads, verifies, and executes `.class` bytecode.
*   **Garbage Collection (GC):** The automated process of identifying and deleting unused objects on the Heap.
*   **Reflection API:** The ability of Java code to examine and modify its own structure (classes, interfaces, fields, methods) at runtime, bypassing compile-time access controls.

---

## 2. Why It Exists

*   **JVM:** Implements the "Write Once, Run Anywhere" promise. The OS only sees the JVM process, while the JVM handles OS-specific machine code translation.
*   **Garbage Collection:** Prevents developers from having to write `free()` or `delete` (like in C/C++), eliminating dangling pointers and reducing memory leaks.
*   **Reflection:** Enables the creation of powerful dynamic frameworks (like Spring, Hibernate, and JUnit) that can instantiate classes and inject dependencies they didn't know about at compile time.

---

## 3. How It Works Internally

### 3.1 The Three Subsystems of the JVM
1.  **Class Loader Subsystem:** Loads `.class` files into memory. Follows the *Delegation Hierarchy Algorithm* (Bootstrap → Extension → Application ClassLoader).
2.  **Runtime Data Areas (Memory):**
    *   **Method Area (Metaspace):** Class-level data, static variables, JIT compiled code. (Shared)
    *   **Heap:** All dynamically allocated objects. Where GC operates. (Shared)
    *   **Stack:** Local variables and method call frames. (Per Thread)
    *   **PC Register:** Pointer to the current instruction. (Per Thread)
3.  **Execution Engine:** Contains the Interpreter (reads line by line), the **JIT Compiler** (finds repeated "hot text" and compiles it to pure machine code for speed), and the Garbage Collector.

### 3.2 Garbage Collection (Generational Hypothesis)
GC is built on the proven theory that *most objects die young*. The Heap is divided into:
1.  **Young Generation:** Contains *Eden* and two *Survivor Spaces* (S0, S1). Newly created objects go to Eden. When Eden fills, a **Minor GC** occurs. Survivors are moved to S0/S1.
2.  **Old (Tenured) Generation:** Objects that survive many Minor GC cycles get promoted here. When this fills, a **Major GC (Full GC)** occurs, which is much slower and causes "Stop-The-World" pauses.

### 3.3 Modern GC Algorithms
*   **G1 GC (Default Java 9+):** Divides the heap into independent regions. Prioritizes collecting regions with the most garbage first to meet predictable pause-time targets.
*   **ZGC (Java 15+):** Ultra-low latency GC. Scales to Terabyte-sized heaps with pause times strictly under 1 millisecond.

---

## 4. Code Examples

### 4.1 Simulating a Memory Leak (OutOfMemoryError)
Java *does* have memory leaks if you hold onto object references forever!
```java
// BAD: Static list never gets cleared. 
// GC cannot touch these objects because 'leakyList' still references them.
public class MemoryLeak {
    private static final List<byte[]> leakyList = new ArrayList<>();

    public static void main(String[] args) {
        while (true) {
            leakyList.add(new byte[1048576]); // Add 1MB arrays forever
        }
    }
}
// Eventually throws: java.lang.OutOfMemoryError: Java heap space
```

### 4.2 Reflection: Breaking Encapsulation
```java
class SecretBank {
    private double vaultBalance = 1000000.0;
}

public class Hacker {
    public static void main(String[] args) throws Exception {
        SecretBank bank = new SecretBank();
        
        // bank.vaultBalance; // Compile Error: field is private
        
        // Use Reflection to steal the money
        Field field = SecretBank.class.getDeclaredField("vaultBalance");
        field.setAccessible(true); // Bypass private modifier!
        
        double money = (double) field.get(bank);
        System.out.println("Stolen: $" + money); // Works perfectly
    }
}
```

### 4.3 Pass By Value (The common confusion)
Java is strictly **Pass by Value**. For objects, the *value* of the reference (the memory address) is passed by value.
```java
public void modify(StringBuilder ref) {
    ref.append(" World");    // Modifies the actual object on the heap
    ref = new StringBuilder(); // Only changes the local variable, caller is unaffected!
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `ClassNotFoundException` and `NoClassDefFoundError`? | `ClassNotFoundException` happens at runtime (e.g., `Class.forName()`) when a class is not on the classpath. `NoClassDefFoundError` means the class *was* present at compile time, but is missing at runtime (e.g., a jar was deleted). |
| What is a "Stop The World" event? | When the GC halts all application threads to safely identify and move objects in memory. |
| Does `System.gc()` force garbage collection? | **No**. It is only a "suggestion" to the JVM. The JVM decides if/when to actually run it. |
| Pass by Value or Pass by Reference? | Java is 100% **Pass by Value**. Primitives pass their value. Objects pass the *value of their memory reference*. |
| StackOverflowError vs OutOfMemoryError? | `StackOverflowError` = Infinite recursion (Stack fills up). `OutOfMemoryError` = Created too many objects, Heap is full. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Using `ThreadLocal` without `remove()` | In web servers (like Tomcat) that use Thread Pools, the thread goes back to the pool. Next request gets the old user's data. Memory leak. | Always use `try...finally { threadLocal.remove(); }` wrapped around request handling. |
| Tuning GC flags prematurely | Manually setting `-XX:NewRatio` without profiling can actively cripple G1GC's ability to self-optimize. | Rely on default G1GC settings unless profiling tools (VisualVM, JFR) prove intervention is needed. |
| Overusing Reflection | Subverts compile-time type safety. Much slower due to security checks and lack of JIT optimization. | Use interfaces and polymorphism for dynamic behavior whenever possible. Leave Reflection to framework builders. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **Class Loaders** | Tomcat using custom class loaders so different web apps (`.war` files) can run different versions of the same Spring library without conflict. |
| **Reflection** | Spring Boot's `@Autowired`. Spring scans the classpath, finds classes with the annotation, and uses Reflection to instantiate and inject the dependencies into private fields. |
| **GC Tuning** | Setting `-Xms2G -Xmx2G` in Kubernetes Docker containers to prevent the JVM from constantly resizing the heap, which wastes CPU cycles on startup. |
| **JIT Compiler** | The reason a Java microservice is slow on the first 10 requests (interpreted) but lightning fast on the 100th request (converted to Native Machine Code by JIT). |

---

## 8. Practice Tasks

1.  **OOM Crash Simulator:** Write the memory leak from Section 4.1. Run it with the CLI flag `-Xmx10m` to crash it instantly. Change the flag to `-Xmx100m` and observe the difference in time to crash.
2.  **Spring Boot Mock:** Create a custom annotation `@MyInject`. Write a class with two `.java` files. In a `main` method, use Reflection to find all fields deeply annotated with `@MyInject` and instantiate them automatically, simulating Spring.
3.  **GC Logs Analysis:** Run a basic Java app with the flag `-Xlog:gc*`. Read the console output to identify when Minor GCs and Full GCs occur.
4.  **Pass by Value Proof:** Write a swap function `public void swap(Dog a, Dog b)`. Prove that you cannot actually swap the original variables passed from the `main` method.

---

## 9. Quick Revision

### Memory Layout
*   **Heap:** Objects (`new User()`). Governed by GC. Generational (Young / Old). 
*   **Stack:** Primitives (`int`, `boolean`) and Reference pointers. Cleared instantly when method ends.
*   **Metaspace:** `.class` blueprints. Stored in Native OS memory.

### GC Cycle
1. Object created → Eden space. 
2. Eden full → Minor GC. Survivors move to S0/S1.
3. Survive long enough → Promoted to Old Generation.
4. Old Generation full → Major GC (Stop The World).

### JVM Components
*   **JIT:** Just In Time compiler. Replaces interpreted bytecode with native machine code for "hot" pathways.
*   **ClassLoader:** Loading → Linking → Initialization. 
*   **Reflection:** Reading/editing private object state at runtime. (Slow, dangerous, powerful).
