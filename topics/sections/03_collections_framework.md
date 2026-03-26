<!-- Part of Java Learning Roadmap — Section 3 -->

## 📦 3. Java Collections Framework

- Arrays vs Collections
- **List**: `ArrayList`, `LinkedList`, `Vector`, `Stack`
  - `ArrayList` vs `LinkedList` — performance tradeoffs
- **Set**: `HashSet`, `LinkedHashSet`, `TreeSet`
- **Map**: `HashMap`, `LinkedHashMap`, `TreeMap`, `Hashtable`
  - **HashMap Internals**
    - Hashing, buckets, collision handling
    - Linked list → Red-Black Tree at threshold 8 (capacity ≥ 64)
    - Load factor (default 0.75), resizing/rehashing
    - `equals()` + `hashCode()` contract for keys
  - `LinkedHashMap` — insertion/access order
  - `TreeMap` — natural ordering, `Comparator`
- **Queue**: `PriorityQueue`, `Deque`, `ArrayDeque`
  - `BlockingQueue` — `LinkedBlockingQueue`, `ArrayBlockingQueue`
- **Concurrent Collections**
  - `ConcurrentHashMap` — segment locking / CAS, no null keys
  - `CopyOnWriteArrayList` — fail-safe iteration
  - `ConcurrentLinkedQueue`
- **Iterators**
  - Fail-Fast (`ConcurrentModificationException`) vs Fail-Safe (copy-on-read)
  - `Iterator` vs `ListIterator`
- Utility Classes
  - `Collections` — `sort()`, `synchronizedList()`, `unmodifiableList()`, `emptyList()`
  - `Arrays` — `sort()`, `binarySearch()`, `copyOf()`
- Special Maps
  - `WeakHashMap` — GC-eligible keys
  - `IdentityHashMap` — reference equality
- **LRU Cache** — implemented with `LinkedHashMap` (`accessOrder=true`)

---
