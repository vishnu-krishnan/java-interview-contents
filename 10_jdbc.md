<!-- Part of Java Learning Roadmap — Section 10 -->

# 🗄️ 10. Java Database Connectivity (JDBC)

---

### 1.1 The Bridge to the Data (JDBC Architecture)

**Core Idea:**
JDBC is the "Universal Translator." It allows your Java app to talk to $any$ database (SQL Server, MySQL, Oracle) using the same set of Java commands.

**Why it matters:**
Without JDBC, you would have to learn a different Java library for every single database. JDBC provides a **Standard Interface** (`java.sql`), so your code doesn't change when you switch from a dev H2 database to a production PostgreSQL database.

**When to use:**
*   When you need high-performance, raw access to a database.
*   When ORMs like Hibernate are "too heavy" or generate inefficient SQL for a complex report.
*   Building data migration tools or ETL pipelines.

**When NOT to use:**
*   In 90% of standard Spring Boot CRUD apps (use Spring Data JPA instead).
*   When you want automatic object mapping (JDBC requires manual `rs.getXXX()` calls).

**Example (Spring Boot):**
Spring Boot doesn't replace JDBC; it includes the `spring-boot-starter-jdbc` which wraps raw JDBC in a `JdbcTemplate` to handle the boring "Open/Close" boilerplate code for you.

**Deep Dive:**
The **Driver Manager** acts as a Matchmaker. When you provide a URL like `jdbc:mysql://...`, it searches your `@Classpath` for a Driver that says "I speak MySQL."
1.  **Driver JAR:** Contains the proprietary binary protocol of the DB.
2.  **Connection:** A physical TCP socket opened to the DB server.
3.  **Statement:** A "Message" sent over that socket.

**Advanced Insight:**
**SPI (Service Provider Interface).** In the old days (Java 5), you had to call `Class.forName()`. Now, the JVM automatically scans `META-INF/services/java.sql.Driver` inside your JARs to find and register drivers automatically.

**Pitfall:**
**Dependency Version Mismatch.** If your MySQL JAR is version 8 but your DB server is version 5, you might get mysterious "Handshake Failures" or `SQLException` errors that are hard to debug.

**Production Tip:**
Always use **Database Migrations** (like Flyway or Liquibase) to manage your schema changes. Never run raw `CREATE TABLE` scripts manually through JDBC in a production environment.

**Interview Trap:**
"If JDBC is database-independent, why do we still need different Driver JAR files?"
**Answer:** Because while the **Java Interface** is the same, the **Network Protocol** (the way the bytes move over the wire) is unique to every vendor. The Driver is the "Translation Layer" that knows the specific vendor's language.

---

## 2. Why It Exists

*   **Database Agnostic:** A developer writes SQL using standard Java `Connection` and `ResultSet` objects. If the company switches from MySQL to PostgreSQL, the Java code remains 99% identical; only the DB URL and the Driver JAR change.
*   **Foundation for ORMs:** Modern frameworks like Hibernate, JPA, and Spring Data JPA don't replace JDBC — they sit on top of it. They generate the SQL and call JDBC under the hood.

---

## 3. How It Works Internally

### 3.1 The Network Flow
1.  **Connection:** `DriverManager.getConnection()` triggers a highly expensive 3-way TCP/IP handshake with the database server, plus database authentication.
2.  **Execution:** The Java application sends a raw string (the SQL statement) over the network.
3.  **Result:** The database executes the SQL and streams the binary result back over the network.
4.  **Mapping:** `ResultSet.getString("name")` extracts the raw bytes and converts them into a Java String.

### 3.2 PreparedStatement (The Performance & Security Shield)

**Core Idea:**
A `Statement` is like sending a new handwritten letter every time. A `PreparedStatement` is a "Template" where you just fill in the blanks (`?`).

**Why it matters:**
Two reasons: **Speed** and **Safety**.
1.  **Speed:** The DB compiles the SQL "Execution Plan" once and reuses it for every set of data you send.
2.  **Safety:** It is the $only$ way to stop **SQL Injection**. The `?` parameters are sent as pure data; the DB never tries to "Execute" them.

**When to use:**
*   **Always.** Never use `Statement` in professional code unless you are building a tool that generates dynamic DDL (like `CREATE TABLE`).

**When NOT to use:**
*   There's almost zero reason to avoid them. Even for a single query, they are safer.

**Example (Security):**
```java
// VULNERABLE: user can input "' OR '1'='1" to steal all data
String sql = "SELECT * FROM users WHERE name = '" + name + "'"; 

// SECURE: The DB treats the ? as a literal string "name", not code.
String safeSql = "SELECT * FROM users WHERE name = ?";
```

**Deep Dive:**
When you call `conn.prepareStatement(sql)`, the JDBC driver sends the SQL string to the DB immediately. The DB "Parses" it, creates an "Execution Plan," and gives it a unique ID. When you call `pstmt.executeQuery()`, only the **ID and the parameters** are sent over the network.

