<!-- Part of Java Learning Roadmap — Section 27 -->

# 27. Coding Programs & Interview Examples

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

### 4.2 Master Coding Roadmap: Individual Interview Solutions

This section expands the core utility patterns into granular, one-by-one interview answers. Each problem is designed to test syntax fluency and architectural maturity.

---

#### 1. Find Duplicates in a List

**Question:**
Given a list of integers, return all duplicate elements.

**Approach:**
*   Use a `Set` to track seen elements.
*   `Set.add()` returns `false` if the element already exists.
*   Filter for elements where `add()` fails.

**Code:**
```java
List<Integer> findDuplicates(List<Integer> list) {
    Set<Integer> seen = new HashSet<>();
    return list.stream()
            .filter(n -> !seen.add(n))
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `Set.add()` returns `false` if the element already exists in the set.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Use `groupingBy()` and filter where `count > 1`.

**Pitfall:**
*   Using `List.contains()` inside a filter, which makes the operation **O(n²)**.

**Interview Insight:**
*   Tests understanding of `Set` internal behavior and `Stream` filtering.

---

#### 2. Remove Duplicates from a List

**Question:**
Return a list with all duplicate elements removed while optionally maintaining order.

**Approach:**
*   Use the `.distinct()` terminal operation.
*   Internally, `distinct()` uses a `HashSet` to filter duplicates.

**Code:**
```java
List<Integer> removeDuplicates(List<Integer> list) {
    return list.stream()
            .distinct()
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `distinct()` is a stateful intermediate operation that ensures output uniqueness.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Pass the list to a `LinkedHashSet` constructor.

**Pitfall:**
*   Using `HashSet` constructor if insertion order must be preserved.

**Interview Insight:**
*   Tests knowledge of `Stream` stateful operations and uniqueness.

---

#### 3. First Non-Repeating Character in a String

**Question:**
Find the first character in a string that does not repeat.

**Approach:**
*   Use `LinkedHashMap` to store counts while preserving character order.
*   Filter the map for the first entry with a count of 1.

**Code:**
```java
Character firstUnique(String s) {
    return s.chars().mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new, Collectors.counting()))
            .entrySet().stream()
            .filter(e -> e.getValue() == 1)
            .map(Map.Entry::getKey)
            .findFirst().orElse(null);
}
```

**Explanation:**
*   `LinkedHashMap` is mandatory; standard `HashMap` would return a random unique character.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Use a frequency array `int[256]` for ASCII strings (O(1) space).

**Pitfall:**
*   Using `HashMap` instead of `LinkedHashMap`, which fails to return the *first* match.

**Interview Insight:**
*   Tests knowledge of different `Map` implementations and their properties.

---

#### 4. Count Element Frequency in a List

**Question:**
Given a list, return a map showing how many times each element appears.

**Approach:**
*   Use `Collectors.groupingBy()` with the `counting()` downstream collector.

**Code:**
```java
Map<Integer, Long> getCounts(List<Integer> list) {
    return list.stream()
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
}
```

**Explanation:**
*   `groupingBy` organizes data by key, and `counting()` tallies the occurrences.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Use `Map.merge(key, 1, Integer::sum)` in a loop.

**Pitfall:**
*   Returning a `Map<Integer, Integer>` instead of `Long`, which is the return type of `counting()`.

**Interview Insight:**
*   Tests if the candidate knows how to use downstream collectors efficiently.

---

#### 5. Sort a List in Descending Order

**Question:**
Sort a list of integers from highest to lowest.

**Approach:**
*   Use `.sorted()` with `Comparator.reverseOrder()`.

**Code:**
```java
List<Integer> sortDescending(List<Integer> list) {
    return list.stream()
            .sorted(Comparator.reverseOrder())
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `sorted()` is a stateful operation that compares elements according to the provided comparator.

**Complexity:**
*   Time: **O(n log n)**
*   Space: **O(n)**

**Alternative:**
*   `list.sort(Collections.reverseOrder())` if modifying the original list is allowed.

**Pitfall:**
*   Attempting to sort a stream of primitives (like `IntStream`) without an explicit comparator.

**Interview Insight:**
*   Tests basic sorting and `Comparator` usage.

---

#### 6. Find the Second Highest Unique Number

**Question:**
Find the second-highest unique value in an integer list.

**Approach:**
*   Get distinct elements, sort descending, skip the first (highest), and take the next.

**Code:**
```java
Integer secondHighest(List<Integer> list) {
    return list.stream()
            .distinct()
            .sorted(Comparator.reverseOrder())
            .skip(1)
            .findFirst().orElse(null);
}
```

**Explanation:**
*   `distinct()` ensures we don't pick the same highest value twice if duplicates exist.

**Complexity:**
*   Time: **O(n log n)**
*   Space: **O(n)**

**Alternative:**
*   A single-pass loop tracking `max` and `secondMax` (O(n) time, O(1) space).

**Pitfall:**
*   Forgetting `distinct()`. If input is `[10, 10, 9]`, the answer should be 9. Without `distinct()`, `skip(1)` gives 10.

**Interview Insight:**
*   Tests deep understanding of `distinct()` and `skip()` behavior.

---

#### 7. Filter Strings by Length

**Question:**
From a list of strings, return only those whose length is greater than 5.

**Approach:**
*   Use `.filter()` with a length condition.

**Code:**
```java
List<String> filterLongStrings(List<String> list) {
    return list.stream()
            .filter(s -> s.length() > 5)
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `filter` allows only elements that meet the boolean criteria to pass through.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   `removeIf()` for in-place modification.

**Pitfall:**
*   Failing to handle `null` strings in the list (can cause `NPE`).

**Interview Insight:**
*   Basic stream filtering test.

---

#### 8. Convert List of Strings to Uppercase

**Question:**
Convert all strings in a list to uppercase.

**Approach:**
*   Use `.map()` to apply the transformation.

**Code:**
```java
List<String> toUpper(List<String> list) {
    return list.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `map` transforms each element in the stream to a new form.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   `replaceAll(String::toUpperCase)` for in-place modification.

**Pitfall:**
*   Modifying the original objects if they were mutable (doesn't apply to Strings as they are immutable).

**Interview Insight:**
*   Basic functional mapping test.

---

#### 9. Sum of All Integers (Performance Mode)

**Question:**
Calculate the total sum of a list of integers.

**Approach:**
*   Convert to an `IntStream` using `mapToInt` to avoid wrapper boxing overhead.

**Code:**
```java
int calculateSum(List<Integer> list) {
    return list.stream()
            .mapToInt(Integer::intValue)
            .sum();
}
```

**Explanation:**
*   `mapToInt` converts `Stream<Integer>` to `IntStream`, which has primitive optimizations.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)** (for the sum itself)

**Alternative:**
*   `reduce(0, Integer::sum)` — acceptable but slightly slower due to boxing.

**Pitfall:**
*   Using `map()` + `reduce()` for very large lists, resulting in excessive object allocations.

**Interview Insight:**
*   Tests knowledge of primitive specialized streams (`IntStream`, `LongStream`).

---

#### 10. Average of a List of Numbers

**Question:**
Calculate the mathematical average of a list of integers.

**Approach:**
*   Use `mapToInt().average()`, which returns an `OptionalDouble`.

**Code:**
```java
double calculateAverage(List<Integer> list) {
    return list.stream()
            .mapToInt(i -> i)
            .average()
            .orElse(0.0);
}
```

**Explanation:**
*   `average()` returns an optional because the list might be empty.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)**

**Alternative:**
*   Calculate `sum / size` manually.

**Pitfall:**
*   Division by zero if you calculate manually on an empty list. `Optional` handles this safely.

**Interview Insight:**
*   Tests handling of return types and numeric safety.

---

#### 11. Find Max and Min in a List

**Question:**
Find the maximum and minimum values in a list of integers.

**Approach:**
*   Use `stream().max()` and `stream().min()` with `Comparator.naturalOrder()`.

**Code:**
```java
int findMax(List<Integer> list) {
    return list.stream().max(Comparator.naturalOrder()).orElse(0);
}

int findMin(List<Integer> list) {
    return list.stream().min(Comparator.naturalOrder()).orElse(0);
}
```

**Explanation:**
*   `max()` and `min()` are reduction operations that return an `Optional`.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)**

**Alternative:**
*   Use `IntSummaryStatistics` to get count, sum, min, max, and average in a single pass.

**Pitfall:**
*   Calling `.get()` on an empty list's Optional without a check or `orElse`.

**Interview Insight:**
*   Tests knowledge of reduction and `Optional` handling.

---

#### 12. Flatten a Nested List (flatMap)

**Question:**
Convert a `List<List<String>>` into a single flat `List<String>`.

**Approach:**
*   Use `.flatMap(List::stream)` to merge sub-streams.

**Code:**
```java
List<String> flattenList(List<List<String>> nested) {
    return nested.stream()
            .flatMap(List::stream)
            .collect(Collectors.toList());
}
```

**Explanation:**
*   `flatMap` takes each element (a list), converts it to a stream, and flattens all resulting streams into one.

**Complexity:**
*   Time: **O(n)** (where n is total elements)
*   Space: **O(n)**

**Alternative:**
*   Nested for-loops with `addAll()`.

**Pitfall:**
*   Using `map()` instead of `flatMap()`, which results in a `Stream<Stream<String>>`.

**Interview Insight:**
*   A core functional programming concept often tested in data processing roles.

---

#### 13. Join Strings with a Delimiter

**Question:**
Concatenate a list of strings using a comma (`,`) as a separator.

**Approach:**
*   Use `Collectors.joining(",")`.

**Code:**
```java
String joinStrings(List<String> list) {
    return list.stream()
            .collect(Collectors.joining(", "));
}
```

**Explanation:**
*   `Collectors.joining()` efficiently builds the string using a `StringBuilder` internally.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   `String.join(", ", list)`.

**Pitfall:**
*   Using `+` concatenation inside a `forEach` loop, which is **O(n²)** due to string immutability.

**Interview Insight:**
*   Tests knowledge of efficient String manipulation.

---

#### 14. Find the Longest String in a List

**Question:**
Return the string with the highest number of characters from a list.

**Approach:**
*   Use `.max()` with a comparator comparing lengths.

**Code:**
```java
String findLongest(List<String> list) {
    return list.stream()
            .max(Comparator.comparingInt(String::length))
            .orElse("");
}
```

**Explanation:**
*   `Comparator.comparingInt` provides a clean way to define the comparison logic based on a property.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)**

**Alternative:**
*   Sort by length descending and take the first element (slower, O(n log n)).

**Pitfall:**
*   Not handling the case where multiple strings have the same maximum length (logic returns the first one found).

**Interview Insight:**
*   Tests property-based comparison skills.

---

#### 15. Group Strings by Length

**Question:**
Group words into a map where the key is the length and the value is a list of words with that length.

**Approach:**
*   Use `Collectors.groupingBy(String::length)`.

**Code:**
```java
Map<Integer, List<String>> groupByLength(List<String> list) {
    return list.stream()
            .collect(Collectors.groupingBy(String::length));
}
```

**Explanation:**
*   `groupingBy` creates a bucket for each unique length returned by the classifier function.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Manual grouping using `computeIfAbsent()`.

**Pitfall:**
*   Assuming the resulting Map is sorted by key (it is not; use `TreeMap::new` if sorting is needed).

**Interview Insight:**
*   Tests ability to perform complex data aggregations.

---

#### 16. Max Salary by Department

**Question:**
Given a list of Employees, find the highest salary in each department.

**Approach:**
*   Use `groupingBy()` with a downstream `maxBy()` collector.

**Code:**
```java
Map<String, Optional<Employee>> maxSalaryByDept(List<Employee> employees) {
    return employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDept,
                Collectors.maxBy(Comparator.comparingDouble(Employee::getSalary))
            ));
}
```

**Explanation:**
*   Groups by department name, then for each group, finds the "maximum" using the salary comparator.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)** (to store the map)

**Alternative:**
*   Use `toMap()` with a merge function: `(existing, replacement) -> existing.getSalary() > replacement.getSalary() ? existing : replacement`.

**Pitfall:**
*   The result value is `Optional<Employee>`, which needs to be unwrapped (using `collectingAndThen` is a senior move).

**Interview Insight:**
*   A standard "Senior" stream question involving nested collectors.

---

#### 17. Average Salary by Department

**Question:**
Calculate the average salary for each department.

**Approach:**
*   Use `groupingBy()` with `averagingDouble()`.

**Code:**
```java
Map<String, Double> avgSalaryByDept(List<Employee> employees) {
    return employees.stream()
            .collect(Collectors.groupingBy(
                Employee::getDept,
                Collectors.averagingDouble(Employee::getSalary)
            ));
}
```

**Explanation:**
*   Downstream collector `averagingDouble` performs the math automatically as elements are grouped.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(k)** (where k is number of departments)

**Alternative:**
*   Summing and counting manually (too verbose).

**Pitfall:**
*   Precision errors if using `float`. `Double` is preferred for financial data (or `BigDecimal` for production).

**Interview Insight:**
*   Tests knowledge of built-in arithmetic collectors.

---

#### 18. Count Elements Matching a Predicate

**Question:**
Count how many strings in a list start with the letter 'A'.

**Approach:**
*   Use `.filter()` followed by `.count()`.

**Code:**
```java
long countStartingWithA(List<String> list) {
    return list.stream()
            .filter(s -> s.startsWith("A"))
            .count();
}
```

**Explanation:**
*   `count()` is a terminal operation that returns the size of the filtered stream.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)**

**Alternative:**
*   Using `int sum = stream.mapToInt(s -> s.startsWith("A") ? 1 : 0).sum()`.

**Pitfall:**
*   Using `collect(toList()).size()`, which wastes memory by creating a whole new list just to get its count.

**Interview Insight:**
*   Checks efficiency awareness.

---

#### 19. Partition Even and Odd Numbers

**Question:**
Split a list of integers into two groups: those that are even and those that are odd.

**Approach:**
*   Use `Collectors.partitioningBy()`.

**Code:**
```java
Map<Boolean, List<Integer>> partitionNumbers(List<Integer> list) {
    return list.stream()
            .collect(Collectors.partitioningBy(n -> n % 2 == 0));
}
```

**Explanation:**
*   `partitioningBy` is a special case of `groupingBy` that always uses a boolean key.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(n)**

**Alternative:**
*   Using `groupingBy` with a boolean criterion (same result, but `partitioningBy` is more expressive).

**Pitfall:**
*   Iterating twice (once for even, once for odd), which is **O(2n)**.

**Interview Insight:**
*   Tests knowledge of specialized collectors.

---

#### 20. Product of All Elements (reduce)

**Question:**
Calculate the product of all integers in a list.

**Approach:**
*   Use `.reduce()` with an identity of 1.

**Code:**
```java
int calculateProduct(List<Integer> list) {
    return list.stream()
            .reduce(1, (a, b) -> a * b);
}
```

**Explanation:**
*   The first parameter `1` is the identity. If the list is empty, the result is 1.

**Complexity:**
*   Time: **O(n)**
*   Space: **O(1)**

**Alternative:**
*   Iterative loop.

**Pitfall:**
*   Using `0` as the identity, which will make the custom product always `0`.

**Interview Insight:**
*   Tests understanding of the "Fold" (Reduce) operation.

---


#### 21. Two Sum (O(N))

**Question:**
Find indices of two numbers that add up to a specific target.

**Approach:**
*   Use a `HashMap` to store `(target - num, index)`.

**Code:**
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) return new int[]{map.get(complement), i};
        map.put(nums[i], i);
    }
    return new int[]{};
}
```

