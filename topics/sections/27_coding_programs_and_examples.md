<!-- Part of Java Learning Roadmap — Section 27 -->

## 💻 27. Coding Programs & Interview Examples

> Hands-on code problems asked in real Java backend interviews. Organized by topic.

### 🔷 A. Java 8 Streams — Most Asked Programs

#### 1. Find duplicate elements in a list
```java
List<Integer> nums = List.of(1, 2, 3, 2, 4, 3, 5);
Set<Integer> seen = new HashSet<>();
List<Integer> duplicates = nums.stream()
    .filter(n -> !seen.add(n))
    .distinct()
    .collect(Collectors.toList());
// Output: [2, 3]
```

#### 2. Find the second highest number
```java
Optional<Integer> second = nums.stream()
    .distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1)
    .findFirst();
```

#### 3. First non-repeating character in a string
```java
String input = "swiss";
Character result = input.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
    .entrySet().stream()
    .filter(e -> e.getValue() == 1)
    .map(Map.Entry::getKey)
    .findFirst()
    .orElse(null);
// Output: 'w'
```

#### 4. Count character frequency in a string
```java
String s = "hello world";
Map<Character, Long> freq = s.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
```

#### 5. Group employees by department & find max salary per dept
```java
Map<String, Optional<Employee>> maxByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment,
             Collectors.maxBy(Comparator.comparingDouble(Employee::getSalary))));

// Average salary per department
Map<String, Double> avgByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment,
             Collectors.averagingDouble(Employee::getSalary)));

// Count per department
Map<String, Long> countByDept = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
```

#### 6. Sort employees: first by name, then by marks descending
```java
employees.stream()
    .sorted(Comparator.comparing(Employee::getName)
        .thenComparing(Comparator.comparingDouble(Employee::getSalary).reversed()))
    .collect(Collectors.toList());
```

#### 7. Reverse words in a sentence
```java
String sentence = "My name is Tom";
String reversed = Arrays.stream(sentence.split(" "))
    .collect(Collectors.collectingAndThen(Collectors.toList(), list -> {
        Collections.reverse(list);
        return String.join(" ", list);
    }));
// Output: "Tom is name My"
```

#### 8. Fibonacci using Stream.iterate (Java 8)
```java
Stream.iterate(new long[]{0, 1}, f -> new long[]{f[1], f[0] + f[1]})
    .limit(10)
    .map(f -> f[0])
    .forEach(System.out::println);
// Output: 0 1 1 2 3 5 8 13 21 34
```

#### 9. Flatten a list of lists
```java
List<List<Integer>> nested = List.of(List.of(1, 2), List.of(3, 4), List.of(5));
List<Integer> flat = nested.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());
```

#### 10. Partition numbers into even and odd
```java
Map<Boolean, List<Integer>> partitioned = nums.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// true  → [2, 4]   false → [1, 3, 5]
```

---

### 🔷 B. String Programs

#### 11. Palindrome check — recursive
```java
public boolean isPalindrome(String s, int left, int right) {
    if (left >= right) return true;
    if (s.charAt(left) != s.charAt(right)) return false;
    return isPalindrome(s, left + 1, right - 1);
}
// Call: isPalindrome("racecar", 0, s.length() - 1) → true
```

#### 12. Anagram check
```java
public boolean isAnagram(String a, String b) {
    char[] ca = a.toCharArray(); char[] cb = b.toCharArray();
    Arrays.sort(ca); Arrays.sort(cb);
    return Arrays.equals(ca, cb);
}
// HashMap approach: O(n) time, O(1) space (limited alphabet)
```

#### 13. Count character occurrences
```java
Map<Character, Integer> map = new LinkedHashMap<>();
for (char c : "hello world".toCharArray())
    map.merge(c, 1, Integer::sum);
// Output: h=1, e=1, l=3, o=2, ' '=1, w=1, r=1, d=1
```

