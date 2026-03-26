<!-- Part of Java Learning Roadmap — Section 4 -->

## 🔀 4. Java Concurrency & Multithreading

- Thread Lifecycle — NEW → RUNNABLE → BLOCKED → WAITING → TIMED_WAITING → TERMINATED
- Creating Threads — `Thread` class, `Runnable`, `Callable`
  - `start()` vs `run()` — key difference
- **Synchronization**
  - `synchronized` — method-level and block-level
  - `volatile` — visibility only, no atomicity
  - `volatile` vs `synchronized` — key differences
  - `ReentrantLock`, `ReadWriteLock`, `StampedLock`
- **Java Memory Model (JMM)**
  - Happens-before relationship
  - Main memory vs CPU cache visibility
- **Common Concurrency Problems**
  - Race Condition — causes and fixes
  - Deadlock — causes, detection, prevention
  - Livelock — threads busy but making no progress
  - Starvation — thread never gets CPU time
- **Executor Framework**
  - `ExecutorService`, `ScheduledExecutorService`
  - Thread pool types: `newFixedThreadPool`, `newCachedThreadPool`, `newSingleThreadExecutor`
  - `submit()` vs `execute()`
- **`Future` and `CompletableFuture`**
  - `Future.get()` blocking behavior
  - `CompletableFuture.supplyAsync()`, `thenApply()`, `thenCompose()`, `thenCombine()`, `exceptionally()`, `allOf()`, `anyOf()`
- **Atomic Classes**
  - `AtomicInteger`, `AtomicLong`, `AtomicReference`
  - CAS (Compare-And-Swap) operations
- **`ThreadLocal`** — thread-scoped state, pitfalls with thread pools
- Synchronization Utilities
  - `CountDownLatch` — wait for N events
  - `CyclicBarrier` — N threads meet at a point
  - `Semaphore` — limit concurrent access
  - `Phaser` — flexible lifecycle
- `ForkJoinPool` — work-stealing, parallel streams
- Parallel Streams — when to use and when NOT to use
- Daemon Threads vs User Threads
- `wait()`, `notify()`, `notifyAll()` — inter-thread communication
- `sleep()` vs `wait()` — lock release behavior
- Connection Pool misconfiguration — thread pool vs DB pool mismatch
- Production scenarios — thread starvation, silent thread death, retry overload

---