**Complexity:**
*   Time: **O(N)**
*   Space: **O(N)**

---

#### 22. Binary Search (Iterative)

**Question:**
Find the index of `target` in a sorted array.

**Code:**
```java
int binarySearch(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

---

#### 23. Anagram Check

**Question:**
Determine if two strings are anagrams of each other.

**Approach:**
*   Use a frequency array of size 26.

**Code:**
```java
boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] count = new int[26];
    for (char c : s.toCharArray()) count[c - 'a']++;
    for (char c : t.toCharArray()) {
        if (--count[c - 'a'] < 0) return false;
    }
    return true;
}
```

---

#### 24. Reverse Words in a String

**Question:**
Input: `"the sky is blue"` -> Output: `"blue is sky the"`

**Code:**
```java
String reverseWords(String s) {
    String[] words = s.trim().split("\\s+");
    Collections.reverse(Arrays.asList(words));
    return String.join(" ", words);
}
```

---

#### 25. String to Integer (atoi)

**Question:**
Convert a string to a 32-bit signed integer.

**Pitfall:**
*   Handling whitespace, signs (`+`/`-`), and integer overflow.

---

#### 26. Valid Palindrome

**Question:**
Check if a string is a palindrome, ignoring non-alphanumeric characters.

**Code:**
```java
boolean isPalindrome(String s) {
    int i = 0, j = s.length() - 1;
    while (i < j) {
        if (!Character.isLetterOrDigit(s.charAt(i))) i++;
        else if (!Character.isLetterOrDigit(s.charAt(j))) j--;
        else if (Character.toLowerCase(s.charAt(i++)) != Character.toLowerCase(s.charAt(j--))) return false;
    }
    return true;
}
```

---

#### 27. Longest Substring Without Repeating Characters

**Question:**
Find the length of the longest substring without duplicates.

**Approach:**
*   Sliding window with a `Set` or `Map` to track character indices.

**Code:**
```java
int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> map = new HashMap<>();
    int max = 0, left = 0;
    for (int right = 0; right < s.length(); right++) {
        if (map.containsKey(s.charAt(right))) left = Math.max(left, map.get(s.charAt(right)) + 1);
        map.put(s.charAt(right), right);
        max = Math.max(max, right - left + 1);
    }
    return max;
}
```

---

#### 28. Container With Most Water

**Question:**
Find two lines that together with the x-axis forms a container with the most water.

**Code:**
```java
int maxArea(int[] height) {
    int max = 0, i = 0, j = height.length - 1;
    while (i < j) {
        max = Math.max(max, Math.min(height[i], height[j]) * (j - i));
        if (height[i] < height[j]) i++; else j--;
    }
    return max;
}
```

---

#### 29. Maximum Subarray (Kadane's Algorithm)

**Question:**
Find the contiguous subarray with the largest sum.

**Code:**
```java
int maxSubArray(int[] nums) {
    int max = nums[0], curr = nums[0];
    for (int i = 1; i < nums.length; i++) {
        curr = Math.max(nums[i], curr + nums[i]);
        max = Math.max(max, curr);
    }
    return max;
}
```

**Complexity:**
*   Time: **O(N)**

---

#### 30. Merge Intervals

**Question:**
Merge overlapping intervals: `[[1,3],[2,6]]` -> `[[1,6]]`.

**Code:**
```java
int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    LinkedList<int[]> merged = new LinkedList<>();
    for (int[] interval : intervals) {
        if (merged.isEmpty() || merged.getLast()[1] < interval[0]) merged.add(interval);
        else merged.getLast()[1] = Math.max(merged.getLast()[1], interval[1]);
    }
    return merged.toArray(new int[merged.size()][]);
}
```

---

#### 31. Insert Interval

**Question:**
Insert a new interval into a sorted list of intervals and merge if necessary.

---

#### 32. Non-overlapping Intervals

**Question:**
Minimum number of intervals to remove to make the rest non-overlapping.

**Approach:**
*   Greedy: Sort by end time and count non-overlaps.

---

#### 33. Meeting Rooms II

**Question:**
Minimum number of conference rooms required.

**Approach:**
*   Sort start and end times separately, or use a `PriorityQueue`.

---

#### 34. Search in Rotated Sorted Array

**Question:**
Find target in `[4,5,6,7,0,1,2]`.

**Algorithm:**
*   Modified Binary Search. Check which half is sorted.

---

#### 35. Find Minimum in Rotated Sorted Array

**Question:**
Find pivot element in $O(\log N)$.

**Code:**
```java
int findMin(int[] nums) {
    int l = 0, r = nums.length - 1;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (nums[m] > nums[r]) l = m + 1; else r = m;
    }
    return nums[l];
}
```

---

#### 36. Search a 2D Matrix

**Question:**
Search target in a matrix where rows are sorted and first element of row > last of previous.

**Approach:**
*   Treat the 2D matrix as a flat 1D array of size `m*n`.

---

#### 37. K-th Largest Element in an Array

**Question:**
Find the k-th largest element (not k-th distinct).

**Code:**
```java
int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int n : nums) {
        pq.offer(n);
        if (pq.size() > k) pq.poll();
    }
    return pq.peek();
}
```

---

#### 38. Top K Frequent Elements

**Question:**
Find the k most frequent elements in an array.

**Approach:**
*   Use a frequency map and then a Bucket Sort or PriorityQueue.

---

#### 39. Find All Duplicates in an Array

**Question:**
Find all duplicates in $O(N)$ time and $O(1)$ space.

**Algorithm:**
*   Negate values at indices to mark "seen".

---

#### 40. Cycle Detection (LinkedList)

**Question:**
Check if a linked list has a cycle (Floyd's Cycle-Finding Algorithm).

**Code:**
```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next; fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