#### 14. String compression ("aaabbc" → "a3b2c1")
```java
public String compress(String s) {
    StringBuilder sb = new StringBuilder();
    int i = 0;
    while (i < s.length()) {
        char c = s.charAt(i); int count = 0;
        while (i < s.length() && s.charAt(i) == c) { i++; count++; }
        sb.append(c).append(count);
    }
    return sb.toString();
}
```

#### 15. Balanced parentheses
```java
public boolean isBalanced(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if ("({[".indexOf(c) >= 0) stack.push(c);
        else {
            if (stack.isEmpty()) return false;
            char top = stack.pop();
            if (c == ')' && top != '(') return false;
            if (c == '}' && top != '{') return false;
            if (c == ']' && top != '[') return false;
        }
    }
    return stack.isEmpty();
}
```

---

### 🔷 C. Collections & Data Structures

#### 16. LRU Cache using LinkedHashMap
```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    LRUCache(int capacity) {
        super(capacity, 0.75f, true); // accessOrder = true
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}
```

#### 17. Remove duplicates from a list (preserve order)
```java
List<Integer> unique = new ArrayList<>(new LinkedHashSet<>(list));
// Or with streams:
List<Integer> unique2 = list.stream().distinct().collect(Collectors.toList());
```

#### 18. Sort a Map by value
```java
Map<String, Integer> sorted = map.entrySet().stream()
    .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
    .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
             (e1, e2) -> e1, LinkedHashMap::new));
```

#### 19. Find common elements between two lists
```java
List<Integer> common = list1.stream()
    .filter(new HashSet<>(list2)::contains)
    .collect(Collectors.toList());
```

#### 20. Comparable vs Comparator
```java
// Comparable — natural order INSIDE the class
class Person implements Comparable<Person> {
    public int compareTo(Person o) { return this.age - o.age; }
}

// Comparator — external/multiple sort orders
list.sort(Comparator.comparing(Person::getName)
    .thenComparing(Comparator.comparingInt(Person::getAge).reversed()));
```

---

### 🔷 D. DSA Classics

#### 21. Two Sum — O(n) with HashMap
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>(); // value → index
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement))
            return new int[]{map.get(complement), i};
        map.put(nums[i], i);
    }
    return new int[]{};
}
// Time: O(n) | Space: O(n)
```

#### 22. Three Sum — O(n²) with sort + two pointers
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum == 0) { result.add(List.of(nums[i], nums[left++], nums[right--])); }
            else if (sum < 0) left++;
            else right--;
        }
    }
    return result;
}
```

#### 23. Binary Search
```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2; // avoids overflow
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1; // not found
}
```

#### 24. Find missing number (XOR trick)
```java
public int missingNumber(int[] nums) {
    int xor = nums.length;
    for (int i = 0; i < nums.length; i++)
        xor ^= i ^ nums[i];
    return xor;
}
// Alternative: n*(n+1)/2 - Arrays.stream(nums).sum()
```

#### 25. Sliding window — maximum subarray sum of size k
```java
public int maxSum(int[] arr, int k) {
    int windowSum = 0, maxSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    maxSum = windowSum;
    for (int i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

---

### 🔷 E. Concurrency Programs

#### 26. Deadlock — example and fix
```java
// DEADLOCK: Thread1 locks A→B, Thread2 locks B→A
synchronized(lockA) { synchronized(lockB) { /* Thread 1 */ } }
synchronized(lockB) { synchronized(lockA) { /* Thread 2 */ } }

// FIX: Always acquire locks in the SAME order
synchronized(lockA) { synchronized(lockB) { /* both threads */ } }

// Or use tryLock with timeout (no indefinite blocking)
if (lockA.tryLock(50, MILLISECONDS) && lockB.tryLock(50, MILLISECONDS)) {
    try { doWork(); } finally { lockA.unlock(); lockB.unlock(); }
}
```

#### 27. ThreadLocal — proper usage with cleanup
```java
static ThreadLocal<MyObject> tl = new ThreadLocal<>();

// BAD: no cleanup → memory leak in thread pools
tl.set(new MyObject()); doWork();

