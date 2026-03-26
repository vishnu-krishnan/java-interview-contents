## JAVA INTERVIEW SCENARIO:

The interviewer says:

“Let’s see how you debug real problems in Java.”

- Your Java service starts throwing OutOfMemoryError even though heap size looks sufficient. Why?

Answer:
- Memory leak due to objects being referenced (not eligible for GC)
- Large number of objects created and retained in collections
- Improper use of caches without eviction
- High GC pressure causing memory not being freed efficiently
---
## Refactoring in Java isn’t “clean-up”.
It’s how you keep change cheap.

Here are 5 Java refactoring moves I use constantly (with quick examples):
- Extract Method (name the intent)
 Before: one 60-line method
 After: subtotal(), applyVipDiscount(), priceWithTaxIfNeeded()

- Kill boolean flags
 Before: generate(true)
 After: generateSummary() / generateDetailed()

- Replace switch with Strategy
 Before: switch(shippingMethod)
 After: ShippingPolicy.cost(order) implementations

- Replace primitives with Value Objects
 Before: createUser(String email)
 After: createUser(new Email(email)) (validation lives in one place)

- Separate domain logic from infrastructure
 Before: “God service” does everything
 After: domain objects own rules, service only orchestrates

Refactor like a professional:
 ✅ small steps
 ✅ tests/characterisation tests
 ✅ behaviour stays the same

What refactor gives you the biggest win in real production code?
---
## One method in my Java demo app was using 71% of CPU. The code looked perfectly fine. After my DevNexus talk, attendees kept asking about the specific anti-patterns. This post shows eight patterns that compile fine, pass code review, and silently kill performance.

Before/after: 1,198ms → 239ms. 85K → 419K orders/sec. 19 GC pauses → 4.

Shoutout to Vinicius Senger for bringing me into his DevNexus talk on Java modernization, this series wouldn't exist without that.
---
## “I thought I knew Strings… until my recent interviews proved me wrong!” 😅

During my recent #Java developer interviews (while switching jobs), I was hit with some deceptively simple-looking String questions —
but trust me, they test how deeply you understand memory, immutability, and the String Pool.

Check these out 👇 — can you guess the outputs? 🤔

1️⃣ String s1 = "Java";
 String s2 = "Java";
 System.out.println(s1 == s2);

2️⃣ String s1 = new String("Hello");
 String s2 = "Hello";
 System.out.println(s1 == s2);

3️⃣ String s1 = "Java";
 String s2 = "Ja" + "va";
 System.out.println(s1 == s2);

4️⃣ String s1 = "Ja";
 String s2 = s1 + "va";
 System.out.println("Java" == s2);

5️⃣ String s1 = "abc";
 s1.concat("xyz");
 System.out.println(s1);

6️⃣ String s1 = "abc";
 s1 = s1.concat("xyz");
 System.out.println(s1);

7️⃣ String s1 = "HELLO";
 String s2 = s1.toLowerCase();
 System.out.println(s1 == s2);

8️⃣ String s1 = new String("Java");
 String s2 = s1.intern();
 System.out.println(s1 == s2);

💥 Most developers fail these not because of logic — but because they don’t truly get how JVM handles Strings internally.

Thanks Vipul Tyagi for ur Detailed Explanation ✨
---
## 2) Your Java application shows high GC activity and performance drops. Why?

Answer:
- Excessive object creation increasing GC pressure
- Short-lived objects flooding the heap
- Improper memory allocation patterns
- Large objects frequently created and discarded
---
## 🔹 2. Class Loading

The JVM loads classes using the ClassLoader subsystem.

- Bootstrap ClassLoader → loads core Java classes
- Platform ClassLoader → loads JDK libraries
- Application ClassLoader → loads your Spring Boot classes

Class metadata is stored in Metaspace.
---
## 🔹 3. Bytecode Verification

Before execution, the JVM verifies bytecode to ensure:

✔ Type safety
✔ Stack safety
✔ No illegal memory access

This protects the JVM from invalid code.