#### 41. Create a Deadlock Situation

**Question:**
Write a program to demonstrate a deadlock between two threads.

**Approach:**
*   Thread 1 locks Resource A and waits for Resource B.
*   Thread 2 locks Resource B and waits for Resource A.

**Code:**
```java
void deadlockDemo() {
    Object A = new Object(), B = new Object();
    new Thread(() -> {
        synchronized(A) {
            Thread.sleep(100);
            synchronized(B) {}
        }
    }).start();
    new Thread(() -> {
        synchronized(B) {
            Thread.sleep(100);
            synchronized(A) {}
        }
    }).start();
}
```

**Complexity:**
*   Space: **O(1)**

**Interview Insight:**
*   Tests knowledge of thread state and locking order.

---

#### 42. Implement an Immutable Class

**Question:**
Create a thread-safe, immutable class.

**Approach:**
*   Final class, private final fields, and deep copies for non-primitive fields.

**Code:**
```java
public final class User {
    private final String name;
    private final List<String> roles;
    public User(String name, List<String> roles) {
        this.name = name;
        this.roles = List.copyOf(roles); 
    }
    public String getName() { return name; }
    public List<String> getRoles() { return roles; }
}
```

**Pitfall:**
*   Exposing the original mutable list to the outside world.

---

#### 43. Singleton Pattern (Double-Checked Locking)

