<!-- Part of Java Learning Roadmap — Section 23 -->

## 🏗️ 21. System Design (HLD)

- **Core Concepts**
  - Horizontal vs Vertical Scaling
  - Load Balancing — round-robin, least connections, consistent hashing
  - CDN — static asset distribution
  - **Caching** — Cache-Aside, Write-Through, Write-Behind, Read-Through
  - Message Queues — decouple producers and consumers
  - **API Gateway** — single entry point, routing, auth, rate limiting
  - **Circuit Breaker** — prevent cascading failures
  - Service Discovery — dynamic service location
- **Database Design for Scale**
  - Sharding (horizontal partitioning) — shard key selection
  - Partitioning — range, hash, list
  - Read replicas — scale reads
  - Consistent Hashing — minimize resharding on node change
  - Rate Limiting design — token bucket, sliding window log
- **CAP Theorem** — tradeoffs in distributed systems
- **Design Principles**
  - Idempotency — safe to retry
  - Exactly-once processing
  - Backpressure — producer vs consumer speed mismatch
  - Graceful degradation
- **Common HLD Interview Problems**
  - URL Shortener (TinyURL)
  - Notification System (email/SMS/push at scale)
  - Chat Application (WhatsApp-like)
  - Payment Processing System
  - Rate Limiter
  - Distributed Job Scheduler
  - Real-time Analytics Platform
  - API Gateway design

---
