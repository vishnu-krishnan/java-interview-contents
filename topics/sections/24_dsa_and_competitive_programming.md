<!-- Part of Java Learning Roadmap — Section 24 -->

# 🏆 24. Competitive Programming & DSA in Java

---

## 1. Definition

**Data Structures and Algorithms (DSA)** is the study of how to organize data in memory (Data Structures) and the step-by-step instructions used to process that data (Algorithms). 
**Competitive Programming / LeetCode** is the practice of solving highly constrained algorithmic puzzles within strict time and space limits, almost universally used as the primary technical filter in Big Tech software engineering interviews.

---

## 2. Why It Exists

*   **Interview Filtering:** Companies like Google and Amazon need a standardized way to test if a candidate can write efficient code before trusting them with systems that handle millions of requests per second.
*   **Scale Matters:** An `O(N^2)` algorithm works perfectly on an array of 100 users (10,000 operations). If a database grows to 1,000,000 users, that same algorithm requires 1 Trillion operations, causing the server to freeze for hours. Understanding DSA prevents catastrophic performance degradation in production.

---

## 3. How It Works Internally (Big O Notation)

Big O describes how the runtime of an algorithm scales as the input size (`N`) grows.
*   **`O(1)` Constant Time:** Accessing `array[5]`. The time taken is exactly the same whether the array has 10 items or 10 billion items.
*   **`O(log N)` Logarithmic Time:** Binary Search. Every operation cuts the remaining data in half. Finding 1 item in 1 Billion takes only ~30 steps.
*   **`O(N)` Linear Time:** Looping through an array once. Time scales 1:1 with input size.
*   **`O(N log N)` Linearithmic Time:** The absolute best possible time complexity for sorting an array (MergeSort, QuickSort).
*   **`O(N^2)` Quadratic Time:** Nested `for` loops. A massive red flag in code reviews.

---

## 4. Code Examples (The Canonical Patterns)

### 4.1 Two Pointers (Valid Palindrome)
Instead of creating a reversed string (wasting `O(N)` space), use two pointers converging to the middle.
*Time: `O(N)`, Space: `O(1)`*
```java
public boolean isPalindrome(String s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) return false;
        left++;
        right--;
    }
    return true;
}
```

### 4.2 Hash Map (Two Sum Optimization)
Given an array and a target, find two numbers that add up to the target.
**BAD (Nested Loops `O(N^2)`):** Check every number against every other number.
**GOOD (HashMap `O(N)`):** Store what we've seen so we can look back instantly in `O(1)` time.
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    return new int[]{};
}
```

### 4.3 Sliding Window (Max Subarray Limit)
Find the maximum sum of a contiguous subarray of size `k`.
Instead of recalculating the sum of `k` elements from scratch every time, subtract the element leaving the window and add the element entering it.
```java
public int maxSum(int[] arr, int k) {
    int windowSum = 0, maxSum = 0;
    // 1. Calculate first window
    for (int i = 0; i < k; i++) windowSum += arr[i];
    maxSum = windowSum;

    // 2. Slide the window
    for (int i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k]; // Add new, remove old
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Arrays vs Linked Lists? | **Arrays** use contiguous memory. Fast read `O(1)`, slow insert/delete `O(N)` because you have to shift all following elements. **Linked Lists** use scattered memory pointers. Slow read `O(N)` (must traverse from head), but fast insert/delete `O(1)` (just change the pointer) *if you already have the node reference*. |
| Stack vs Queue? | **Stack:** Last-In, First-Out (LIFO). Used for undo mechanisms, JVM method execution, parsing parentheses. **Queue:** First-In, First-Out (FIFO). Used for Task scheduling, Breadth-First-Search (BFS). |
| What is a Hash Collision? | When two different Keys produce the exact same Integer Hash Code. Java's `HashMap` solves this by placing both items into a LinkedList (or a Red-Black Tree in Java 8+) at that specific array bucket index. |
| Difference between a Tree and a Graph? | A Tree is a specialized form of a Graph. A Tree has a root, follows a strict parent-child hierarchy, and **cannot contain cycles** (loops). A Graph can be completely disconnected and circular. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Modifying Strings in a loop | `String s = ""; for(int i=0; i<1000; i++) s += "A";` Strings are immutable. This creates 1000 abandoned String objects on the Heap. Time Complexity accidentally becomes `O(N^2)`. | ALWAYS use `StringBuilder` inside loops for `O(N)` String manipulation. |
| Forgetting Space Complexity | Using a massive 2D matrix dynamic programming grid to solve a problem that only requires keeping track of the previous 2 numbers (like Fibonacci). | During interviews, state the Time complexity AND the Space complexity. Always optimize space if it drops from `O(N)` to `O(1)`. |
| Writing `.contains()` inside a `List` loop | `ArrayList.contains(key)` takes `O(N)` time. Putting it inside an `O(N)` `for` loop makes the whole algorithm `O(N^2)`. | Before the loop, dump the List into a `HashSet`. Checking `HashSet.contains()` is `O(1)`. The algorithm becomes `O(N)`. |

---

## 7. Real-World Usage

| DSA Structure | Where it shows up in Production |
|---|---|
| **Trees (B-Trees)** | The core structure underlying PostgreSQL and MySQL database indexing. Allows O(log N) lookups on 100GB tables. |
| **Graphs** | Neo4j databases. Google Maps calculating the shortest path from LA to NY (Dijkstra's Algorithm). Facebook friend recommendations. |
| **Priority Queue (Min/Max Heap)** | CPU Task Scheduling. Also used in Hospitals/Triage systems where the most critical patient jumps to the front of the line automatically. |

---

## 8. Practice Tasks

*Open LeetCode. Do not use an IDE. Write the code exclusively in the browser to simulate a real whiteboard interview.*
1.  **Fast & Slow Pointers:** Solve *Linked List Cycle* (LeetCode 141). Create two pointers, slow moves 1 step, fast moves 2 steps. If they ever equal each other, the list has an infinite loop.
2.  **Stack:** Solve *Valid Parentheses* (LeetCode 20). Iterate through strings `(){}[]`. If opening, push to stack. If closing, pop from stack and check if it matches.
3.  **Binary Search:** Solve *Binary Search* (LeetCode 704). Find a target in a sorted array in `O(log N)` time without using a linear loop.

---

## 9. Quick Revision

### Time Complexity Master Cheat Sheet
| Scale | Complexity | Typical Problem Signature |
|---|---|---|
| **Best** | `O(1)` | Hash Map lookup, Array Indexing. |
| **Great** | `O(log N)` | Binary Search. Data is constantly halved. |
| **Good** | `O(N)` | Simple `for` loop traversal, Sliding Window, Two Pointers. |
| **Okay** | `O(N log N)` | Sorting an array. `Arrays.sort()` uses this. |
| **Bad** | `O(N^2)` | Nested `for` loops. Often the "Brute Force" starting point. |
| **Terrible**| `O(2^N)` | Recursive tree with 2 branches (e.g. naive Fibonacci). |

### Problem Solving Approach
1. Understand the problem (Ask clarifying questions about upper bounds/nulls).
2. State the Brute Force `O(N^2)` solution verbally.
3. Optimize using a HashMap, Two-Pointers, or Sorting to `O(N)` or `O(N log N)`.
4. Write the code.
5. Dry run it with edge cases (empty array, size 1 array, negative numbers).