// GOOD: always remove in finally
try {
    tl.set(new MyObject());
    doWork();
} finally {
    tl.remove(); // critical — prevents memory leak
}
```

#### 28. Virtual Threads (Java 21) — 1 million tasks
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 1_000_000).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1)); // blocks cheaply
            return i;
        })
    );
} // 1 million virtual threads, NOT 1 million OS threads
```

---

### 🔷 F. Spring Boot REST API Programs

#### 29. REST controller — GET by ID and search by name
```java
@RestController
@RequestMapping("/api/persons")
public class PersonController {
    @Autowired private PersonRepository repo;

    @GetMapping("/{id}")
    public ResponseEntity<Person> getById(@PathVariable Long id) {
        return repo.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/search")
    public List<Person> getByName(@RequestParam String name) {
        return repo.findByNameContainingIgnoreCase(name);
    }
}
```

#### 30. Immutable class using Java 16+ Record
```java
public record Employee(String name, List<String> roles) {
    public Employee {
        if (name == null || name.isBlank())
            throw new IllegalArgumentException("Name required");
        roles = List.copyOf(roles); // defensive copy — immutable
    }
}
// Usage:
Employee e = new Employee("Alice", List.of("Dev", "Lead"));
e.roles().add("PM"); // throws UnsupportedOperationException ✅
```

#### 31. Factory Pattern with switch expression (Java 17+)
```java
class ShapeFactory {
    public Shape get(String type) {
        return switch (type) {
            case "CIRCLE"   -> new Circle();
            case "RECTANGLE"-> new Rectangle();
            default         -> throw new IllegalArgumentException("Unknown: " + type);
        };
    }
}
```

---

### 🔷 G. Golden Rules for Coding Problems

---

#### 🏆 G1. DSA Pattern Recognition — 10 Rules

> Hear the problem → recognize the pattern → pick the right tool. Every time.

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

---

#### ⚡ G2. Java Streams — Golden Rules

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

---

#### 🔤 G3. String Problems — Golden Rules

| # | Rule | Example / Hint |
|---|---|---|
| 1 | Use `StringBuilder` for building strings in loops | `String +` in loop = O(n²), `StringBuilder` = O(n) |
| 2 | Anagram check → sort both, or use `int[26]` freq array | `Arrays.sort(a) == Arrays.sort(b)` |
| 3 | Palindrome → **two pointers** (left, right converging) | Avoids creating a reversed copy |
| 4 | First non-repeating → `LinkedHashMap` (insertion-order + count) | Preserves order while counting |
| 5 | Duplicate characters → `HashSet.add()` returns `false` if duplicate | `if (!seen.add(c)) duplicates.add(c)` |
| 6 | Substring search → use `String.contains()` or `indexOf()` | Don't write KMP for interviews unless asked |
| 7 | Word frequency → `Map.merge(word, 1, Integer::sum)` | Cleaner than `getOrDefault + put` |
| 8 | Reverse words → `split(" ")` + reverse array + `String.join` | Or use `Deque` as a stack |
| 9 | Remove duplicate chars preserving order → `LinkedHashSet` | `new LinkedHashSet<>(Arrays.asList(chars))` |
| 10 | char↔int conversion → `(char) c` and `c - 'a'` for indexing | `'a'` = 97; use for freq array indexing |
| 11 | **Never** compare Strings with `==` — always `.equals()` | `==` checks reference, not content |
| 12 | `s.chars()` returns `IntStream` — cast to `(char)` for Stream ops | `s.chars().mapToObj(c -> (char) c)` |

---

#### 📦 G4. Collections — Golden Rules