**Question:**
Implement a thread-safe Singleton.

**Approach:**
*   Use `volatile` and double-checked synchronization.

**Code:**
```java
public class DB {
    private static volatile DB instance;
    public static DB getInstance() {
        if (instance == null) {
            synchronized(DB.class) {
                if (instance == null) instance = new DB();
            }
        }
        return instance;
    }
}
```

---

#### 44. Handling Nulls with Optional

**Question:**
Safely fetch a nested value from a potentially null object.

**Approach:**
*   `Optional.ofNullable(...).map(...).orElse(...)`.

**Code:**
```java
String getCity(User user) {
    return Optional.ofNullable(user)
            .map(User::getAddress)
            .map(Address::getCity)
            .orElse("N/A");
}
```

---

#### 45. FlatMap with Optional

**Question:**
Chain methods where the intermediate result is also an `Optional`.

**Code:**
```java
Optional<String> getCode(User user) {
    return Optional.ofNullable(user)
            .flatMap(User::getOptionalProfile)
            .map(Profile::getCode);
}
```

---

#### 46. Create Virtual Threads (Java 21)

**Question:**
Demonstrate how to start 100,000 threads for network tasks.

**Approach:**
*   Use `Executors.newVirtualThreadPerTaskExecutor()`.

**Code:**
```java
void runManyTasks() {
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
        IntStream.range(0, 100_000).forEach(i -> {
            executor.submit(() -> { ... task logic ... });
        });
    }
}
```

**Interview Insight:**
*   Virtual threads solve the "one-thread-per-connection" scalability issue.

---

#### 47. Use Structured Concurrency (Java 21)

**Question:**
Run two parallel subtasks and fail if either fails.

**Code:**
```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Subtask<String> user = scope.fork(() -> fetchUser());
    Subtask<Integer> id = scope.fork(() -> fetchId());
    scope.join().throwIfFailed();
    return new Data(user.get(), id.get());
}
```

---

#### 48. Scoped Values (Java 21)

**Question:**
Share a context-bound value without passing it as a parameter.

**Code:**
```java
static final ScopedValue<String> CONTEXT = ScopedValue.newInstance();
ScopedValue.where(CONTEXT, "admin").run(() -> {
    service.doProtectedAction();
});
```

---

#### 49. Record as a DTO (Java 17+)

**Question:**
Create an immutable data holder for an API response.

**Code:**
```java
public record UserResponse(String username, String email) {
    public UserResponse {
        Objects.requireNonNull(email);
    }
}
```

---

#### 50. Simple Search API with Stream

**Question:**
Filter a collection based on name and price range.

