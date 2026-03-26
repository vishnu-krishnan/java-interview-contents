<!-- Part of Java Learning Roadmap — Section 8 -->

## 🚀 15. Advanced Java Topics

- **JVM Internals**
  - JVM Architecture — Class Loader, Runtime Data Areas, Execution Engine
  - Class Loading — Bootstrap, Platform, Application ClassLoader
  - Bytecode Verification
  - JIT Compilation — interpreted vs compiled
- **Memory Management**
  - Heap (Young Gen: Eden + Survivors, Old Gen), Stack, Metaspace, Code Cache
  - Stack Overflow — causes (deep recursion)
  - Memory Leak — objects retained via collections, caches, listeners
- **Garbage Collection**
  - GC Algorithms — Serial, Parallel, CMS, G1, ZGC, Shenandoah
  - GC Tuning — `-Xms`, `-Xmx`, `-XX:+UseG1GC`
  - GC Pause analysis — `OutOfMemoryError` types
- **Java Reflection API** — `Class<?>`, `Method`, `Field`, dynamic invocation
- **Annotations** — meta-annotations, custom annotation processing
- **Java Modules** (`module-info.java`) — JPMS (Java 9+)
- **Performance Anti-Patterns**
  - String concatenation in loops → use `StringBuilder`
  - Catching generic `Exception`
  - Returning `null` instead of empty collection
  - Magic numbers — use named constants
  - One method doing everything — Single Responsibility

---
