<!-- Part of Java Learning Roadmap — Section 4 -->

# 🔀 4. Java Concurrency & Multithreading

---

## 1. Definition

**Concurrency** is the ability of an application to make progress on multiple tasks simultaneously (acting like they are running at the same time by context switching). **Parallelism** is actually executing multiple tasks at the exact same physical time on multicore processors.

In Java, this is achieved via **Threads**.
### 1.1 Process vs. Thread

**Core Idea:**
A **Process** is like a whole office building (its own space, utilities, and security). A **Thread** is like an employee inside that building (shares the workspace/Heap, but has their own desk/Stack).

**Why it matters:**
Modern CPUs have many "cores." If you only use one thread, you are paying for an 8-core CPU but only using 1/8th of its power. Parallelism is the only way to scale high-traffic systems.

**When to use:**
*   To perform background tasks (sending emails, processing logs) without freezing the UI.
*   To handle multiple user requests in a web server (Spring/Tomcat).

**When NOT to use:**
*   When the task is too small (the time spent creating the thread is longer than the task itself).
*   In purely sequential logic where one step *must* finish before the next.

**Example (Spring Boot):**
In a REST controller, using `@Async` on a method allows the main request thread to return a "202 Accepted" immediately, while a background thread handles the heavy report generation.

**Deep Dive:**
*   **Process:** Managed by the OS. Completely isolated from other processes. If one crashes, others survive.
*   **Thread:** Managed by the JVM (mostly). Shares the **Heap** (objects) with other threads but has a private **Stack** (local variables) and **PC Register** (instruction pointer).

**Advanced Insight:**
**Context Switching.** This is the "hidden tax" for multithreading. When the OS switches from Thread A to Thread B, it must save A's state and load B's state into the CPU registers. If you have too many threads (thousands), the CPU spends more time switching than doing real work!

**Pitfall:**
**Memory Visibility.** Since threads share the Heap, if two threads change the same object without synchronization, they can "corrupt" the data (Race Condition).

**Production Tip:**
Always name your threads (via custom `ThreadFactory`). When you look at a **Thread Dump** in production to debug a freeze, seeing "Order-Processing-Thread-1" is much more helpful than "Thread-42."

**Interview Trap:**
"Can threads share their local variables?"
**Answer:** **No.** Local variables live on the **Stack**, which is private to each thread. Only objects on the **Heap** (instance variables) are shared.

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

### 3.2 Java Memory Model (JMM) & `volatile`

**Core Idea:**
`volatile` is a "Red Flag" told to the CPU: "Don't cache this value! Always read it directly from the main RAM."

**Why it matters:**
Modern CPUs are so fast they keep data in a private "L1 Cache" for speed. If Thread 1 updates `running = false` in its L1 cache, Thread 2 on another core might keep reading `true` from its own L1 cache forever, causing an infinite loop.

**When to use:**
*   For flags (like `boolean stopSignal`) used to communicate between threads.
*   When you need high speed and only care about **visibility**, not complex math.

**When NOT to use:**
*   When performing operations like `count++`. `volatile` does NOT make operations atomic.
*   For complex business logic involving multiple variables.

**Example:**
A "Health Check" background thread that reads a `volatile boolean isSystemHealthy` flag updated by various monitoring threads.

**Deep Dive:**
The JMM defines a **"Happens-Before"** relationship. When a thread writes to a `volatile` variable, all memory writes made by that thread *before* the volatile write are guaranteed to be visible to any other thread that subsequently reads that same `volatile` variable.

**Advanced Insight:**
**Instruction Reordering.** To optimize performance, the CPU/JIT compiler sometimes swaps the order of your code lines. `volatile` acts as a **"Memory Barrier"** (Fence), preventing the compiler from moving instructions across that line.

**Pitfall:**
Assuming `volatile` is a replacement for `synchronized`. It is not. It solves the **Visibility** problem, but does $not$ solve the **Atomicity** problem.

**Production Tip:**
If you have a singleton that is lazily initialized, use a **Double-Checked Locking** pattern with a `volatile` instance variable to prevent threads from seeing a partially constructed object.

