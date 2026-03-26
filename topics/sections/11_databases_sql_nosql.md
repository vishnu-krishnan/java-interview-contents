<!-- Part of Java Learning Roadmap — Section 11 -->

# 🗄️ 11. Databases (SQL & NoSQL)

---

## 1. Definition

A **Database** is an organized collection of data. In modern backend engineering, they are split into two major categories:
1.  **SQL (Relational):** Data is stored in tables (rows and columns) with a strict schema. Focuses on data integrity and relational mapping (e.g., PostgreSQL, MySQL, Oracle). Follows **ACID**.
2.  **NoSQL (Non-Relational):** Data is stored in flexible formats (JSON documents, Key-Value pairs, Wide-Columns, Graphs). Focuses on massive horizontal scaling and fast unstructured reads/writes (e.g., MongoDB, Redis, Cassandra). Follows **BASE** and the **CAP Theorem**.

---

## 2. Why It Exists

*   **Data Persistence:** Applications lose state when restarted. Databases save state to disk safely.
*   **The SQL vs NoSQL split:** Relational DBs scale *vertically* (buying a bigger, more expensive server). When web traffic exploded (Google, Facebook), vertical scaling hit a physical limit. NoSQL was invented to scale *horizontally* (adding thousands of cheap, small servers together) by sacrificing strict relational rules.

---

## 3. How It Works Internally

### 3.1 SQL Data Integrity (ACID)
Relational DBs guarantee that transactions are safe using ACID:
*   **Atomicity:** "All or Nothing." If a transaction has 3 steps and step 3 fails, steps 1 and 2 are rolled back automatically.
*   **Consistency:** The database rules (constraints, foreign keys) are never violated before or after a transaction.
*   **Isolation:** Concurrent transactions don't interfere with each other. (Controlled via Isolation Levels like *Read Committed* or *Serializable*).
*   **Durability:** Once the DB says "Commit Successful", the data is permanently on disk, even if the power cord is immediately unplugged.

### 3.2 SQL Indexing (B-Trees)
Indexes map a column's value to its physical row location. Most SQL databases use a **B-Tree** (Balanced Tree) structure.
*   *Advantage:* Searching goes from O(N) (Full Table Scan) down to O(log N).
*   *Trade-off:* Every time you `INSERT`, `UPDATE`, or `DELETE`, the DB must physically update the B-Tree structure. Too many indexes severely degrade write performance.

### 3.3 NoSQL and The CAP Theorem
In a distributed (multi-server) system, you can only pick 2 of the following 3 guarantees:
1.  **Consistency:** Every read receives the most recent write. (All nodes have the exact same data instantly).
2.  **Availability:** Every request receives a non-error response. (The system never goes down).
3.  **Partition Tolerance:** The system continues operating even if the network fails between nodes.
*Because networks ALWAYS fail eventually, you must choose Partition Tolerance (P). You then decide if your NoSQL DB is CP (Consistent) or AP (Available).*

### 3.4 NoSQL Types
*   **Document:** (MongoDB) JSON-like (BSON) structures. Great for changing schemas.
*   **Key-Value:** (Redis) Extremely fast memory lookups. Used for caching.
*   **Column-Family:** (Cassandra) Stores data in massive column families. Perfect for heavy write loads (IoT, time-series data).
*   **Graph:** (Neo4j) Nodes and Edges. Used for social networks or recommendation engines.

---

## 4. Code Examples

### 4.1 Essential SQL Joins
```sql
-- Inner Join: Only rows where matching users AND orders exist
SELECT u.name, o.total 
FROM users u 
INNER JOIN orders o ON u.id = o.user_id;

-- Left Join: ALL users, even if they have NO orders (order columns will be NULL)
SELECT u.name, o.total 
FROM users u 
LEFT JOIN orders o ON u.id = o.user_id;
```

### 4.2 Creating an Index
```sql
-- Speeds up: SELECT * FROM users WHERE email = 'test@test.com'
CREATE INDEX idx_users_email ON users(email);
```

### 4.3 MongoDB Document (No Schema)
Unlike SQL, you can save varying data structures in the same MongoDB "Collection" (Table).
```json
// Document 1
{ "_id": 1, "name": "John", "age": 30 }

// Document 2 (Completely different structure, totally allowed)
{ "_id": 2, "name": "Jane", "hobbies": ["Running", "Java"], "manager": true }
```