**Code:**
```java
List<Product> search(List<Product> items, String name, double min, double max) {
    return items.stream()
            .filter(p -> p.name().contains(name))
            .filter(p -> p.price() >= min && p.price() <= max)
            .toList();
}
```

---

#### 51. Retry Logic with CompletableFuture

**Question:**
Implement a simple auto-retry for an asynchronous task.

**Approach:**
*   Chain `.handle()` or `.exceptionally()` to re-invoke the supplier.

**Code:**
```java
CompletableFuture<String> fetchWithRetry(int retries) {
    return callApi().handle((res, ex) -> {
        if (ex != null && retries > 0) return fetchWithRetry(retries - 1).join();
        return res;
    });
}
```

---

#### 52. Circuit Breaker Mechanism (Concept)

**Question:**
Explain how to prevent cascading failures in microservices.

**Answer:**
*   If a service fails repeatedly, the circuit **trips (Opens)**. Requests fail immediately without hitting the backend, saving resources. After a timeout, it allows a few through (**Half-Open**) to test health.

---

#### 53. Event Processing (Observer Pattern)

**Question:**
Implementing a "Listener" system for state changes.

**Approach:**
*   Maintain a list of listeners and notify them in a loop.

**Code:**
```java
public interface Listener { void onUpdate(String msg); }
class Server {
    List<Listener> observers = new ArrayList<>();
    void notify(String msg) { observers.forEach(o -> o.onUpdate(msg)); }
}
```

---

#### 54. Custom ForkJoinPool for Parallel Streams

**Question:**
How do you avoid blocking the common `ForkJoinPool` during heavy I/O?

**Approach:**
*   Submit the stream task to a custom pool instance.

**Code:**
```java
ForkJoinPool customPool = new ForkJoinPool(10);
customPool.submit(() -> list.parallelStream().forEach(...)).join();
```

---

#### 55. GC Metrics Monitoring

**Question:**
How do you check for "Stop-the-World" pauses in a running JVM?

**Answer:**
*   Use `jstat -gc <pid> 1000` to see GC frequency and duration. Look for high `FGC` (Full GC) counts.

---
#### 56. Intersection of Two Sorted Arrays (O(N))

**Question:**
Find the common elements between two sorted arrays efficiently.

**Approach:**
*   Use two pointers starting at 0. If values match, record and increment both. If not, increment the pointer of the smaller value.

**Code:**
```java
List<Integer> sortedIntersection(int[] a, int[] b) {
    List<Integer> res = new ArrayList<>();
    int i = 0, j = 0;
    while (i < a.length && j < b.length) {
        if (a[i] == b[j]) { res.add(a[i]); i++; j++; }
        else if (a[i] < b[j]) i++;
        else j++;
    }
    return res;
}
```

**Complexity:**
*   Time: **O(N + M)**
*   Space: **O(1)** (excluding result)

---

#### 57. Circular Buffer (Ring Buffer)

**Question:**
Implement a fixed-size Circular Buffer.

**Approach:**
*   Use an array with `head` and `tail` indices. Wrap indices using modulo (`% size`).

**Code:**
```java
class RingBuffer<T> {
    private T[] data;
    private int head = 0, tail = 0, count = 0;
    public RingBuffer(int size) { data = (T[]) new Object[size]; }
    public void add(T val) {
        data[tail] = val;
        tail = (tail + 1) % data.length;
        if (count == data.length) head = (head + 1) % data.length;
        else count++;
    }
}
```

---

#### 58. Rate Limiter (Token Bucket)

**Question:**
Implement a simple Token Bucket rate limiter.

**Approach:**
*   Track current tokens and last refill time. Add tokens proportional to elapsed time on every request.

**Code:**
```java
class RateLimiter {
    private float tokens;
    private long lastTime = System.currentTimeMillis();
    public synchronized boolean allow(int rate, int cap) {
        long now = System.currentTimeMillis();
        tokens = Math.min(cap, tokens + (now - lastTime) * (rate / 1000.0f));
        lastTime = now;
        if (tokens >= 1) { tokens--; return true; }
        return false;
    }
}
```

---

#### 59. Exponential Backoff Logic

**Question:**
Write a function to calculate a wait time that doubles on every retry with "jitter".

**Code:**
```java
long getWaitTime(int retry, long base) {
    long backoff = base * (long) Math.pow(2, retry);
    return backoff + new Random().nextLong(backoff / 2); // adding jitter
}
```

---

#### 60. Custom ThreadPool (Basic)

**Question:**
Implement a simple Thread Pool where workers take tasks from a `BlockingQueue`.

**Code:**
```java
class SimplePool {
    private final BlockingQueue<Runnable> queue = new LinkedBlockingQueue<>();
    public SimplePool(int threads) {
        for (int i = 0; i < threads; i++) {
            new Thread(() -> {
                while (true) {
                    try { queue.take().run(); } catch (Exception e) {}
                }
            }).start();
        }
    }
    public void execute(Runnable task) { queue.offer(task); }
}
```

---

#### 61. Reflection: Accessing a Private Method

**Question:**
You have a JAR but need to call a private method `secretMethod()` from a class `LegacyComponent`.

**Approach:**
*   Use `getDeclaredMethod()`, then `setAccessible(true)`.

**Code:**
```java
void callPrivate(Object obj) throws Exception {
    Method m = obj.getClass().getDeclaredMethod("secretMethod");
    m.setAccessible(true);
    m.invoke(obj);
}
```

---

#### 62. Dynamic Proxy (JDK)

**Question:**
Create a wrapper around an interface to log every method call.

**Code:**
```java
Object proxy = Proxy.newProxyInstance(
    target.getClass().getClassLoader(),
    target.getClass().getInterfaces(),
    (p, method, args) -> {
        System.out.println("Invoking: " + method.getName());
        return method.invoke(target, args);
    });
```

---

#### 63. Classloader: Loading a JAR at Runtime

**Question:**
How do you load a class from a JAR file dynamically if it’s not on the classpath?

**Code:**
```java
URL[] urls = { new URL("file:///path/to/my-jar.jar") };
URLClassLoader cl = new URLClassLoader(urls);
Class<?> cls = cl.loadClass("com.example.MyClass");
```

---

#### 64. String Constant Pool (Manual Internship)

**Question:**
Ensure two strings created with `new String()` point to the same memory location in the pool.

**Code:**
```java
String s1 = new String("test").intern();
String s2 = new String("test").intern();
System.out.println(s1 == s2); // Output: true
```

---

