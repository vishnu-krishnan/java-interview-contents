<!-- Part of Java Learning Roadmap — Section 27 -->

# 💻 27. Coding Programs & Interview Examples

---

## 1. Definition
This section bridges theoretical algorithms with practical Java fluency, testing your mastery of **Java 8 Streams, Lambdas, Collections, and Concurrency**.

### The Golden Rules for Live Coding
1.  **Never Use an IDE:** Practice writing code in a plain text editor (Notepad/Google Doc). Interviews expect you to know standard library methods (`String.substring(int, int)`) without auto-complete.
2.  **Declare Types Properly:** Don't write pseudo-code unless instructed. Use `Map<String, Integer>` instead of just `Map()`.
3.  **Handle Nulls:** In real Java systems, inputs are often `null`. Write `if (input == null || input.isEmpty())` before processing a String.
4.  **Know the Complexity:** Streams are not magical; they run `O(N)` loops. Know the time/space complexity of every stream operation.

---

## 2. Why It Exists
* **Syntax Fluency:** Distinguishes modern engineers (1-line `Collectors.groupingBy()`) from legacy coders (15-line nested `for` loops).
* **Deep Mechanics:** Tests knowledge beyond pure logic to expose JVM understanding (e.g., thread starvation, object pooling, GC overhead).

---

## 3. How It Works Internally
* **Stream Object Allocation:** `list.stream().map(String::toUpperCase).collect(toList())` allocates a new Object on the Heap for every element. For 1M records, this triggers massive Garbage Collection. A primitive `for` loop is mathematically superior for latency-critical paths.
* **Singleton `volatile` Trap:** Without `volatile`, thread A might cache a partially constructed Singleton in its L1 CPU cache. `volatile` enforces a "Happens-Before" memory boundary, flushing read/writes directly to Main RAM.

---

## 4. Code Examples

### 4.1 Canonical Snippets
**Java 8: First Non-Repeating Character** (Finding 'w' in "swiss")
```java
public Character firstNonRepeating(String s) {
    if (s == null || s.isEmpty()) return null;
    return s.chars().mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
            .entrySet().stream()
            .filter(e -> e.getValue() == 1L)
            .map(Map.Entry::getKey).findFirst().orElse(null);
}
```

**Concurrency: Thread-Safe Singleton (Double-Checked Locking)**
```java
public class DBConnection {
    private static volatile DBConnection instance; // volatile prevents instruction re-ordering
    private DBConnection() {}
    public static DBConnection getInstance() {
        if (instance == null) {
            synchronized (DBConnection.class) {
                if (instance == null) instance = new DBConnection();
            }
        }
        return instance;
    }
}
```

### 4.2 The Top 50 Reference Directory (Java 8+)
| # | Problem | Key API / Pattern |
|---|---|---|
| 1-2 | Find/Remove duplicates | `filter(!seen.add(n))` / `.distinct()` |
| 3-4 | First non-repeating / Freq | `groupingBy(..., LinkedHashMap::new, counting())` |
| 5-8 | Sort / 2nd Highest | `.distinct().sorted(reverseOrder()).skip(1).findFirst()` |
| 9-11 | Filter Evens / Uppercase | `.filter(n -> n % 2 == 0)` / `.map(String::toUpperCase)` |
| 12-14 | Flatten / Join / Max Len | `flatMap(Collection::stream)` / `joining(",")` / `max(comparingInt)` |
| 15-18 | Group / Max Salary by Dept | `groupingBy(getDept, maxBy(comparingDouble))` |
| 19-21 | Partition Evens / Sum | `partitioningBy(n%2==0)` / `mapToInt(i->i).sum()` |
| 22-26 | Common / Sort Map / Nulls | `filter(set::contains)` / `comparingByValue()` / `filter(Objects::nonNull)` |
| 27-29 | Word Count / Group by Len | `split("\\s+").length` / `groupingBy(String::length)` |
| 30-31 | Merge Lists / Missing Num | `Stream.concat(l1, l2)` / XOR Trick (`n*(n+1)/2 - sum`) |
| 32-35 | Two Sum / Binary Search | `HashMap O(n)` / Left-Right Pointers `O(log n)` |
| 36-40 | LRU / Sliding Window | `LinkedHashMap(cap, 0.75f, true)` / Single-pass `O(n)` |
| 41-43 | Deadlock / Immutable Class | Lock in same order / `final` + `List.copyOf()` |
| 44-48 | Optional / Virtual Threads | `ofNullable().map().orElse()` / `newVirtualThreadPerTaskExecutor()` |
| 49-50 | Record DTO / Search API | `record User(String name){}` / `@GetMapping + @RequestParam` |

---