### 4.4 Redis Caching (Key-Value)
```bash
# Set a user session that automatically deletes itself after 3600 seconds (1 hour)
SETEX session:12345 3600 "{'user':'admin'}"

# Retrieve it
GET session:12345
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| When would you choose NoSQL over SQL? | 1. Unstructured or rapidly changing data. 2. Need massive horizontal read/write scaling. 3. Data has no complex relationships (no multi-table JOINs needed). |
| What is Normalization? | Organizing SQL tables to reduce redundancy. **1NF:** Atomic values. **2NF:** 1NF + no partial dependencies. **3NF:** 2NF + no transitive dependencies (columns shouldn't depend on other non-key columns). |
| How do you find the 2nd highest salary in SQL? | `SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);` OR using Window functions: `SELECT salary FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank FROM employees) WHERE rank = 2;` |
| What is the N+1 Query Problem? | Occurs in ORMs (like Hibernate) where the system executes 1 query to fetch a list of N parent entities, and then executes N separate queries to fetch their children. Fix: Use `JOIN FETCH`. |
| Cache-Aside vs Write-Through? | **Cache-aside:** App checks cache; if miss, queries DB, updates cache. **Write-through:** App writes to Cache, and Cache writes to DB synchronously. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Indexing every column "to make it fast" | Completely destroys Database Write latency (Inserts take forever). Wastes massive disk space. | Only index columns used in `WHERE`, `JOIN`, or `ORDER BY` clauses. Don't index booleans. |
| Doing `SELECT *` in production | Pulls unnecessary data over the network, wasting RAM, Bandwidth, and CPU on both DB and Java App. | Explicitly name columns: `SELECT id, name FROM...` |
| Using NoSQL for Financial Ledgers | MongoDB/Cassandra don't have strict ACID guarantees across multi-document transactions by default. | Use SQL (PostgreSQL, MySQL) for strictly relational, transactional data (money handling). |

---

## 7. Real-World Usage

| Database | Primary Architecture Use Case |
|---|---|
| **PostgreSQL** | The modern default for core business data. ACID compliant, strict, supports advanced JSON querying internally. |
| **MongoDB** | Content Management Systems, User Profiles, Catalogs where the features/fields change every week. |
| **Redis** | High-speed cache sitting in front of PostgreSQL. Stores Rate Limiter counts, JWT Session tokens, and top 10 Leaderboards. |
| **Cassandra** | Apple/Netflix use it to store billions of event logs/metrics per minute. Writes are instantly fast across distributed clusters. |

---

## 8. Practice Tasks

1.  **Denormalization test:** Read about why a MongoDB database prefers "Denormalized" data (embedding orders directly into the User document) compared to SQL's "Normalized" data (putting orders in a separate Orders table).
2.  **Execution Plan:** Connect to any SQL database. Write a query with a `WHERE` clause on an unindexed column. Prefix the query with `EXPLAIN ANALYZE` (or just `EXPLAIN`) and look at the "Seq Scan" (Sequential Scan) warning. Add an index to that column and run `EXPLAIN` again to see the "Index Scan".
3.  **Redis LRU:** Research how to configure Redis with `maxmemory-policy allkeys-lru` so it automatically acts as a Least Recently Used cache when it runs out of RAM.

---

## 9. Quick Revision

### CAP Theorem Matrix
| Type | Guarantees | Example |
|---|---|---|
| **CA** | Consistency + Availability (Network never fails? Impossible in distributed) | Single-node PostgreSQL |
| **CP** | Consistency + Partition Tolerance (Will go down rather than serve stale data) | MongoDB, HBase |
| **AP** | Availability + Partition Tolerance (Will serve stale data to stay online) | Cassandra, DynamoDB |

### ACID vs BASE
*   **ACID (SQL):** Atomicity, Consistency, Isolation, Durability. Strict, safe.
*   **BASE (NoSQL):** Basically Available, Soft state, Eventual consistency. Fast, scaling.

### Query Tools
*   **`GROUP BY`** aggregates rows into groups.
*   **`HAVING`** filters *after* grouping (unlike `WHERE` which filters *before* grouping).
*   **`ORDER BY`** sorts the final output. Can use indexes to sort instantly.