#### 65. Volatile vs AtomicInteger

**Question:**
Why is `volatile int count = 0; count++;` not thread-safe?

**Answer:**
*   `count++` is not atomic; it’s 3 steps (read, increment, write). `volatile` only ensures visibility, not atomicity. Use `AtomicInteger` for CAS (Compare-And-Swap) operations.

---

#### 66. CountDownLatch vs CyclicBarrier

**Question:**
When would you use `CyclicBarrier` over `CountDownLatch`?

**Answer:**
*   `CountDownLatch` is for a "Wait for N tasks" (one-time). `CyclicBarrier` is for a "Wait for each other" (multi-stage rounds) and can be **reused** after the barrier trips.

---

#### 67. Phaser (Java 7 Concurrency API)

**Question:**
Implement a multi-phase task where the number of participants can change.

**Code:**
```java
Phaser phaser = new Phaser(1); // register self
phaser.arriveAndAwaitAdvance(); // phase 1 complete
phaser.arriveAndDeregister(); // exit
```

---

#### 68. StampedLock (Optimistic Read)

**Question:**
How do you perform a high-performance read that doesn't block writers unless necessary?

**Code:**
```java
StampedLock lock = new StampedLock();
long stamp = lock.tryOptimisticRead();
// ... read fields ...
if (!lock.validate(stamp)) { // check if a write happened
    stamp = lock.readLock(); // fallback to heavy read lock
    try { /* ... re-read ... */ } finally { lock.unlockRead(stamp); }
}
```

---

#### 69. ReentrantLock with Fair Ordering

**Question:**
Ensure threads get a lock in the exact order they requested it.

**Code:**
```java
Lock fairLock = new ReentrantLock(true); // 'true' enables fairness
```

---

#### 70. Checking Memory Leaks with VisualVM

**Question:**
How do you identify which object is eating the heap in a live environment?

**Answer:**
*   Take a **Heap Dump** `.hprof` and open it in VisualVM or Eclipse Mat. Sort by **Retained Size**. Look for "GC Roots" — paths that prevent the object from being garbage collected.

#### 71. ThreadLocal: Preventing Memory Leaks

**Question:**
How do you use `ThreadLocal` safely in a ThreadPool (like Tomcat) to avoid memory leaks?

**Approach:**
*   Always call `remove()` in a `finally` block.

**Code:**
```java
ThreadLocal<User> context = new ThreadLocal<>();
try {
    context.set(currentUser);
    businessLogic();
} finally {
    context.remove(); // CRITICAL: prevents thread from carrying old value to next request
}
```

**Interview Insight:**
*   Threads in pools are reused. If you don't call `remove()`, the object stays in the thread's map forever, preventing GC.

---

#### 72. InheritableThreadLocal

**Question:**
Pass a value from a parent thread to a child thread automatically.

**Code:**
```java
ThreadLocal<String> tl = new InheritableThreadLocal<>();
tl.set("ParentData");
new Thread(() -> System.out.println(tl.get())).start(); // Output: ParentData
```

---

#### 73. StackOverflowError: Recursive Depth

**Question:**
How do you increase the stack size for deep recursion in JVM?

**Answer:**
*   Use the `-Xss` flag (e.g., `-Xss2m`). However, the real solution is usually to refactor to an iterative approach using an explicit `Stack` object on the heap.

---

#### 74. OutOfMemoryError: Metaspace vs Heap

**Question:**
You get `java.lang.OutOfMemoryError: Metaspace`. What does it mean?

**Answer:**
*   **Metaspace** stores class metadata. This error occurs if you load too many classes (e.g., via dynamic proxies or reflection in a loop). Unlike the Heap, it grows automatically unless limited by `-XX:MaxMetaspaceSize`.

---

#### 75. WeakReference vs SoftReference

**Question:**
When would you use a `SoftReference` for a cache?

**Answer:**
*   **WeakReference:** Collected immediately during the next GC cycle.
*   **SoftReference:** Only collected when the JVM actually runs out of memory. This makes it ideal for memory-sensitive caches.

---

#### 76. PhantomReference and Cleaner

**Question:**
What is the modern replacement for the deprecated `Object.finalize()`?

**Approach:**
*   Use `java.lang.ref.Cleaner`.

**Code:**
```java
Cleaner cleaner = Cleaner.create();
cleaner.register(myObj, () -> System.out.println("Cleaning resources..."));
```

---

#### 77. Unsafe API: Manual Memory Management

**Question:**
Allocating memory outside the Java Heap.

**Code:**
```java
long address = unsafe.allocateMemory(1024);
unsafe.putInt(address, 42);
unsafe.freeMemory(address); // MUST be freed manually
```

**Interview Insight:**
*   Only for extreme performance (off-heap caching like BigMemory or Aeron).

---

#### 78. VarHandle (Java 9+ Alternative to Unsafe)

**Question:**
Safely perform atomic updates on a private field without `AtomicInteger`.

**Code:**
```java
private static final VarHandle COUNT;
static {
    try {
        COUNT = MethodHandles.lookup().findVarHandle(MyClass.class, "count", int.class);
    } catch (Exception e) { throw new Error(e); }
}
void increment() { COUNT.getAndAdd(this, 1); }
```

---

#### 79. Manual Garbage Collection Hint

**Question:**
Does `System.gc()` guarantee immediate garbage collection?

**Answer:**
*   **No.** It is a "hint" to the JVM. Most modern production JVMs ignore it entirely. In some cases, it can actually hurt performance by triggering an expensive Full GC when only a minor one was needed.

---

#### 80. Checking Thread Contention

**Question:**
A service is slow despite low CPU usage. How do you check for lock contention?

**Approach:**
*   Analyze thread states to find many threads in `BLOCKED` status.

**Answer:**
*   Take a **Thread Dump** (`jstack <pid>`). Look for threads in the `BLOCKED` state. If many threads are waiting for the same monitor (object lock), you have identified the bottleneck.

---

#### 81. Custom Stack (Fixed Size array)

**Question:**
Implement a LIFO Stack using a basic integer array.

**Approach:**
*   Use an array and a `top` index.

**Code:**
```java
class MyStack {
    private int[] data = new int[10];
    private int top = -1;
    public void push(int x) { data[++top] = x; }
    public int pop() { return data[top--]; }
    public boolean isEmpty() { return top == -1; }
}
```

---

#### 82. Stack using Two Queues

