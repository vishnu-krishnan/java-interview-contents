<!-- Part of Java Learning Roadmap — Section 20 -->

## 🌐 18. Microservices Architecture

- **Monolith vs Microservices** — tradeoffs, when to choose
- **Core Principles** — single responsibility, loose coupling, independent deployment
- **Service Communication**
  - Synchronous: REST (`RestTemplate`, `WebClient`), **Feign Client**
  - Asynchronous: Kafka, RabbitMQ, JMS
  - gRPC — high-performance RPC
- **API Gateway**
  - Spring Cloud Gateway, Nginx
  - Routing, rate limiting, auth enforcement, load balancing
- **Service Discovery**
  - Eureka (Netflix OSS), Consul
  - Client-side vs server-side discovery
- **Resilience Patterns**
  - **Circuit Breaker** — Resilience4j (`@CircuitBreaker`, CLOSED → OPEN → HALF-OPEN)
  - **Retry** with exponential backoff
  - **Bulkhead** — isolate failures
  - **Timeout** — prevent thread blocking
  - **Fallback** — graceful degradation
- **Distributed Transactions**
  - Why 2PC (Two-Phase Commit) is hard in microservices
  - **Saga Pattern**
    - Choreography — event-driven, no central coordinator
    - Orchestration — central saga orchestrator
- **CQRS** (Command Query Responsibility Segregation) — separate read/write models
- **Event-Driven Architecture**
  - Event sourcing — store events as source of truth
- **Data Management**
  - Database per Service pattern
  - Eventual consistency
  - Distributed Locking (Redis `SETNX`, Redisson)
- **Security in Microservices**
  - JWT + OAuth2 (Authorization Server, Resource Server)
  - API Gateway-level auth
  - mTLS (Mutual TLS) for service-to-service
- **Configuration Management**
  - Spring Cloud Config Server
  - Centralized vs per-service config
- **Distributed Tracing**
  - Zipkin, Jaeger, OpenTelemetry
  - Correlation IDs, trace/span IDs
- **Idempotency** — ensure exactly-once processing
- **Rate Limiting & Throttling** — token bucket, sliding window

---
