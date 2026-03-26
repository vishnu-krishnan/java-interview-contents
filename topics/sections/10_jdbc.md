<!-- Part of Java Learning Roadmap — Section 10 -->

# 🗄️ 10. Java Database Connectivity (JDBC)

---

## 1. Definition

**JDBC (Java Database Connectivity)** is a standard Java API (`java.sql` package) used to connect Java applications to Relational Databases (RDBMS) like MySQL, PostgreSQL, or Oracle. It acts as a middle layer, translating Java method calls into database-specific network protocols.

### Core Architecture
*   **JDBC API:** The interfaces provided by Java (`Connection`, `Statement`, `ResultSet`).
*   **JDBC Driver Manager:** The JVM component that matches connection requests to the right driver.
*   **JDBC Driver:** A vendor-specific `.jar` file (e.g., `mysql-connector-java.jar`) that actually implements the interfaces and contains the proprietary network logic to talk to that specific database.

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

### 3.2 Statement vs PreparedStatement
*   **`Statement`:** Sends raw strings to the DB. The DB optimizer has to compile the SQL execution plan every single time. Re-running the query with a different WHERE clause forces a recompile. Highly vulnerable to **SQL Injection**.
*   **`PreparedStatement`:** Sends a template to the DB (e.g., `SELECT * FROM users WHERE id = ?`). The DB compiles the execution plan *once* and caches it. You then send only the parameters individually over the network. Safe, faster, and prevents SQL injection because parameters are treated strictly as data, not executable code.

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

### 4.2 Manual Transaction Management
```java
try (Connection conn = DriverManager.getConnection(url, user, pwd)) {
    // Disable auto-commit to start a manual transaction
    conn.setAutoCommit(false); 

    try (PreparedStatement withdraw = conn.prepareStatement("UPDATE acct SET bal = bal-100 WHERE id=1");
         PreparedStatement deposit = conn.prepareStatement("UPDATE acct SET bal = bal+100 WHERE id=2")) {
        
        withdraw.executeUpdate();
        // What if the server crashes right here?
        deposit.executeUpdate();
        
        // Both succeeded, commit to disk
        conn.commit(); 
    } catch (SQLException ex) {
        // Something failed, undo everything!
        conn.rollback(); 
    }
}
```

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

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Forgetting to close Connections/ResultSets | Causes connection leaks. The DB maxes out its connection limit and the entire application freezes waiting for connections. | ALWAYS use `try-with-resources`. Even missing a `ResultSet.close()` can hold memory locks on the database server. |
| Using string concatenation for SQL | `SELECT * FROM users WHERE name = '` + name + `'` opens you to devastating SQL Injection attacks. | ALWAYS use `PreparedStatement` with `?` bind variables. |
| Opening a connection per user request | `DriverManager.getConnection()` takes ~50ms+ to handshake. Doing this per HTTP request kills throughput. | Use a **Connection Pool** (like HikariCP) in production. |

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
