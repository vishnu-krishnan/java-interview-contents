<!-- Part of Java Learning Roadmap — Section 23 -->

# 🏗️ 23. System Design (HLD)

---

## 1. Definition

**High-Level Design (HLD)** is the architecture of how a large-scale system is structured. It is the big picture. Instead of writing Java code to sort an array, HLD asks: "How do you design a system like Netflix that streams video to 100 million users worldwide without crashing?"

It consists of arranging major building blocks:
*   Load Balancers (Nginx, AWS ALB)
*   Application Servers (Tomcat / Spring Boot)
*   Databases (PostgreSQL / MongoDB)
*   Caches (Redis / Memcached)
*   Message Queues (Kafka / RabbitMQ)
*   Content Delivery Networks (Cloudflare CDN)

---

## 2. Why It Exists

*   **Scalability:** A single Web Server and a single Database will crash if traffic spikes from 1,000 to 1,000,000 users. HLD strategies allow you to handle massive traffic.
*   **High Availability (HA):** Hard drives fail. Datacenters catch on fire. Proper HLD ensures there is no **Single Point of Failure (SPOF)**. If a server physically dies, the system instantly reroutes traffic and stays online 99.99% of the year.
*   **Latency:** Users abandon apps if they take > 3 seconds to load. HLD uses CDNs and edge caching to serve data to a user in Tokyo from a server geographically located in Tokyo, not New York.

---

## 3. How It Works Internally

### 3.1 Scaling Up vs Scaling Out
*   **Vertical Scaling (Up):** Taking your 16GB RAM server, turning it off, and upgrading the motherboard to 128GB RAM. Pro: Zero code changes. Con: Has a hard physical limit, very expensive, causes downtime.
*   **Horizontal Scaling (Out):** Keeping your 16GB server, and buying 9 more identical 16GB servers. You put a Load Balancer in front of all 10. Pro: Infinite scalability, highly available. Con: Your Java application must now be **Stateless** (session data must live in Redis, not JVM memory).

### 3.2 Database Scaling
Web traffic is usually 90% Reads and 10% Writes.
*   **Read Replicas:** You have 1 "Master" DB that accepts all `INSERT`/`UPDATE` traffic. It instantly clones its data to 5 "Slave/Replica" DBs. All `SELECT` queries are routed to the 5 Replicas, instantly quintupling your read performance.
*   **Sharding:** When the data gets so big (10 Terabytes) that it won't fit on one hard drive. You split the table horizontally. Users A-M are stored physically on Server 1. Users N-Z are stored on Server 2. Extremely complex to manage query joins.

### 3.3 Consistent Hashing
If you have 4 Redis servers holding your cache, a standard hash `user_id % 4` decides which server holds the data. If Server #2 crashes, the math becomes `user_id % 3`. Suddenly, *every single user's data maps to a different server*, causing a 100% cache miss rate and crashing the system (Thundering Herd).
**Consistent Hashing** maps servers and keys onto a virtual circle (a Hash Ring). If a server crashes, only the keys belonging to that specific server are remapped to its neighbor. 90% of the cache remains perfectly valid.

---

## 4. Code Examples

### 4.1 Nginx Load Balancer Configuration
A Load Balancer sits at the edge of your network and distributes traffic.
```nginx
# Round-Robin Load Balancing across 3 Spring Boot servers
upstream backend_servers {
    server 10.0.0.1:8080;
    server 10.0.0.2:8080;
    server 10.0.0.3:8080;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend_servers;
    }
}
```

