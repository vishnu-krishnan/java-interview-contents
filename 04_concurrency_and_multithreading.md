<!-- Part of Java Learning Roadmap — Section 4 -->

# 🔀 4. Java Concurrency & Multithreading

---

## 1. Definition

**Concurrency** is the ability of an application to make progress on multiple tasks simultaneously (acting like they are running at the same time by context switching). **Parallelism** is actually executing multiple tasks at the exact same physical time on multicore processors.

In Java, this is achieved via **Threads**.
*   **Process:** An independent execution environment with its own memory space (e.g., a running JVM).
*   **Thread:** A lightweight sub-process. Multiple threads exist within ONE process and share the same Heap memory, but each thread has its own Stack and PC (Program Counter) register.

---

## 2. Why It Exists

*   **Resource Utilization:** Keeps the CPU busy while other threads are blocked waiting for I/O (like a database query or network call).
*   **Responsiveness:** In GUI apps or web servers, background threads handle heavy processing so the main thread can continue accepting user input/requests.
*   **High Throughput:** A web server (like Tomcat) uses a Thread Pool to handle thousands of simultaneous user requests.

---

## 3. How It Works Internally

### 3.1 Thread Lifecycle (The 6 States)
1.  **NEW:** Thread object created, but `start()` not called yet.
2.  **RUNNABLE:** Ready to run, waiting for CPU time from the OS scheduler.
3.  **BLOCKED:** Waiting to acquire a monitor lock (e.g., trying to enter a `synchronized` block that someone else holds).
4.  **WAITING:** Waiting indefinitely for another thread (e.g., calling `wait()` or `join()`).
5.  **TIMED_WAITING:** Waiting for a specific timeframe (e.g., `Thread.sleep(1000)`).
6.  **TERMINATED:** The `run()` method has completed.

### 3.2 Java Memory Model (JMM)
In modern CPUs, each core has its own Cache (L1/L2), while the Main Memory (RAM) is shared.
*   **Visibility Problem:** Thread A updates a variable in Core 1's cache. Thread B reads the variable on Core 2, but sees the old value from Main Memory because Core 1 hasn't flushed its cache yet.
*   **The Fix:** Using the `volatile` keyword forces all reads/writes of that variable directly to Main Memory, ensuring visibility across threads.
*   **Happens-Before:** The JMM guarantees that if action A *happens-before* action B, the memory effects of A will be visible to B.

### 3.3 Virtual Threads (Java 21)
Traditionally, 1 Java Thread = 1 OS Thread (Heavyweight, ~1MB RAM per thread). You max out around a few thousand.
**Project Loom** introduced Virtual Threads: Lightweight threads managed by the JVM. When a Virtual Thread hits a blocking operation, the JVM unmounts it from the OS thread, freeing the OS thread to execute another Virtual Thread. You can create *millions* of them cheaply.

---

## 4. Code Examples

### 4.1 Creating Threads
```java
// 1. Implementing Runnable (Preferred)
Runnable task = () -> System.out.println("Running in " + Thread.currentThread().getName());
Thread t1 = new Thread(task);
t1.start(); // Creates new OS thread

// BAD: t1.run() does NOT create a new thread, runs synchronously in main thread!
```

### 4.2 ExecutorService (Thread Pools)
Never create raw `new Thread()` in production. OS threads are expensive to create/destroy.
```java
ExecutorService pool = Executors.newFixedThreadPool(10); // Reuses 10 threads

for (int i = 0; i < 100; i++) {
    pool.submit(() -> {
        System.out.println("Task processed by " + Thread.currentThread().getName());
    });
}
pool.shutdown(); // Stop accepting new tasks, finish current ones
```

### 4.3 Lock Ordering (Fixing Deadlocks)
```java
Object lockA = new Object();
Object lockB = new Object();

// DEADLOCK RISK:
// Thread 1 locks A, waits for B. Thread 2 locks B, waits for A.

// FIX: Always acquire locks in the exact same global order.
synchronized(lockA) {
    synchronized(lockB) {
        System.out.println("Safe execution");
    }
}
```

### 4.4 CompletableFuture (Non-blocking async pipelines)
```java
// Fetch user async, then fetch their orders async, then print.
// No thread blocking!
CompletableFuture.supplyAsync(() -> fetchUser(123))
    .thenApplyAsync(user -> fetchOrders(user))
    .thenAccept(orders -> System.out.println("Orders: " + orders))
    .exceptionally(ex -> {
        System.err.println("Failed: " + ex.getMessage());
        return null;
    });
```