## 5. Interview Questions & Traps
| Question | Answer |
|---|---|
| **Why `LinkedHashMap` for consecutive counting?** | `HashMap` randomly scrambles iteration order based on hashes. `LinkedHashMap` preserves exact insertion chronology, ensuring `.findFirst()` is accurate. |
| **Complexity of `groupingBy`?** | Space: `O(N)` (creates a new Map). Time: `O(N)` (single pass iteration). |
| **Why not put `synchronized` on `getInstance()`?** | Method-level synchronization blocks *every* read request eternally. Double-checked locking only synchronizes exactly once during the initial bare creation. |

---

## 6. Common Mistakes

*   **Shared Mutable State in Parallel Streams:** Appending to a generic `ArrayList` inside a `.parallelStream()` causes silent missing data or `ConcurrentModificationException`. **Fix:** Use `ConcurrentHashMap` or return pure collections.
*   **Assuming Array Sizes:** Hardcoding `int[] res = new int[5]` assumes constraints. **Fix:** Use dynamic `ArrayList` mapping.
*   **Modifying Fixed Arrays:** Invoking `.add()` on `Arrays.asList("A", "B")` throws `UnsupportedOperationException`. **Fix:** Wrap it: `new ArrayList<>(Arrays.asList(...))`.

---

## 7. Real-World Usage
*   **Mapping:** Converting 10,000 DB `Entity` records to `ResponseDTO`s before dropping them across the REST API JSON wire.
*   **Grouping:** Aggregation tasks (e.g., feeding a stream of 1M credit card transactions into a `groupingBy(Merchant)` pipeline to calculate total ad-spend).
*   **Double-Checked Locking:** Instantiating extremely heavy configuration objects (AWS S3 Clients, HikariDB Pools) strictly once.

---

## 8. Practice Tasks
1.  **Chaining:** Create a 1-line stream that filters an array of numbers, multiplies by 10, removes duplicates, and sorts descending.
2.  **String Parsing:** Given raw text `"The cat in the hat!"`, remove punctuation, cast lowercase, and stream the top 3 frequent words.
3.  **Concurrency Ruin:** Create 2 threads. T1 locks A then sleeps and locks B. T2 locks B then sleeps and locks A. Observe the JVM freeze to truly understand Deadlocks.

---

## 9. Quick Revision: The Golden Reference

### 9.1 DSA Pattern Recognition — 10 Rules
| # | If the problem says... | Use this |
|---|---|---|
| 1 | Top / min / max **K elements** among N | **Heap** (`PriorityQueue`) |
| 2 | Input is **sorted** (array or list) | **Binary Search** or **Two Pointers** |
| 3 | Need **all combinations** or **permutations** | **Backtracking** or **BFS** |
| 4 | **Tree** or **Graph** traversal | **BFS** (level-order) or **DFS** (depth-first) |
| 5 | Recursive solution exists | Convert to iterative using a **Stack** |
| 6 | O(n²) brute force exists | Look for **HashMap** O(n)/O(n) or **sorting** O(n log n)/O(1) |
| 7 | **Maximize or minimize** something | **Dynamic Programming** (memoization / tabulation) |
| 8 | Find **common substring** across strings | **HashMap** or **Trie** |
| 9 | **Search or manipulate** a set of strings | **Trie** is the best structure |
| 10 | LinkedList, **no extra space** allowed | **Fast & Slow Pointer** approach |

### 9.2 Java Streams — Golden Rules
| # | Rule | Reason |
|---|---|---|
| 1 | **Never modify the source** inside a stream | Causes `ConcurrentModificationException` |
| 2 | Use `.distinct()` before `.sorted()`  | Saves sorting duplicates — cheaper |
| 3 | Use `filter()` as early as possible | Reduces elements flowing through pipeline |
| 4 | Prefer `.findFirst()` over `.collect().get(0)` | Short-circuits — stops at first match |
| 5 | Use `mapToInt/mapToDouble` for numeric ops | Avoids boxing overhead of `map()` |
| 6 | **Never use** `parallelStream()` with shared mutable state | Race conditions — use `ConcurrentHashMap` instead |
| 7 | Use `Collectors.groupingBy()` for any group-by problem | Replaces nested loops + maps |
| 8 | Use `Collectors.joining()` for string joining | Much faster than `+` concatenation in loops |
| 9 | `flatMap()` = map + flatten | Use when each element maps to a collection |
| 10 | Chain `Comparator.comparing().thenComparing()` | Multi-field sorting with no `if-else` |
| 11 | `Stream.iterate()` for infinite/generated sequences | Fibonacci, number ranges, sequences |
| 12 | Use `collectors.collectingAndThen()` to post-process | E.g., reverse a list after collecting |
| 13 | Use `Optional.map().orElse()` — **never** `.get()` without check | `.get()` on empty Optional throws exception |
| 14 | `peek()` is for debugging only — never business logic | Terminal ops may not run on all elements |
| 15 | `reduce(identity, accumulator)` for fold operations | Sum, product, max without boxing |