### 4.2 The "Cache-Aside" Pattern (Pseudocode)
The most common way to build highly scalable reads.
```java
public User getUserProfile(String userId) {
    // 1. Ask Redis cache first
    User user = redis.get("user:" + userId);
    
    if (user == null) {
        // 2. Cache Miss! Query the slow PostgreSQL DB
        user = database.query("SELECT * FROM users WHERE id = ?", userId);
        
        // 3. Save the result in Redis so the next API call is instantly fast
        // Important: Set a TTL (Time To Live) so the cache clears itself eventually
        redis.set("user:" + userId, user, "1_HOUR");
    }
    
    return user;
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Design a URL Shortener (like bit.ly)? | **Requirements:** Fast redirect, 1 billion links. **Design:** User inputs long URL. API server generates a unique short 7-char Base62 string (using a Snowflake ID generator). Saves `[short_code : long_url]` to a NoSQL DB (Cassandra). When another user hits the short URL, API looks it up, and returns HTTP 301 Redirect to the long URL. Heavily Cache the lookups in Redis! |
| What is a Single Point of Failure (SPOF)? | A component of the system that, if it fails, stops the entire system from working. (e.g., You have 10 Web Servers, but only 1 Database. If the DB dies, the whole site is down). Fix: Replication. |
| Difference between Throughput and Latency? | **Latency:** How long it takes one single user request to finish (e.g., 20ms). **Throughput:** How many requests the system can handle simultaneously per second (e.g., 5,000 TPS). |
| How do you handle database replication lag? | Because Master clones to Replicas asynchronously, if a user updates their password on the Master and instantly logs in hitting a Replica, the Replica might not have the new password yet (Replication Lag). Fix: Route all reads from the *same user* to the Master for 1 minute after they perform a write. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Designing distributed systems perfectly synchronously | User registers. Thread waits: 1s to save DB -> 3s to email user -> 2s to ping Salesforce. The user stares at a loading spinner for 6 seconds. | Add a **Message Queue** (Kafka). Save user to DB (100ms), dump `UserRegisteredEvent` on Kafka (10ms), return HTTP 200 instantly (110ms). Asynchronous workers send the email later. |
| Premature Optimization | Adding Microservices, Sharding, and Kafka on Day 1 for a startup with 50 total users. Development slows to a crawl. | Use a Monolith and a single PostgreSQL DB. 99% of companies never hit the scale requiring DB sharding. |
| Ignoring Network Unreliability (Fallacies of Distributed Systems) | Assuming `restTemplate.getForObject()` will always succeed in less than 50ms. | Networks drop packets constantly. Add Timeouts to EVERY network call, use Circuit Breakers, and implement Idempotent Retries. |

---

## 7. Real-World Usage

| Component | Where it shows up |
|---|---|
| **Content Delivery Network (CDN)** | Netflix uses Open Connect (their CDN framework) to store identical copies of *Stranger Things* on servers inside the physical ISP buildings (like Comcast) around the globe. You don't stream it from Netflix's core servers in Virginia; you stream it from a cached box 5 miles from your house. |
| **Rate Limiter** | Twitter API allows 100 tweets per hour. They use Redis with a "Token Bucket" algorithmic script. Every web request checks Redis. If the bucket is empty, API returns `HTTP 429 Too Many Requests`. |
| **Distributed Metrics (Snowflake ID)** | You can't use `id INT AUTO_INCREMENT` in SQL if you have 5 separate databases holding the shards, because 2 DBs will both generate `id=1`. Twitter invented "Snowflake IDs" — a 64-bit integer combining the Timestamp + Datacenter ID + Server ID + Sequence Number to guarantee a globally unique, sortable ID across thousands of servers. |

---

## 8. Practice Tasks

1.  **Architecture Diagramming:** Go to `draw.io` or `excalidraw`. Draw a high-availability architecture for an Instagram clone. Assume 1 Million Daily Active Users. Include an ALB, Web Servers, an Image Storage layer (S3), a generic CDN, a Relational DB for user metadata, and a Cache layer for the timeline feed. Add arrows detailing the data flow when a user uploads a photo.
2.  **Latency Math:** Learn the standard "Latency Numbers Every Programmer Should Know": Reading 1MB from RAM (250us), Reading 1MB from an SSD disk (1,000us), Sending a packet from California to Europe and back (150,000us). Play with visualizing why Caching is mandatory on a global level.

---

## 9. Quick Revision

### HLD Master Principles
*   **Scale Out, not Up.** Add more cheap servers, not one expensive super-server.
*   **Stateless is King.** A request can safely hit *any* web server if the server holds no session state.
*   **Decouple heavily.** Use Message Queues so spikes in traffic don't crush synchronous APIs.
*   **Cache everything.** Hit the disk only when absolutely necessary.

### 5 Critical HLD Terms
1.  **CAP Theorem:** Consistency, Availability, Partition Tolerance (Pick 2).
2.  **SPOF:** Single Point of Failure (Kill it with redundancy).
3.  **Sharding:** Splitting a DB table into pieces across multiple servers.
4.  **CDN:** Edging static assets (images/js) physically closer to users.
5.  **Round-Robin:** Simplest load balancer algorithm. Server 1, then 2, then 3, then 1...