### 4.5 Virtual Threads (Java 21)
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 100_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1)); // Blocks CHEAPLY
            return i;
        });
    });
} // Finishes 100k tasks in ~1 second, using a handful of OS threads.
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `start()` and `run()`? | `start()` allocates a new call stack and executes the code asynchronously. `run()` executes synchronously on the current thread. |
| Difference between `Runnable` and `Callable`? | `Runnable` cannot return a result and cannot throw checked exceptions. `Callable` returns a generic result (`Future<T>`) and can throw checked exceptions. |
| Difference between `wait()` and `sleep()`? | `wait()` is an `Object` method used for inter-thread communication. It **releases the lock**. `sleep()` is a `Thread` method that pauses execution and **keeps the lock**. |
| What is a Race Condition? | Two or more threads read/write shared data at the same time, producing incorrect results based on unpredictable timing. Fixed by synchronization/Atomic classes. |
| Cannot we just use `volatile` instead of `synchronized`? | No. `volatile` guarantees visibility, NOT atomicity. For `count++` (which is read-modify-write), multiple threads can still overwrite each other's increments. |
| What is a ThreadLocal? | A class that provides thread-local variables. Each thread accessing the variable gets its own independent copy (e.g., storing a unique Transaction ID for a web request constraint). |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Forgetting `ThreadLocal.remove()` in web servers | Thread pools reuse threads for new requests. The new request will see the previous request's isolated data (Memory leak / Security breach). | Always call `.remove()` inside a `finally` block at the end of the request. |
| Synchronizing a whole method unnecessarily | Bottleneck. Only one thread can execute ANY synchronized method on that object instance at a time. | Synchronize only the critical section block: `synchronized(this) { ... }` |
| Calling `.get()` on a `Future` or `CompletableFuture` | It blocks the current thread until the async task finishes, defeating the purpose of async. | Use `.thenApply()` or `.thenAccept()` callbacks to process the result non-blockingly. |
| Virtual Threads + `synchronized` block | "Pinning" — The virtual thread cannot unmount from the OS carrier thread while holding a synchronized lock monitor. | Use `ReentrantLock` instead of `synchronized` when working with Virtual Threads. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **Thread Pools** | Spring Boot / Tomcat defaults to a pool of 200 threads to handle incoming HTTP REST requests concurrently. |
| **`CompletableFuture`** | A microservice calling 3 different external APIs (User Service, Inventory Service, Fraud Service) in parallel, joining the results at the end to respond in 200ms instead of 600ms. |
| **`ThreadLocal`** | Spring Security placing the `SecurityContext` (Logged-in User) into a ThreadLocal so it can be accessed anywhere during the HTTP request without passing it as a method parameter. |
| **`AtomicInteger`** | Generating sequential unique sequence IDs in a busy application without heavy locking. |

---

## 8. Practice Tasks

1.  **Race Condition Simulator**: Write a class with `int count = 0`. Create 10 threads that loop 1000 times doing `count++`. Wait for all to finish and print the result. (It won't be 10,000). 
2.  **Fix the Race**: Fix task 1 using `synchronized`, then fix it using `AtomicInteger`, then fix it using `ReentrantLock`. Compare the code differences.
3.  **Deadlock creation**: Write a program with 2 threads and 2 locks that guarantees a deadlock every time it runs. Analyze the resulting thread dump using `jstack`.
4.  **Producer-Consumer**: Build a bounded buffer using `wait()` and `notify()`. One thread generates numbers, another consumes them. If buffer is full, producer waits. If empty, consumer waits.

---

## 9. Quick Revision

```
Process = App instance (has own memory) | Thread = lightweight path within process (shares memory/heap, has own stack).

Lifecycle: NEW → RUNNABLE ↔ (BLOCKED | WAITING | TIMED_WAITING) → TERMINATED

Keywords:
* synchronized = Mutual Exclusion (Atomicity) + Visibility. Can cause contention.
* volatile = Visibility ONLY. Reads from Main Memory. No atomicity.
* ReentrantLock = Advanced lock (Fairness, tryLock, interruptible).

ExecutorService: Always use Thread Pools, avoid "new Thread()".
Callable: Returns Future<T>, throws Exceptions.
Runnable: Returns void, no checked Exceptions.

Future.get() = Blocking.
CompletableFuture = Non-blocking chains, combines async tasks easily.

ThreadLocal = Variables private to the current executing thread. MUST BE REMOVED to avoid pool leaks.

Java 21 Virtual Threads:
* Managed by JVM, not OS.
* Millions of threads allowed.
* Perfect for I/O blocking (DB calls, HTTP). Not for CPU intensive tasks.
```
