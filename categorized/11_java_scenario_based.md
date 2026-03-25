

## 🔹 Interview Question: What is the transient keyword in Java?
Me:
The transient keyword in Java is used to indicate that a field should NOT be serialized.
🧠 First, what is Serialization?
Serialization is the process of converting an object into a format (byte stream / JSON) so that it can be:
- Saved to a file
- Sent over the network
- Stored in a database
🎁 Real-Life Analogy
Imagine you want to send a gift to a friend who lives far away.
You:
📦 Pack the gift
🔒 Seal the box
🚚 Send it via delivery
This process is similar to Serialization.

When your friend receives it:
📦 Opens the box
🎁 Restores the gift
This is Deserialization.

💻 Example in Java
public class Employee {
 private long id;
 private String name;
 private String department;

 private transient BigDecimal salary;

 // getters & setters
}
Here, the salary field is marked as transient.
- This means:
It will NOT be included during serialization
After deserialization, its value will be default (null / 0)
⚙️ Where is this useful?
We use transient when:
- Data is sensitive (e.g., salary, passwords)
- Data is temporary / derived
- Data is not required to persist or transfer

🔄 Example with JSON (Jackson / Gson)
When converting object → JSON:
{
 "id": 1,
 "name": "John",
 "department": "Engineering"
}
- Notice that salary is NOT present.
🚀 Key Takeaway
transient helps control what should NOT travel with your object when it is serialized.
A small keyword, but very important in real-world backend systems and interviews.

---



## Recently I attended a Java Backend Developer interview (4+ years experience). Sharing some of the questions that were asked. Hope it helps others preparing for similar roles.

Round 1 – Coding + Core Java + Spring Boot
Duration (40 mins)

- Find the first non-repeated character in a string
- OOPs concepts in detail (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Coding question: Can a private method in parent be overridden in child? Explain with code
- Method overloading in child class – coding example
- Connection Pooling in Java / Spring Boot
- Spring Boot Bean Lifecycle
- Difference between @Component and @Service

Round 2 – Advanced Java + Coding + System Design
(Duration 1hr 20 minutes)

- OOPs concepts discussion
- REST APIs concepts and best practices
- Type Erasure in Generics (Java Generics concept)
- Coding problem: Sort strings by length, and if length is same sort alphabetically
- What will be the output of:
"String str = "java.code"
"str.replaceAll(".", "__");"
- Immutable class in Java – how to design
- Singleton class implementation
- In constructor, can we write logic other than initializing fields?
- Design patterns used in your projects
- Fault tolerance – Circuit Breaker pattern in Microservices
- SQL Question: Find average salary and 2nd highest average salary
- How to use @EmbeddedId in JPA
- How to resolve NoUniqueBeanDefinitionException.

And many cross questions.

Round 3 - Hackerrank Assessment

- Functionality implmentation based on Oops concept successfully completed.
- Medium level question 4 out of 7 test case passed.

Round 4 - Management round.
Project Related and tech stack related questions.

Result - REJECTED .

Despite the good interview where 80-85% questions i answered correctly I was not able to clear.

Learning - Sometimes your best interview also can lead to rejection so just focus on next interview rather than thinking about previous Results 😊

Hope this helps Java developers preparing for backend interviews.

---



## Want Cleaner, Faster Java Code? Start Here.

---