### 9.3 String Problems — Golden Rules
| # | Rule | Hint |
|---|---|---|
| 1 | Use `StringBuilder` for building strings in loops | `String +` in loop = O(n²), `StringBuilder` = O(n) |
| 2 | Anagram check → sort both, or use `int[26]` freq array | `Arrays.sort(a) == Arrays.sort(b)` |
| 3 | Palindrome → **two pointers** (left, right converging) | Avoids creating a reversed copy |
| 4 | First non-repeating → `LinkedHashMap` | Preserves order while counting |
| 5 | Duplicate characters → `HashSet.add()` returns `false` | `if (!seen.add(c)) duplicates.add(c)` |
| 6 | Substring search → use `String.contains()` or `indexOf()` | Don't write KMP unless asked |
| 7 | Word frequency → `Map.merge(word, 1, Integer::sum)` | Cleaner than `getOrDefault + put` |
| 8 | Reverse words → `split(" ")` + reverse array + `String.join` | Or use `Deque` as a stack |
| 9 | Remove duplicate chars preserving order | `new LinkedHashSet<>(Arrays.asList(chars))` |
| 10 | char↔int conversion → `(char) c` and `c - 'a'` | `'a'` = 97; use for freq array indexing |
| 11 | **Never** compare Strings with `==` | Always `.equals()` |
| 12 | `s.chars()` returns `IntStream` | Cast to `(char)` for Stream ops |

### 9.4 Collections — Golden Rules
| # | Rule | Why |
|---|---|---|
| 1 | **HashMap** for O(1), **TreeMap** for sorted | Don't use TreeMap when order doesn't matter (5× slower) |
| 2 | **LinkedHashMap** for insertion order + O(1) | Foundation for LRU Cache |
| 3 | **HashSet** to track seen elements in O(1) | Replaces nested loops for duplicates |
| 4 | `computeIfAbsent(key, k -> new ArrayList<>())` | Cleaner than `getOrDefault + put` |
| 5 | `Map.merge(key, 1, Integer::sum)` | Replaces 3-line map-counting code |
| 6 | Use **`Deque`** (`ArrayDeque`) instead of `Stack` | `Stack` is legacy + synchronized |
| 7 | Fail-fast iterators → never `list.remove()` inside `for-each` | Use `Iterator.remove()` or `removeIf()` |
| 8 | `Collections.unmodifiableList()` vs `List.of()` | `List.of()` throws on add/set |
| 9 | **`ConcurrentHashMap`** for multi-threaded maps | `HashMap` is not thread-safe |
| 10 | **`CopyOnWriteArrayList`** for read-heavy | Safe concurrent iteration |
| 11 | `PriorityQueue` default = min-heap | Use `Comparator.reverseOrder()` for max-heap |
| 12 | `equals()` + `hashCode()` contract | If `equals()` is overridden, override `hashCode()` |

### 9.5 Concurrency — Golden Rules
| # | Rule | Why |
|---|---|---|
| 1 | **Prefer `ReentrantLock` over `synchronized`** | Supports `tryLock`, fairness |
| 2 | **Always** call `ThreadLocal.remove()` in `finally` | Prevents stale data leak in thread pools |
| 3 | **`volatile`** = visibility only, NOT atomicity | Use `AtomicInteger` to increment |
| 4 | **Lock ordering** prevents deadlock | Acquire `lockA` before `lockB` universally |
| 5 | Use `ConcurrentHashMap` over `Collections.synchronizedMap()` | CHM uses segment-locks |
| 6 | Use **`CompletableFuture`** for async pipelines | Avoid raw `Thread` blocking |
| 7 | `parallelStream()` uses shared ForkJoinPool | Starvation risk; use custom pool |
| 8 | **Virtual Threads** (Java 21) — avoid `synchronized` | It pins the carrier thread; use `ReentrantLock` |

### 9.6 SQL Interview — Golden Rules
| # | Rule | Hint |
|---|---|---|
| 1 | **Nth highest salary** → `DENSE_RANK()` | `DENSE_RANK() OVER (ORDER BY salary DESC) = N` |
| 2 | **Duplicates** → `GROUP BY + HAVING COUNT(*) > 1` | Never `DISTINCT` to find duplicates |
| 3 | **Employees with no manager** | `LEFT JOIN + IS NULL` or `NOT IN` |
| 4 | **Running cumulative sum** | `SUM() OVER (ORDER BY ...)` |
| 5 | **Rank with gaps** → `RANK()` | **No gaps** → `DENSE_RANK()` |
| 6 | **Delete duplicates, keep one** | `DELETE WHERE id NOT IN (SELECT MIN(id) GROUP BY ...)` |
| 7 | `WHERE` filters **rows**, `HAVING` filters **groups** | `HAVING` runs after `GROUP BY` |
| 8 | **Index** columns in `WHERE`/`JOIN`/`ORDER BY` | Never index boolean columns |
| 9 | `EXPLAIN` / `EXPLAIN ANALYZE` before optimizing | Find and fix full sequential scans |
