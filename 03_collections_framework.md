<!-- Part of Java Learning Roadmap — Section 3 -->

# 📦 3. Java Collections Framework

---

## 1. Definition

The **Java Collections Framework (JCF)** is a unified architecture representing and manipulating collections of objects. It provides standard `Interfaces` (List, Set, Map, Queue), `Implementations` (ArrayList, HashSet, HashMap), and `Algorithms` (Collections.sort, binarySearch) to reduce programming effort and increase performance.

### 1.1 Hierarchy Concept

**Core Idea:**
A unified contract that separates how you use data (`Interfaces`) from how the computer stores it (`Implementations`).

**Deep Dive:**
The hierarchy is split between the `Collection` branch (individual items) and the `Map` branch (pairs). `Map` is kept separate because the logic of "mapping" a key to a value is fundamentally different from a simple list of items.

**Advanced Insight:**
At the JVM level, collections only store object references (pointers). This means primitives like `int` are **autoboxed** into `Integer` objects, which consumes significantly more memory and header space.

**Production Tip:**
Always "Program to the Interface" (`List<String> s = new ArrayList<>()`). This allows you to swap implementations later for performance or testing without changing the rest of your app.

---

## 2. Why It Exists

Before Java 1.2, Java used ad-hoc classes like `Vector`, `Stack`, `Hashtable`, and `Properties`. These had no common interface, making it hard to switch between them.
*   **Interoperability:** High-level APIs can accept `List<T>` and not care if it's an `ArrayList` or `LinkedList`.
*   **Reusability:** Eliminates the need to write custom sorting, searching, or dynamic array logic.
*   **Performance:** Implementations are highly optimized (e.g., Java 8 HashMap uses Red-Black trees for collisions).

---

## 3. How It Works Internally

### 3.1 HashMap Internals (The most asked interview topic)

**Core Idea:**
An array of "Buckets" where keys are placed based on their calculated math ID (Hash).

1.  **Buckets:** An array of `Node<K,V>` objects. Default capacity is 16.
2.  **Hashing:** When `put(K, V)` is called, Java calculates `hash = (key.hashCode()) ^ (h >>> 16)` and finds the bucket index using `(n - 1) & hash`.
3.  **Collisions:** If two keys land in the same bucket, they form a Linked List.
4.  **Treeification (Java 8+):** If a bucket's linked list length exceeds `TREEIFY_THRESHOLD` (8), it transforms into a **Red-Black Tree** to improve worst-case search time from `O(n)` to `O(log n)`.
5.  **Rehashing:** When the map hits its **Load Factor** (default 0.75, meaning 12 items out of 16), it doubles the array size and redistributes all nodes.

**Deep Dive:**
HashMap uses **Dynamic Resizing**. Every time it resizes, it must "re-hash" every single item to its new position. This is expensive ($O(n)$ during resize).

**Advanced Insight:**
Why the `^ (h >>> 16)` XOR shift? It spreads the "entropy" of the hash code to the lower bits. Since most hash maps are small, only the low bits are used for indexing. Shifting the high bits down ensures the high-order data isn't ignored, reducing collisions.

**Pitfall:**
**Mutable Keys.** If you change an object's field *after* using it as a key in a HashMap, its `hashCode()` might change. You will never be able to find that item again; it's lost in the wrong bucket.

**Production Tip:**
If you know you'll store 1000 items, initialize the map with a capacity of `1334` (taking the 0.75 load factor into account) to avoid multiple expensive resizing operations.

**Interview Trap:**
"Can HashMap have multiple null keys?" **No.** Only one null key (it always goes to bucket 0). Trying to add a second null key just overwrites the first one.

### 3.2 List Internals
*   **ArrayList:** Backed by dynamically resizing arrays. Expanding adds 50% capacity (`newCapacity = oldCapacity + (oldCapacity >> 1)`). Fast read `O(1)`, slow insert `O(n)`.
*   **LinkedList:** Backed by a doubly-linked list. Each node has `prev` and `next` pointers. Fast insert at ends `O(1)`, slow read `O(n)`.

### 3.3 Set Internals
*   **HashSet:** Literally just a wrapper around a `HashMap`. The elements you add are stored as keys in the map, and a dummy `Object` (called `PRESENT`) is used as the value.

### 3.4 Concurrent Collections & Fail-Fast vs Fail-Safe

**Core Idea:**
"Fail-Fast" stops everything when it detects trouble; "Fail-Safe" handles trouble gracefully by working on a copy or using clever locking.

*   **Fail-Fast (ArrayList, HashMap):** If a thread modifies the collection structurally while an Iterator is iterating over it, it throws `ConcurrentModificationException`. It tracks this using a `modCount` variable.
*   **Fail-Safe (ConcurrentHashMap, CopyOnWriteArrayList):** Iterate over a clone/snapshot of the collection. Modifications don't affect the running traversal. Safe for multi-threading.

**Deep Dive:**
`ConcurrentHashMap` doesn't just lock the whole map. It uses **Bucket-Level Synchronization**. In Java 8+, it uses CAS (Compare-And-Swap) for the first node and `synchronized` only when multiple threads hit the *exact same* bucket.

**Advanced Insight:**
`CopyOnWriteArrayList` is a **Read-Heavy** optimization. Every write operation literally creates a brand new copy of the internal array. This makes reads $O(1)$ and thread-safe without locks, but makes writes extremely heavy.

**Production Tip:**
Use `ConcurrentHashMap` for caches and multi-threaded shared state. Avoid using `Hashtable` or `Collections.synchronizedMap()` as they lock the *entire* map, which kills performance at scale.

---

## 4. Code Examples