| # | Rule | Why |
|---|---|---|
| 1 | **HashMap** for O(1) lookup, **TreeMap** for sorted order | Don't use TreeMap when order doesn't matter — 5× slower |
| 2 | **LinkedHashMap** when you need insertion order + O(1) | Foundation for LRU Cache |
| 3 | **HashSet** to track seen elements in O(1) | Replaces nested loops for duplicates |
| 4 | `computeIfAbsent(key, k -> new ArrayList<>())` for grouping | Cleaner than `getOrDefault + put` |
| 5 | `Map.merge(key, 1, Integer::sum)` for counting | Replaces 3-line `getOrDefault` pattern |
| 6 | Use **`Deque`** (`ArrayDeque`) instead of `Stack` | `Stack` is legacy + synchronized |
| 7 | Fail-fast iterators → never `list.remove()` inside `for-each` | Use `Iterator.remove()` or `removeIf()` |
| 8 | `Collections.unmodifiableList()` vs `List.of()` | `List.of()` throws on add/set, `unmodifiable` wraps existing |
| 9 | **`ConcurrentHashMap`** for multi-threaded maps | `HashMap` is not thread-safe; `Hashtable` is deprecated |
| 10 | **`CopyOnWriteArrayList`** for read-heavy, write-rare concurrent lists | Safe iteration; writes create a full copy |
| 11 | `PriorityQueue` default = min-heap; reverse for max-heap | `new PriorityQueue<>(Comparator.reverseOrder())` |
| 12 | `equals()` + `hashCode()` must be consistent for Map keys | If `equals()` is overridden, override `hashCode()` too |

---

#### 🔀 G5. Concurrency — Golden Rules

| # | Rule | Why |
|---|---|---|
| 1 | **Prefer `ReentrantLock` over `synchronized`** for complex locking | Supports `tryLock`, `lockInterruptibly`, fairness |
| 2 | **Always** call `ThreadLocal.remove()` in `finally` | Thread pools reuse threads → stale data leak |
| 3 | **`volatile`** = visibility only, NOT atomicity | Use `AtomicInteger` for atomic increments |
| 4 | **Lock ordering** prevents deadlock | Always acquire `lockA` before `lockB` in all threads |
| 5 | Use `ConcurrentHashMap` — never `Collections.synchronizedMap()` | `synchronizedMap` locks entire map; CHM is segment-locked |
| 6 | Use **`CompletableFuture`** for async pipelines | Avoid raw `Thread` or legacy `Future.get()` blocking |
| 7 | `parallelStream()` uses **ForkJoinPool** (shared) | Can starve other tasks; use custom pool for isolation |
| 8 | **Virtual Threads** (Java 21) — never use `synchronized` inside | Pins the carrier thread; use `ReentrantLock` instead |
| 9 | `CountDownLatch` = wait for N events (one-time); `CyclicBarrier` = N threads meet repeatedly | Choose based on reuse need |
| 10 | Design stateless services whenever possible | No shared state = no concurrency bugs |

---

#### 🗄️ G6. SQL Interview — Golden Rules

| # | Rule | Hint |
|---|---|---|
| 1 | **Nth highest salary** → `DENSE_RANK()` or subquery with `LIMIT OFFSET` | `DENSE_RANK() OVER (ORDER BY salary DESC) = N` |
| 2 | **Duplicates** → `GROUP BY + HAVING COUNT(*) > 1` | Never `DISTINCT` to find duplicates |
| 3 | **Find employees with no manager** → `LEFT JOIN + IS NULL` | Or `NOT IN (SELECT manager_id ...)` |
| 4 | **Running total / cumulative sum** → `SUM() OVER (ORDER BY ...)` | Window function, not grouped |
| 5 | **Rank with gaps** → `RANK()`; **no gaps** → `DENSE_RANK()` | `ROW_NUMBER()` = always unique |
| 6 | **Delete duplicates, keep one** → `DELETE WHERE id NOT IN (SELECT MIN(id) GROUP BY ...)` | Use CTE for clarity |
| 7 | **Self join** for hierarchical data | `e1 JOIN e2 ON e1.manager_id = e2.id` |
| 8 | `WHERE` filters **rows**; `HAVING` filters **groups** | `HAVING` runs after `GROUP BY` |
| 9 | **Index** on columns used in `WHERE`, `JOIN`, `ORDER BY` | Never index low-cardinality columns (like boolean) |
| 10 | `EXPLAIN` / `EXPLAIN ANALYZE` before optimizing | See the query plan — find seq scans to fix |



### 🔷 H. Top 50 Coding Programs — Quick Reference List (Java 8+)

> Practice these in order. All solvable with Streams + Collections.