**Advanced Insight:**
**Server-side vs Client-side Ps.** Some drivers (like MySQL) might mock PreparedStatements by just doing string replacement on the client-side unless you set `useServerPrepStmts=true`. For maximum performance, ensure the DB itself is handling the template.

**Pitfall:**
**One-Indexed Pain.** In Java, `ResultSet` column indexes and `PreparedStatement` parameter indexes start at **1**, not 0. If you use `pstmt.setString(0, "A")`, you will get a `SQLException`.

**Production Tip:**
Use **Named Parameters** (via Spring's `NamedParameterJdbcTemplate`) if your query has 10+ parameters. It's much harder to mess up `:userId` than it is to track the 7th `?` in a long SQL string.

**Interview Trap:**
"Does a `PreparedStatement` always run faster than a `Statement`?"
**Answer:** **Usually, but not always.** On the very first execution, it might be slightly slower because of the extra round-trip to "Prepare" the statement. The performance gain comes on the **second** and subsequent executions.

---

## 4. Code Examples

### 4.1 The Complete JDBC Flow (Java 7+ try-with-resources)
```java
String url = "jdbc:postgresql://localhost:5432/mydb";
String user = "admin";
String pwd = "password";
String query = "SELECT id, name FROM users WHERE age > ?";

// 1. Establish connection (AutoClosed)
try (Connection conn = DriverManager.getConnection(url, user, pwd);
     // 2. Prepare Statement (AutoClosed)
     PreparedStatement pstmt = conn.prepareStatement(query)) {

    // 3. Bind parameters (1-indexed!)
    pstmt.setInt(1, 18);

    // 4. Execute Query & process ResultSet (AutoClosed)
    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
            int id = rs.getInt("id");
            String name = rs.getString("name");
            System.out.println("User: " + id + " - " + name);
        }
    }
} catch (SQLException e) {
    e.printStackTrace();
}
```

### 4.2 ACID Transactions & Reliability

**Core Idea:**
A transaction is an "All or Nothing" operation. If you are moving money from Bank ID 1 to Bank ID 2, you want $both$ updates to succeed, or $neither$ of them.

**Why it matters:**
In a distributed system, a server crash or network failure in the middle of a process can leave your data in a "Corrupted" state (money gone from ID 1 but not arrived in ID 2). Transactions prevent this.

**When to use:**
*   Every time you perform multiple `INSERT`, `UPDATE`, or `DELETE` operations that represent a single business unit of work.

**When NOT to use:**
*   For simple, single `SELECT` statements (the DB handles those automatically).

**Example (Bank Transfer):**
The code starts with `conn.setAutoCommit(false)`. We run the withdraw, then the deposit. If anything fails (a `RuntimeException`), we call `rollback()`. If everything finishes perfectly, we call `commit()`.

**Deep Dive:**
JDBC transactions are bound to the **Connection**. Every command on that connection is part of the same transaction until you commit it.
*   **Dirty Read:** Seeing data from another transaction that hasn't committed yet (Dangerous!).
*   **Phantom Read:** Seeing a different number of rows when you run the same query twice.

**Advanced Insight:**
**Isolation Levels.** You can set how "private" your transaction is using `conn.setTransactionIsolation()`. `READ_COMMITTED` is the industry standard for most apps, balancing speed and safety.

**Pitfall:**
**Transaction Timeout.** If a transaction stays open too long (waiting for a slow API call), it holds **Database Locks**. This will cause other users to hang and can eventually crash the DB's lock table. **Never do I/O or network calls inside a DB transaction.**

**Production Tip:**
In Spring Boot, never manage transactions manually with JDBC. Use `@Transactional`. It uses the **Proxy Pattern** to automatically handle the `commit` and `rollback` logic for you.

**Interview Trap:**
"What happens to an open transaction if the DB connection is closed before a commit?"
**Answer:** It depends on the vendor, but in almost all modern databases (Oracle, Postgres), an uncommitted transaction is **automatically rolled back** for safety.

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `execute()`, `executeQuery()`, and `executeUpdate()`? | `execute()` returns boolean (true if result is a ResultSet, false if update count). `executeQuery()` returns a `ResultSet` (for SELECTs). `executeUpdate()` returns an `int` representing rows affected (for INSERT/UPDATE/DELETE). |
| What is SQL Injection and how do you prevent it? | A hacking technique where malicious SQL code is injected into user input (e.g., `name = "admin' OR '1'='1"`). Prevented purely by using `PreparedStatement` which escapes inputs as literal data rather than executable script. |
| What are the types of `ResultSet`? | Type-Forward-Only (default, cursor moves only forward), Scroll-Insensitive (can go backward, doesn't see DB updates made by others), Scroll-Sensitive (sees DB updates live). |
| How do you insert multiple rows efficiently? | Use `PreparedStatement.addBatch()` in a loop, then call `executeBatch()`. It sends all queries to the DB in one single network round trip. |
| Why is `Class.forName("com.mysql.jdbc.Driver")` no longer needed? | Since JDBC 4.0 (Java 6), the API uses the Service Provider Interface (SPI) to automatically discover and load drivers found on the classpath. |

---

### 4.3 Connection Pooling (The Performance Engine)

**Core Idea:**
Opening a DB connection is like "Hiring a new employee"—it's slow and expensive. A Connection Pool is a "Staff Room" of 10 employees already hired and waiting to work.

**Why it matters:**
Opening a TCP connection + SSL handshake + DB Auth takes ~50ms-100ms. If your app handles 100 requests/sec, opening 100 connections would waste 10 seconds of CPU time just on "Hello." A pool makes it **0.1ms**.

**When to use:**
*   **Always** in a production Web App or Microservice.

**When NOT to use:**
*   In a simple one-off CLI script or migration tool that runs once and exits.

**Example (HikariCP):**
Spring Boot uses **HikariCP** by default. It’s so fast because it uses specialized Java Bytecode and low-level array structures to avoid "Lock Contention" when multiple threads ask for a connection at the same time.

**Deep Dive:**
1.  **Borrow:** Thread asks the Pool for a connection.
2.  **Use:** Thread runs SQL queries.
3.  **Return:** Thread calls `conn.close()`. The pool intercepts this call and *doesn't* close the connection; it just puts it back in the "Available" list.

**Advanced Insight:**
**Deadlocks.** If you have 10 threads but your pool size is only 5, and all 10 threads try to grab two connections each (Transaction nesting), the entire app will "Deadlock" and stop responding.

**Pitfall:**
**Leaking Connections.** If you forget to call `close()` (or don't use try-with-resources), the connection stays "In Use" in the pool forever. Eventually, the pool runs out, and all future requests fail with "Connection not available."

**Production Tip:**
**Pool Sizing.** Don't set a massive pool size (like 500). Most DBs perform $worse$ with 500 active connections due to Disk I/O contention. For most microservices, a pool size of **10-20** is actually faster than 100!

**Interview Trap:**
"If I call `connection.close()` while using a Connection Pool, does it actually close the network socket?"
**Answer:** **No.** The pool provides a "Proxy" connection. The `close()` method is intercepted to return the connection to the pool. To actually kill the socket, you would have to shut down the entire Pool.

---

## 7. Real-World Usage

| Tool | Where it shows up |
|---|---|
| **Connection Pooling (HikariCP)** | Rather than opening/closing connections 1000 times a second, a Web Server pre-opens a "Pool" of 20 connections. A thread borrows one, runs SQL, and hands it back. HikariCP is the default pool in Spring Boot due to its extreme lightweight performance. |
| **Spring `JdbcTemplate`** | A wrapper class around pure JDBC that eliminates the `try...catch...finally` boilerplate and automatically maps `ResultSet` rows into Java Objects using row mappers. |
| **Pessimistic Locking** | Running `SELECT * FROM orders WHERE id=5 FOR UPDATE` via JDBC to force the database to lock the row, preventing concurrent web servers from altering the order simultaneously. |

---

## 8. Practice Tasks

1.  **CRUD Operations:** Create a raw JDBC application (no Spring/Hibernate) that connects to a local database. Create a `students` table, Insert 3 records, Select them and print, Update one, and Delete one.
2.  **Batch Processing Benchmark:** Using a `for` loop, insert 10,000 rows into a table executing `.executeUpdate()` every time. Measure the speed. Then, change the code to use `.addBatch()` inside the loop and `executeBatch()` at the end. Compare the speed difference. (It will be massive).
3.  **SQL Injection Sim:** Create a `Statement` query: `"SELECT * FROM users WHERE name = '" + userInput + "'"`. Set `userInput` to `' OR 1=1 --`. Observe how it returns the entire database table.

---

## 9. Quick Revision

```
JDBC Architecture: Java App -> JDBC API -> DriverManager -> Vendor Driver -> Database

Connections: Extremely heavy. Use HikariCP for connection pooling.
Resources: Use try-with-resources immediately to auto-close Connection, Statement, and ResultSet.

Statement Types:
- Statement: Raw SQL, slow plan compilation, vulnerable to injection.
- PreparedStatement: Parametrized (?), compiled once, defeats injection, safe.
- CallableStatement: Used exclusively to call Database Stored Procedures.

Execution Types:
- executeQuery() → Returns `ResultSet` (SELECT).
- executeUpdate() → Returns `int` (INSERT/UPDATE/DELETE).

Transactions:
- default behavior: Autocommit = true (every SQL is committed instantly).
- safe behavior: setAutoCommit(false) -> execute -> commit() or rollback().
```
