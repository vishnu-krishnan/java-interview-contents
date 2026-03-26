<!-- Part of Java Learning Roadmap — Section 11 -->

## 🗄️ 8. Databases (SQL & NoSQL)

### 🗃️ SQL & Relational Databases

- Relational Database Concepts (Tables, Keys, Normalization — 1NF/2NF/3NF/BCNF)
- **Core SQL**
  - DDL: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
  - DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
  - `DELETE` vs `DROP` vs `TRUNCATE` — differences
  - Joins: `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, `SELF`, `CROSS`
  - Subqueries, Nested Queries, CTEs (`WITH` clause)
  - Aggregation: `GROUP BY`, `HAVING`, `ORDER BY`
  - `WHERE` vs `HAVING` — filtering rows vs groups
- **Window Functions**
  - `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`
  - `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`
- **Common SQL Interview Patterns**
  - 2nd / Nth highest salary — subquery + `LIMIT/OFFSET`
  - Find duplicates and delete keeping one
  - Top N records per group
  - Employees with no manager (self-join)
  - Average salary per department
- **Views** — virtual table, updatable views
- **Stored Procedures vs Functions**
- Indexing — B-Tree, Composite Index, Covering Index, `EXPLAIN` plan analysis
- Transactions — ACID properties, Isolation Levels (`READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`)
- **Database Design for Scale**
  - Sharding vs Partitioning (horizontal vs vertical)
  - Read-heavy vs Write-heavy system design
  - Read replicas
- Popular Databases: **MySQL**, **PostgreSQL**

### 🍃 NoSQL Databases

- Relational vs Non-Relational — when to choose
- Types of NoSQL
  - **Document Store**: MongoDB
  - **Key-Value Store**: Redis
  - **Column Family**: Apache Cassandra
  - **Graph DB**: Neo4j
- CAP Theorem — Consistency, Availability, Partition Tolerance
- **MongoDB**
  - Collections, Documents, BSON
  - CRUD Operations
  - Aggregation Pipeline
  - Indexing in MongoDB
- **Redis**
  - Caching Strategies — Cache-Aside, Write-Through, Write-Behind
  - Data Structures: Strings, Hashes, Lists, Sets, Sorted Sets
  - TTL (Time To Live) and Eviction Policies
  - Distributed Locking with Redis
- Consistent Hashing — distribution of data across nodes
- Database per Service pattern (Microservices)

---