### 4.1 LRU Cache using `LinkedHashMap`
`LinkedHashMap` can effortlessly implement an LRU (Least Recently Used) cache by overriding `removeEldestEntry`.

```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;

    public LRUCache(int capacity) {
        // args: initialCapacity, loadFactor, accessOrder (true = ordered by last access)
        super(capacity, 0.75f, true); 
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity; // Remove oldest if limit exceeded
    }
}
```

### 4.2 Removing elements safely during iteration
```java
List<String> list = new ArrayList<>(List.of("A", "B", "C"));

// BAD: Throws ConcurrentModificationException
for(String s : list) {
    if(s.equals("B")) list.remove(s); 
}

// GOOD: Using Iterator.remove()
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if (it.next().equals("B")) {
        it.remove(); 
    }
}

// BETTER: Java 8 removeIf
list.removeIf(s -> s.equals("B"));
```

### 4.3 CopyOnWriteArrayList (Write-rare, read-heavy)
```java
// Thread-safe list. Every write (add/set/remove) clones the underlying array.
List<String> threadSafeList = new CopyOnWriteArrayList<>();
threadSafeList.add("Config1");

// Safe to iterate while other threads modify, because iterator uses the snapshot.
for (String config : threadSafeList) {
    System.out.println(config);
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `Hashtable` and `HashMap`? | `Hashtable` is legacy, synchronized (slow), does not allow `null` keys/values. `HashMap` is not thread-safe (fast), allows ONE `null` key and multiple `null` values. |
| Difference between `HashMap` and `ConcurrentHashMap`? | `CHM` is thread-safe. Java 8+ `CHM` uses CAS and locks only the specific bucket (node) being updated, not the whole map. `CHM` does NOT allow `null` keys or values. |
| Can you store `null` in a `TreeSet`? | **No**. `TreeSet` uses `compareTo()`. Comparing `null` throws `NullPointerException`. |
| What happens if two keys have the same `hashCode`? | They hash to the same bucket (Collision). `HashMap` will then use `.equals()` to check if the keys are actually identical. If false, it appends to the linked list/tree in that bucket. |
| Array vs ArrayList? | Arrays are fixed size, hold primitives or objects. ArrayLists are dynamic, hold only objects (primitives are autoboxed). |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Modifying a collection inside a `for-each` loop | `ConcurrentModificationException` | Use `Iterator.remove()` or `collection.removeIf()` |
| Overriding `equals()` but not `hashCode()` | Objects equal by logic will hash to different buckets. `HashSet` and `HashMap` will fail to find them. | Generate both `equals` and `hashCode` based on identical fields. |
| Using `LinkedList` for random access | `list.get(5000)` takes O(N) time because it traverses node by node. | Always use `ArrayList` unless doing heavy O(1) head/tail insertions. |
| Synchronizing collections with `Collections.synchronizedList()` | Locks the entire list for every operation; poor concurrency scale. | Use `CopyOnWriteArrayList` or `ConcurrentHashMap` for high-concurrency needs. |

---

## 7. Real-World Usage

| Structure | Where it shows up |
|---|---|
| **`HashMap`** | In-memory caching, indexing records by ID, frequency counting. |
| **`LinkedHashMap`** | LRU Caches (e.g., caching recent user sessions or images). |
| **`HashSet`** | Extracting unique items (e.g., getting a list of unique tags from posts). |
| **`TreeSet`** | Keeping a leaderboard or maintaining a naturally sorted list of active jobs. |
| **`PriorityQueue`** | Job scheduling systems, implementing Dijkstra's algorithm, finding Top-K elements. |
| **`CopyOnWriteArrayList`** | Storing Event Listeners or application configurations where reads happen 99% of the time. |

---

## 8. Practice Tasks

1.  **Word Counter:** Write a program that takes a text string, removes punctuation, and uses a `HashMap` to output the frequency of each word.
2.  **Sort complex objects:** Create an `Employee` class. Store them in a `List`. Sort the list using `Collections.sort()` and a custom `Comparator` (sort by Salary descending, then Name ascending).
3.  **Implement a custom LinkedList:** Build a `SinglyLinkedList` with `add(val)`, `remove(val)`, and `reverse()` methods.
4.  **LRU Cache simulation:** Instantiate the `LRUCache` from section 4.1. Add 5 items, get item 1, add a 6th item. Print the map and verify item 2 was evicted, not item 1.

---

## 9. Quick Revision

### Time Complexity (Big O)
| Collection | Add | Remove | Get / Contains | Notes |
|---|---|---|---|---|
| **ArrayList** | O(1) *amortized* | O(N) | O(1) / O(N) | Fast reads, slow shifting |
| **LinkedList** | O(1) | O(1) *if pointer* | O(N) / O(N) | Fast head/tail insertions |
| **HashSet/Map** | O(1) | O(1) | O(1) | Backed by hash table |
| **TreeSet/Map** | O(log N) | O(log N) | O(log N) | Backed by Red-Black Tree |

### Summary
*   **Iterable -> Collection -> List / Set / Queue**
*   **List:** Ordered, duplicates ok. Use `ArrayList` 99% of the time.
*   **Set:** Unordered, unique. `HashSet` (fastest), `TreeSet` (sorted), `LinkedHashSet` (insertion order).
*   **Map:** K-V pairs. `HashMap` (default), `LinkedHashMap` (LRU), `ConcurrentHashMap` (thread-safe).
*   **HashMap internal:** Bucket array → Linked List node → Red-Black tree if nodes > 8.
*   **equals() & hashCode():** If `a.equals(b)` is true, `a.hashCode() == b.hashCode()` MUST be true.