**Question:**
Implement a Stack where you only have `Queue.offer()` and `Queue.poll()` available.

**Approach:**
*   Use two queues. For push, add to q2, move all q1 to q2, then swap q1 and q2.

**Code:**
```java
void push(int x) {
    q2.offer(x);
    while (!q1.isEmpty()) q2.offer(q1.poll());
    Queue<Integer> temp = q1; q1 = q2; q2 = temp;
}
```

---

#### 83. Queue using Two Stacks

**Question:**
Implement a FIFO Queue using two LIFO Stacks.

**Approach:**
*   Push to `s1`. To pop, if `s2` is empty, move all from `s1` to `s2`. Pop from `s2`.

**Code:**
```java
public int dequeue() {
    if (s2.isEmpty()) while (!s1.isEmpty()) s2.push(s1.pop());
    return s2.pop();
}
```

**Interview Insight:**
*   Amortized time complexity for dequeue is $O(1)$.

---

#### 84. Balanced Parentheses (Stack)

**Question:**
Check if "(([]))" is balanced.

**Code:**
```java
boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(')');
        else if (c == '[') stack.push(']');
        else if (stack.isEmpty() || stack.pop() != c) return false;
    }
    return stack.isEmpty();
}
```

---

#### 85. Next Greater Element (Monotonic Stack)

**Question:**
For index `i`, find the first index `j > i` where `arr[j] > arr[i]`.

**Algorithm:**
```java
int[] nextGreater(int[] nums) {
    int[] res = new int[nums.length];
    Stack<Integer> s = new Stack<>();
    for (int i = nums.length - 1; i >= 0; i--) {
        while (!s.isEmpty() && s.peek() <= nums[i]) s.pop();
        res[i] = s.isEmpty() ? -1 : s.peek();
        s.push(nums[i]);
    }
    return res;
}
```

**Complexity:**
*   Time: **O(N)**

---

#### 86. Permutation of a String (Recursion)

**Question:**
Generate all possible arrangements of "ABC".

**Code:**
```java
void permute(String s, String res) {
    if (s.isEmpty()) { System.out.println(res); return; }
    for (int i = 0; i < s.length(); i++) {
        permute(s.substring(0, i) + s.substring(i + 1), res + s.charAt(i));
    }
}
```

---

#### 87. Generate All Subsets (Power Set)

**Question:**
Input: `[1, 2]` -> Output: `[], [1], [2], [1, 2]`

**Code:**
```java
void subsets(int[] nums, int i, List<Integer> curr) {
    if (i == nums.length) { System.out.println(curr); return; }
    subsets(nums, i + 1, new ArrayList<>(curr)); // Exclude
    curr.add(nums[i]);
    subsets(nums, i + 1, new ArrayList<>(curr)); // Include
}
```

---

#### 88. Binary Tree Inorder Traversal (Iterative)

**Question:**
Traverse a tree (Left, Node, Right) without recursion.

**Approach:**
*   Use a Stack. Push current node and move left until null. Pop, print, move right.

**Code:**
```java
void inorder(TreeNode root) {
    Stack<TreeNode> s = new Stack<>();
    TreeNode curr = root;
    while (curr != null || !s.isEmpty()) {
        while (curr != null) { s.push(curr); curr = curr.left; }
        curr = s.pop();
        System.out.println(curr.val);
        curr = curr.right;
    }
}
```

---

#### 89. Lowest Common Ancestor (Binary Tree)

**Question:**
Find the deepest node that is a parent of both `p` and `q`.

**Code:**
```java
TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) return root;
    TreeNode left = lca(root.left, p, q);
    TreeNode right = lca(root.right, p, q);
    if (left != null && right != null) return root;
    return left != null ? left : right;
}
```

---

#### 90. Level Order Traversal (BFS)

**Question:**
Print tree nodes level by level.

**Approach:**
*   Use a `Queue`. Offer root, then while not empty, poll, print, and offer children.

**Code:**
```java
void bfs(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);
    while (!q.isEmpty()) {
        TreeNode n = q.poll();
        System.out.println(n.val);
        if (n.left != null) q.offer(n.left);
        if (n.right != null) q.offer(n.right);
    }
}
```

---

#### 91. Zig-Zag Traversal of a Tree

**Question:**
Level 1: Left-to-Right. Level 2: Right-to-Left. Level 3: Left-to-Right...

**Approach:**
*   Similar to BFS but use two stacks or a Deque and a flag.

**Code:**
```java
void zigZag(TreeNode root) {
    if (root == null) return;
    Deque<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    boolean rev = false;
    while (!q.isEmpty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode n = rev ? q.pollLast() : q.pollFirst();
            System.out.print(n.val + " ");
            if (rev) { 
                if (n.right != null) q.offerFirst(n.right);
                if (n.left != null) q.offerFirst(n.left);
            } else {
                if (n.left != null) q.offerLast(n.left);
                if (n.right != null) q.offerLast(n.right);
            }
        }
        rev = !rev;
    }
}
```

---

#### 92. K-th Smallest Element in a BST

**Question:**
Find the k-th smallest value in a Binary Search Tree.

**Approach:**
*   Inorder traversal of a BST is sorted. Perform inorder and count until `k`.

**Code:**
```java
void findKth(TreeNode root, int k) {
    if (root == null) return;
    findKth(root.left, k);
    if (++count == k) System.out.println(root.val);
    findKth(root.right, k);
}
```

---

#### 93. TST (Ternary Search Tree) Concept

**Question:**
What is the memory advantage of a TST over a standard Trie?

**Answer:**
*   A **Trie** has 26 pointers (for ASCII) per node, many of which are null. A **TST** only has 3 pointers (Less, Equal, Greater) per node, making it much more memory-efficient at the cost of slight speed degradation.

---

#### 94. Spliterator: Custom Parallel Stream Behavior

**Question:**
How do you control how a stream is split for parallel execution?

**Answer:**
*   Implement `Spliterator<T>`. Override `trySplit()` to return a new spliterator for half the data and `tryAdvance()` for single-element processing.

---

#### 95. Collectors.collectingAndThen()

**Question:**
Collect a stream into a List and then immediately wrap it into an `UnmodifiableList`.

**Code:**
```java
List<String> list = stream.collect(
    Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList)
);
```

---

#### 96. Stream.takeWhile() vs filter()

**Question:**
Get elements from a list until a condition is first broken.

