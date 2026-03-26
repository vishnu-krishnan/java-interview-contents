## Recently, I attended a few interviews for a Java developer role in service-based companies. Sharing some commonly asked coding questions that might help others preparing. 👇
Java Streams (Very Important)
1️⃣ First Non-Repeating Character
Find the first character that does not repeat in a string
- Example: "swiss" → w
2️⃣ Reverse Words Using Streams
- Input: "My name is Tom"
- Output: "Tom is name My"
3️⃣ Remove Duplicate Characters
(Remove duplicates while maintaining order)
- Input: "HappyBirthDay"
- Output: "HapyBirthDy"
4️⃣ Sum of Salaries by Department
Group employees and calculate total salary per department
5️⃣ Maximum Salary by Department eg: maxBy() method
Find highest salary in each department
6️⃣ Average Salary by Department eg: averagingToDouble() method
Calculate average salary per department
7️⃣ Sort Students Using Streams
✔ First Sort by First Name
✔ Then by Marks. solve using thenComparing() method

🔹 Data Structures & Algorithms
8️⃣ Three Sum (O(n²))
Find all unique triplets with given sum
- Input: [-1,0,1,2,-2,3], Target = 0
9️⃣ Two Sum (O(n))
Find two numbers with given sum
- Input: [5,7,2,3,4], Target = 9
🔟 Balanced Parentheses
- Input: "{}()" → Balanced
1️⃣1️⃣ Binary Search (O(log n))
- Input: [2,4,6,8,10], Target = 6

💡 If you're preparing for Java roles, focus on these areas — they are being asked frequently!

## 10 Golden Rules for Solving a Coding Question in an Interview 🔥

1 If we are dealing with
top/maximum/minimum/closest
'K' elements among 'N' elements, we will be using a Heap

2 If the given input is a sorted array or a list, we will either be using Binray Search or the Two Pointers strategy.

3 If we need to try all combinations (or permutations) of the input, we can either use Backtracking or Breadth First Search.

4 Most of the questions related to Trees or Graphs can be solved either through Breadth First Search or Depth First Search.

5 Every recursive solution can be converted to an iterative solution using a Stack.

6 For a problem involving arrays, if there exists a solution in O(n^2)time and O(1) space, there must exist two other solutions: 1) Using a HashMap or a Set for O(n) time and O(n) space, 2) Using sorting for O(n log n) time and O(1) space.

7 If a problem is asking for optimization (e.g., maximization or minimization), we will be using Dynamic Programming.

8 If we need to find some common substring among a set of strings, we will be using a HashMap or a Trie.

9 If we need to search/manipulate a bunch of strings, Trie will be the best data structure.

10 If the problem is related to a LinkedList and we can't use extra space, then use the Fast & Slow Pointer approach.

Doc cc : design gurus