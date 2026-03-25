## 💡 UnaryOperator vs Function – A Subtle but Important Java Interview Concept
While exploring Java functional interfaces, I came across an interesting comparison: UnaryOperator vs Function — a small concept that interviewers love to test.
Here’s the clarity I gained:
🔹 Function<T, R>
- Takes input of type T
- Returns output of type R
- Used for general transformations
🔹 UnaryOperator<T>
- Takes input of type T
- Returns output of the same type T
- It’s a specialized version of Function
- Extends Function<T, T>
📌 Key Difference:
UnaryOperator is used when input and output types are the same, while Function is used when they are different.
🔹 Why use UnaryOperator?
- Improves readability (intent is clear)
- Promotes type safety
- Useful in operations like transforming values of same type
📌 Example:
Squaring a number → input = Integer, output = Integer → perfect use case for UnaryOperator
These small distinctions are what make a difference in Java interviews and clean code practices.

---



## Java 8 has transformed the way we write Java, making it more functional, expressive, and powerful.

Here’s a quick cheatsheet I use daily:

- **Lambda Expressions**: Simplify the syntax for writing anonymous functions.
- **Streams API**: Enable functional-style operations on collections, allowing for easy filtering, mapping, and reducing.
- **Optional Class**: Helps to avoid null checks and provides a way to express the absence of a value.
- **Default Methods**: Allow interfaces to have methods with implementations, enabling backward compatibility.
- **Method References**: Provide a shorthand notation for calling methods.

This cheatsheet serves as a handy reference for leveraging the features of Java 8 effectively.

---

## Different versions of Java and their main features for any interview revisions.

→Java 8 (2014)
Introduced functional programming concepts, Lambdas and the Stream API, which totally changed how developers write code for processing collections.

→Java 11 (2018 - LTS)
The most popular feature is the var keyword, which lets you declare local variables with less boilerplate code, making it cleaner and easier to read.

→Java 17 (2021 - LTS)
Focused on making code more expressive and modern. The best additions are Text Blocks for creating multiline strings without all the messy escape characters and Pattern Matching for instanceof, which simplifies type-checking and casting.

→Java 21 (2023 - LTS)
Star of the show is Virtual Threads (from Project Loom), which makes it incredibly easy to write highly concurrent applications that can handle millions of tasks with ease.

Java 25 (LTS - 2025)
Aims to boost performance even further. It will continue to enhance major projects like Panama (for better interaction with native code) and Valhalla (for improved memory layout with value types), making Java even more powerful and scalable.

---

## 𝙅𝒂𝙫𝒂 𝑰𝙣𝒕𝙚𝒓𝙫𝒊𝙚𝒘 𝑷𝙧𝒆𝙥𝒂𝙧𝒂𝙩𝒊𝙤𝒏 - 𝟰

🔹 𝙈𝙖𝙨𝙩𝙚𝙧𝙞𝙣𝙜 𝙅𝙖𝙫𝙖 𝙎𝙩𝙧𝙚𝙖𝙢𝙨: 𝙙𝙞𝙨𝙩𝙞𝙣𝙘𝙩(), 𝙥𝙚𝙚𝙠(), 𝙡𝙞𝙢𝙞𝙩(), 𝙖𝙣𝙙 𝙨𝙠𝙞𝙥()! 🔹

🚀 Java Streams are powerful, but do you know how to control data flow efficiently? In the latest video of my Java Streams Series, I dive deep into four essential methods that every Java developer should master:

✅ distinct() – Remove duplicate elements efficiently
✅ peek() – Inspect elements at different stages of a stream
✅ limit() – Process only a subset of elements
✅ skip() – Ignore unwanted elements with ease

## 💻 Most Asked 35 Java 8 Coding Questions in Interviews
Many developers prepare Java theory.
But in real interviews, companies often test Java 8 coding skills using Streams and Lambda expressions.
Here are 35 commonly asked Java 8 coding problems 👇
 1. Find duplicate elements in a list using Streams
 2. Remove duplicates from a list using Streams
 3. Find the first non-repeated character in a string
 4. Find the frequency of each character in a string
 5. Reverse a string using Streams
 6. Sort a list of integers using Streams
 7. Sort a list of employees by salary using Streams
 8. Find the second highest number in a list
 9. Find the highest number in a list using Streams
 10. Find the minimum number in a list
 11. Find even numbers from a list using Streams
 12. Find odd numbers from a list using Streams
 13. Count numbers greater than a given value
 14. Convert a list into a set using Streams
 15. Convert a list into a map using Streams
 16. Join list of strings into a single string
 17. Find the longest string in a list
 18. Find the shortest string in a list
 19. Group employees by department using Collectors.groupingBy()
 20. Count occurrences of each element in a list
 21. Partition numbers into even and odd
 22. Find duplicate characters in a string
 23. Find common elements between two lists
 24. Convert list of strings to uppercase
 25. Filter employees with salary greater than a given value
 26. Get top 3 highest numbers from a list
 27. Merge two lists using Streams
 28. Check if a list contains duplicate elements
 29. Calculate the sum of numbers using Streams
 30. Group employees by department and count employees
 31. Group employees by department and find highest salary
 32. Group employees by department and average salary
 33. Group strings by their length
 34. Group employees by city
 35. Group words by their first character
These coding problems test your understanding of:
✔ Stream API
✔ Lambda Expressions
✔ Functional Programming
✔ Data transformation using Streams
Master these and you’ll be well prepared for Java backend interviews.

---



## 🚀 Java 8 Features Day 5

🔗 Functional Interface Chaining (Java 8)
 - Java 8 introduced functional interfaces in java.util.function package.

🔹 Predicate Chaining
 - A Predicate<T> returns true or false.
 Methods:
 and() → Both conditions must be true
 or() → At least one condition must be true
 negate() → Opposite result

Example : and()

import java.util.function.Predicate;
class Main {
 public static void main(String[] args) {
 Predicate<Integer> isEven = number -> number % 2 == 0;
 Predicate<Integer> isGreaterThan100 = number -> number > 100;
 Predicate<Integer> combined = isGreaterThan100.and(isEven);
 System.out.println(combined.test(175)); // false
 }
}

Example: or()

Predicate<Integer> combined = isGreaterThan100.or(isEven);
System.out.println(combined.test(175)); // true

Example: negate()

Predicate<Integer> notGreaterThan100 = isGreaterThan100.negate();
System.out.println(notGreaterThan100.test(15)); // true

🔹 Function Chaining
 - A Function<T, R> transforms data.
 Methods:
 andThen() → First perform current function, then the next.
 compose() → First perform parameter function, then current function

import java.util.function.Function;

class Main {
 public static void main(String[] args) {

 Function<String, String> userName = name -> name.substring(0, 4);
 Function<String, String> generateUserId = name -> name + name.length();

 // andThen()
 Function<String, String> userId = userName.andThen(generateUserId);
 System.out.println(userId.apply("Hariprasath")); // Hari4

 // compose()
 Function<String, String> userId2 = generateUserId.compose(userName);
 System.out.println(userId2.apply("Hariprasath")); // Hari4
 }
}

🔹 Consumer Chaining
 - A Consumer<T> performs an operation but returns nothing.
 Method:
 andThen() → Executes consumers sequentially
 Example:
 - Code Remaining in comment section 👁️‍🗨️

♻️Repost so others can learn and grow together.
 🔔 Follow Hariprasath V for daily Java, DSA, and System Design,Springboot,Microservices,Devops,Full Stack resources.


================================================

---