**Code:**
```java
List<Integer> list = Stream.of(1, 2, 10, 3)
    .takeWhile(n -> n < 10)
    .toList(); // Output: [1, 2] (3 is ignored even if it meets the condition)
```

---

#### 97. Simple JSON Stringifier (Recursion)

**Question:**
Convert a `Map<String, Object>` into a JSON-like string recursively.

**Code:**
```java
String toJson(Object obj) {
    if (obj instanceof Map) {
        return "{" + ((Map<?,?>)obj).entrySet().stream()
            .map(e -> "\"" + e.getKey() + "\":" + toJson(e.getValue()))
            .collect(Collectors.joining(",")) + "}";
    }
    return "\"" + obj.toString() + "\"";
}
```

---

#### 98. Bloom Filter (Scalability Logic)

**Question:**
How do you check if a username exists across 1 billion records without hitting a database?

**Answer:**
*   Use a **Bloom Filter**. It's a probabilistic data structure. It can say "Definitely No" (No collisions) or "Maybe Yes" (Potential false positive). It uses $O(1)$ time and tiny memory compared to a full set.

---

#### 99. Checking Thread Deadlock programmatically

**Question:**
How can a Java application detect if it’s currently in a deadlock?

**Code:**
```java
ThreadMXBean bean = ManagementFactory.getThreadMXBean();
long[] deadlockedThreads = bean.findDeadlockedThreads();
if (deadlockedThreads != null) {
    ThreadInfo[] info = bean.getThreadInfo(deadlockedThreads);
    System.out.println("Deadlock Detected!");
}
```

---

#### 100. Manual Garbage Collection "Hint"

**Question:**
Why is `System.gc()` often disabled in production (-XX:+DisableExplicitGC)?

**Answer:**
*   To prevent developers from accidentally triggering expensive "Stop-the-World" Full GC pauses during critical request processing.

---

**Q: How do you identify and fix a memory leak in a Java application?**
**A:** Monitor heap usage for a continuous upward trend. Use `jmap -dump` to create a snapshot and analyze it in Eclipse MAT. Look for the "Leak Suspects" report. Common causes include unclosed Resources (DB/Stream), static collections growing infinitely, or `ThreadLocal` variables not being removed.

**Q: What is the difference between `synchronized` and `ReentrantLock`?**
**A:** `synchronized` is a simple JVM-level keyword. `ReentrantLock` is a more robust class that supports **Timeouts** (`tryLock`), **Interruption**, and **Fairness** policies (preventing thread starvation).

---

## 5. Architectural Best Practices

**Q: Explain the SOLID principles in the context of Java development.**
**A:** 
1. **Single Responsibility:** A class should do one thing (e.g., a `User` class shouldn't have `sendEmail()` logic).
2. **Open-Closed:** Open for extension, closed for modification (use Inheritance/Interfaces).
3. **Liskov Substitution:** Subclasses should be swappable for their parent classes.
4. **Interface Segregation:** Don't force a class to implement methods it doesn't need (use smaller, specific interfaces).
5. **Dependency Inversion:** Depend on abstractions, not concrete implementations (the foundation of Spring DI).

**Q: When should you use Checked vs. Unchecked Exceptions?**
**A:**
*   **Checked:** For scenarios that are **recoverable** and expected (e.g., `FileNotFoundException`). The caller $must$ handle it.
*   **Unchecked (Runtime):** For **programming errors** (e.g., `NullPointerException`) or scenarios where the application cannot realistically recover. In modern microservices, most developers prefer Unchecked exceptions to keep method signatures clean.

---

## 6. Quick Revision: The Golden Reference

### 6.1 DSA Pattern Recognition — 10 Rules
| # | If you see this... | Best Strategy |
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

### 6.2 Java Streams — Golden Rules
| # | Best Practice | Why it Matters |
|---|---|---|
| 1 | Never modify the source inside a stream | Causes ConcurrentModificationException |
| 2 | Use .distinct() before .sorted() | Saves sorting duplicates - cheaper |
| 3 | Use filter() as early as possible | Reduces elements flowing through pipeline |
| 4 | Prefer .findFirst() over .collect().get(0) | Short-circuits - stops at first match |
| 5 | Use mapToInt/mapToDouble for numeric ops | Avoids boxing overhead of map() |
| 6 | Never use parallelStream() with shared mutable state | Race conditions - use ConcurrentHashMap instead |
| 7 | Use Collectors.groupingBy() for any group-by problem | Replaces nested loops + maps |
| 8 | Use Collectors.joining() for string joining | Much faster than + concatenation in loops |
| 9 | flatMap() = map + flatten | Use when each element maps to a collection |
| 10 | Chain Comparator.comparing().thenComparing() | Multi-field sorting with no if-else |
| 11 | Stream.iterate() for infinite/generated sequences | Fibonacci, number ranges, sequences |
| 12 | Use collectors.collectingAndThen() to post-process | E.g., reverse a list after collecting |
| 13 | Use Optional.map().orElse() - never .get() without check | .get() on empty Optional throws exception |
| 14 | peek() is for debugging only - never business logic | Terminal ops may not run on all elements |
| 15 | reduce(identity, accumulator) for fold operations | Sum, product, max without boxing |

### 6.3 String Problems — Golden Rules
| # | Best Practice | Why it Matters |
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

### 6.4 Collections — Golden Rules
| # | Best Practice | Why it Matters |
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

### 6.5 Concurrency — Golden Rules
| # | Best Practice | Why it Matters |
|---|---|---|
| 1 | **Prefer `ReentrantLock` over `synchronized`** | Supports `tryLock`, fairness |
| 2 | **Always** call `ThreadLocal.remove()` in `finally` | Prevents stale data leak in thread pools |
| 3 | **`volatile`** = visibility only, NOT atomicity | Use `AtomicInteger` to increment |
| 4 | **Lock ordering** prevents deadlock | Acquire `lockA` before `lockB` universally |
| 5 | Use `ConcurrentHashMap` over `Collections.synchronizedMap()` | CHM uses segment-locks |
| 6 | Use **`CompletableFuture`** for async pipelines | Avoid raw `Thread` blocking |
| 7 | `parallelStream()` uses shared ForkJoinPool | Starvation risk; use custom pool |
| 8 | **Virtual Threads** (Java 21) — avoid `synchronized` | It pins the carrier thread; use `ReentrantLock` |

### 6.6 SQL Interview — Golden Rules
| # | Best Practice | Why it Matters |
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