**Interview Trap:**
"Does `volatile int x; x++;` work safely with multiple threads?"
**Answer:** **No.** `x++` is actually three steps: Read, Increment, Write. Between Read and Write, another thread can interject. You need `AtomicInteger` or `synchronized` for this.

### 3.4 Virtual Threads (Project Loom - Java 21)

**Core Idea:**
"Java threads on a diet." Instead of 1 Java thread = 1 heavy OS thread (1MB), you can now have millions of Java threads running on just a few OS threads.

**Why it matters:**
Traditionally, if your app handles 5,000 users at once, you need 5,000 OS threads, which crashes the server due to RAM exhaustion. Virtual threads solve this, making Java as scalable for I/O as Node.js or Go.

**When to use:**
*   **I/O-heavy tasks:** Database calls, HTTP API requests, reading files.
*   Replacing almost all usage of standard "Platform Threads" in web servers.

**When NOT to use:**
*   **CPU-heavy tasks:** Complex math, image processing, video encoding. Virtual threads won't help here; you still need physical cores.

**Example (Spring Boot 3.2+):**
By setting `spring.threads.virtual.enabled=true`, Tomcat will now use Virtual Threads for every incoming HTTP request, allowing your microservice to handle massive traffic with virtually zero memory overhead.

**Deep Dive:**
When a Virtual Thread hits a blocking call (like `db.query()`), the JVM "unmounts" it from the OS thread (Carrier Thread) and saves its state in the Heap. The OS thread is then free to run a different Virtual Thread. Once the DB responds, the JVM "remounts" the first thread and continues.

**Advanced Insight:**
**Pinning.** If a Virtual Thread enters a `synchronized` block and then tries to perform I/O, it gets "pinned" to the OS thread. The OS thread cannot be freed. This defeats the purpose of Virtual Threads. This is why Java developers are moving to `ReentrantLock` instead of `synchronized`.

**Pitfall:**
**ThreadLocal abuse.** Since you can have millions of Virtual Threads, using heavy `ThreadLocal` storage can still leak massive amounts of Heap memory. Use **Scoped Values** (Java 21) as a better alternative.

**Production Tip:**
Do **NOT** pool Virtual Threads. Creating them is as cheap as creating a `new Object()`. Just create a new one for every task and let it die when finished.

**Interview Trap:**
"Can Virtual Threads make my code run faster?"
**Answer:** **Directly, No.** They don't speed up the computation. They improve **Throughput** (handling more tasks at once), not **Latency** (making one task finish faster).

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

### 4.2 ExecutorService & Thread Pools

**Core Idea:**
A "Hiring Agency" for threads. Instead of creating and firing a worker for every tiny task, you keep a steady crew of workers (Pool) and give them tasks one by one.

**Why it matters:**
Creating an OS thread involves a "Syscall," which is very slow. If you create a new thread for every 1ms task, you spend 90% of your time creating threads and only 10% doing work.

**When to use:**
*   Always. In production, never use `new Thread()`. Use an `ExecutorService`.
*   Handling background batches or fixed-size parallel tasks.