| # | Problem | Key API/Pattern |
|---|---|---|
| 1 | Find duplicates in a list | `filter(!seen.add(n))` |
| 2 | Remove duplicates | `.distinct()` or `LinkedHashSet` |
| 3 | First non-repeating character | `groupingBy` + `LinkedHashMap` + `counting()` |
| 4 | Frequency of each character | `chars().mapToObj().groupingBy()` |
| 5 | Reverse a string | `new StringBuilder(s).reverse()` |
| 6 | Sort list of integers | `.sorted()` |
| 7 | Sort employees by salary | `Comparator.comparingDouble()` |
| 8 | Second highest number | `.distinct().sorted(reversed).skip(1).findFirst()` |
| 9 | Filter even numbers | `.filter(n -> n % 2 == 0)` |
| 10 | Filter odd numbers | `.filter(n -> n % 2 != 0)` |
| 11 | Convert list to uppercase | `.map(String::toUpperCase)` |
| 12 | Flatten list of lists | `.flatMap(Collection::stream)` |
| 13 | Join strings with delimiter | `Collectors.joining(", ")` |
| 14 | Find longest string | `.max(Comparator.comparingInt(String::length))` |
| 15 | Group by department | `Collectors.groupingBy(Employee::getDept)` |
| 16 | Count per department | `groupingBy + counting()` |
| 17 | Max salary per department | `groupingBy + maxBy()` |
| 18 | Avg salary per department | `groupingBy + averagingDouble()` |
| 19 | Partition even/odd | `Collectors.partitioningBy(n -> n % 2 == 0)` |
| 20 | Top 3 earners | `.sorted(reversed).limit(3)` |
| 21 | Calculate sum | `.mapToInt(i -> i).sum()` or `reduce(0, Integer::sum)` |
| 22 | Check contains duplicates | `stream().count() != distinct().count()` |
| 23 | Find common elements | `.filter(new HashSet<>(list2)::contains)` |
| 24 | Convert list to map | `Collectors.toMap(key, value)` |
| 25 | Sort map by value | `.sorted(Map.Entry.comparingByValue())` |
| 26 | Filter nulls | `.filter(Objects::nonNull)` |
| 27 | Count words in sentence | `s.trim().split("\\s+").length` |
| 28 | Reverse words in sentence | `Stream.of(split).collect + Collections.reverse` |
| 29 | Group strings by length | `groupingBy(String::length)` |
| 30 | Merge two lists | `Stream.concat(l1.stream(), l2.stream())` |
| 31 | Find missing number | XOR trick or `n*(n+1)/2 - sum` |
| 32 | Two Sum | `HashMap<value, index>` — O(n) |
| 33 | Binary Search | Left/right pointers — O(log n) |
| 34 | Palindrome check | Two-pointer or recursive |
| 35 | Anagram check | `Arrays.sort` both or `HashMap` frequency |
| 36 | Balanced parentheses | Stack-based |
| 37 | LRU Cache | `LinkedHashMap(capacity, 0.75f, true)` |
| 38 | Fibonacci (Stream) | `Stream.iterate(new long[]{0,1}, ...)` |
| 39 | Sliding window max sum | Single-pass O(n) |
| 40 | String compression | Pointer-based counter |
| 41 | Deadlock example + fix | Lock ordering / `tryLock` |
| 42 | Thread-safe Singleton | `volatile` + double-checked locking or Enum |
| 43 | Immutable class | `final` class + `final` fields + `List.copyOf()` |
| 44 | Custom Comparator chaining | `comparing().thenComparing()` |
| 45 | Parallel stream pitfall | Shared mutable state → `ConcurrentHashMap` |
| 46 | `Optional` chaining | `ofNullable().map().orElse()` |
| 47 | `CompletableFuture` chain | `supplyAsync().thenApply().exceptionally()` |
| 48 | Virtual Threads (Java 21) | `Executors.newVirtualThreadPerTaskExecutor()` |
| 49 | Record as DTO | `record UserDTO(String name, String email) {}` |
| 50 | Spring Boot REST GET+SEARCH | `@GetMapping + ResponseEntity + @RequestParam` |

---