**When NOT to use:**
*   When using Java 21 Virtual Threads (you don't pool Virtual Threads).
*   For extremely short, infrequent one-off tasks (though even then, a pool is safer).

**Example:**
A report generator that takes 1,000 Excel rows and processes batches of 50 rows in parallel using a `FixedThreadPool(8)`.

**Deep Dive:**
*   **FixedThreadPool:** Best for predictable CPU-bound tasks.
*   **CachedThreadPool:** Grows as needed. Good for many short-lived tasks, but can crash the server if too many arrive at once.
*   **WorkStealingPool:** Uses multiple queues to ensure no core is idle while others are busy.

**Advanced Insight:**
**The BlockingQueue.** Every ExecutorService has an internal queue. If the pool is full, new tasks stay in the queue. If the queue fills up, the **RejectedExecutionHandler** kicks in (default is to throw an exception).

**Pitfall:**
**Forgetting to `.shutdown()`.** An `ExecutorService` acts like a "non-daemon" thread. If you don't shut it down, your Java app will never stop even if the main method is finished.

**Production Tip:**
Always define a **Thread Queue Limit**. Using an unbounded queue (like the default `LinkedBlockingQueue`) can lead to $OutOfMemoryError$ if tasks arrive faster than they are processed.

**Interview Trap:**
"What's the difference between `execute()` and `submit()`?"
**Answer:** `execute()` (from `Runnable`) returns `void`—it's fire-and-forget. `submit()` (from `Callable`) returns a `Future`, allowing you to get the result or catch an exception later.

### 4.3 Synchronization & ReentrantLocks

**Core Idea:**
A "Bathroom Door Lock." It ensures only one thread can enter the "Critical Section" (the toilet) at a time, preventing messy race conditions.

**Why it matters:**
Without locks, if two threads do `balance = balance - 100` at the same time, they might both read `$500`, subtract 100, and write `$400`, accidentally "deleting" a transaction.

**When to use:**
*   Protecting any shared mutable state (counters, lists, business entities).
*   Implementing complex atomic operations across multiple variables.

**When NOT to use:**
*   On read-only data (immutability is the best concurrency strategy).
*   When `AtomicInteger` or `ConcurrentHashMap` can do the job faster without locking.

**Example:**
A `StockInventory` class where `deductStock()` is marked `synchronized` to ensure we never oversell an item during a flash sale.

**Deep Dive:**
*   **Synchronized:** uses an "Intrinsic Monitor Lock" on the object. If a thread crashes while holding it, the lock is automatically released.
*   **ReentrantLock:** An explicit lock from `java.util.concurrent`. It offers **Fairness** (ordering), `tryLock()` (don't wait forever), and can be interrupted.

**Advanced Insight:**
**Deadlocks & Liveness.** If Thread 1 holds Lock A and wants B, and Thread 2 holds Lock B and wants A, they sit forever. Modern architects use `tryLock()` with a timeout to detect and break these stalemates.

**Pitfall:**
**Synchronizing on the wrong object.** If you synchronize on a `new Object()` inside a method, every thread gets its own lock, making the synchronization useless. Always lock on a shared `final` field.

**Production Tip:**
Avoid `synchronized` methods in Java 21 Virtual Threads. Use **`ReentrantLock`** instead. Synchronized blocks can "Pin" the virtual thread to the OS carrier thread, killing your server's scalability.

**Interview Trap:**
"Can a thread acquire the same lock twice?"
**Answer:** **Yes.** Java locks are **Reentrant**. A thread holding a lock can enter another block synchronized on the same object without blocking itself.

### 4.4 CompletableFuture & Async Pipelines

**Core Idea:**
A "Voucher." You give someone a task and they give you a voucher (`CompletableFuture`). You can tell the voucher, "Once the task is done, do this next, then that," all without waiting around.

**Why it matters:**
Classic threads "Block" (sit idle doing nothing) while waiting for an API. `CompletableFuture` allows the thread to be released to do other work, only "waking up" when the result is actually ready.

**When to use:**
*   Calling multiple Microservices in parallel.
*   Complex multi-step workflows (Step 1 → Step 2 → Step 3).

**When NOT to use:**
*   Simple logic where synchronous code is easier to read.
*   When you don't care about non-blocking performance.

**Example:**
An e-commerce "Checkout" page:
1. Fetch User Profile (Async)
2. Fetch Inventory (Async)
3. *Combine results* to calculate shipping (Async)
4. Send Email (Async)

**Deep Dive:**
It implements the `Future` and `CompletionStage` interfaces. It uses the **ForkJoinPool.commonPool()** by default, but you should always provide your own custom `Executor` for production isolation.

**Advanced Insight:**
`thenApply` vs `thenCompose`. 
*   `thenApply`: Used for simple mapping ($T \to U$).
*   `thenCompose`: Used when the next step *also* returns a `CompletableFuture` ($T \to CF<U>$), preventing nested "Nested Vouchers."

**Pitfall:**
Blocking with `.get()`. This defeats the entire purpose. Always use `.thenAccept()` or `.handle()` callbacks to keep the pipeline reactive.

**Production Tip:**
Always use the `Async` versions of methods (e.g., `thenApplyAsync`) and pass a dedicated `ExecutorService`. This prevents your business logic from "stealing" threads from the shared system pool.

**Interview Trap:**
"How is `CompletableFuture` different from a regular `Future`?"
**Answer:** A `Future` can only be checked for completion or blocked on. A `CompletableFuture` can be manually completed, chained with callbacks, and combined with other futures without blocking.

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

### 7.1 `ThreadLocal` & Scoped Values

**Core Idea:**
A "Personal Locker." Each thread gets its own private copy of a variable that no other thread can see or touch.

**Why it matters:**
It allows you to store "Context" (like a user ID or a DB connection) and access it anywhere in your code without passing it through 50 method parameters.

**When to use:**
*   Storing a `UserSession` for the duration of an HTTP request.
*   Keeping an expensive object like `SimpleDateFormat` (which is NOT thread-safe) private to each thread.

**When NOT to use:**
*   General data storage (it makes code hard to test and hidden dependencies).
*   In high-frequency Virtual Threads (use **Scoped Values** instead).

**Example (Spring Security):**
`SecurityContextHolder` uses a `ThreadLocal` to store the details of the currently logged-in user so your Service layer can check permissions without knowing about the HTTP Controller.

**Deep Dive:**
A `ThreadLocal` map is actually stored *inside* the `Thread` object. When the thread dies, the map should be GC'd.

**Advanced Insight:**
**ThreadLocal Leak (The Silent Killer).** In web servers, threads are reused from a pool. If Thread 1 sets `userId = 123` and finishes, but doesn't call `.remove()`, the *next* user who gets that same thread will "inherit" the previous user's ID. **Always remove in a `finally` block.**

**Pitfall:**
Using `static ThreadLocal` in a shared library. It becomes almost impossible to track who is setting/clearing it, leading to memory leaks that are notoriously hard to debug in production.

**Production Tip:**
In Java 21, prefer **Scoped Values**. They are immutable, safer, and perform significantly better with millions of Virtual Threads than traditional `ThreadLocal`.

**Interview Trap:**
"How do you share a `ThreadLocal` with a child thread?"
**Answer:** Use `InheritableThreadLocal`. However, be careful as changes in the parent *after* the child is created are usually not visible to the child.


### 7.2 Atomic Variables (Lock-Free Concurrency)

**Core Idea:**
"Magic Variables" that can be updated safely by multiple threads without using any locks at all.

**Why it matters:**
Locks are slow. They involve the OS and context switching. Atomics use CPU instructions (CAS) to perform updates at hardware speed.

**When to use:**
*   Counters (`AtomicInteger`).
*   Boolean flags needing atomic state changes (`AtomicBoolean.compareAndSet`).
*   Reference updates (`AtomicReference`).

**When NOT to use:**
*   When you need to update two variables together as one unit.
*   For complex business logic that requires a "Stop-the-world" lock.

**Example:**
A `RequestCounter` in a high-traffic API that increments for every hit. Using `AtomicLong` is 10x faster than a `synchronized` counter.

**Deep Dive:**
They use **CAS (Compare-And-Swap)**. The CPU instruction says: "If the current value is X, change it to Y. If it's not X, tell me I failed." The thread then usually retries in a tight loop.

**Advanced Insight:**
**ABA Problem.** In some systems, a value changes from A to B back to A. A simple CAS won't detect this. `AtomicStampedReference` solves this by adding a "version number" (stamp) to the value.

**Pitfall:**
**High Contention.** If 1,000 threads try to update the same `AtomicInteger` at once, they spend so much time retrying the CAS loop that performance drops. For massive contention, use **`LongAdder`** instead.

**Production Tip:**
Use `LongAdder` or `DoubleAdder` for high-volume statistics (like metrics/logging). They split the sum into multiple "cells" to reduce CPU contention, making them much faster than `AtomicLong` in huge systems.

**Interview Trap:**
"Is `AtomicInteger` always faster than `synchronized`?"
**Answer:** Not always. In low contention (1-2 threads), Atomics are faster. In extreme contention, the retry loops can consume more CPU than a simple lock wait.

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
