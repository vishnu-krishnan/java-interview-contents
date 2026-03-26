<!-- Part of Java Learning Roadmap — Section 21 -->

## 📨 19. Apache Kafka & Messaging

### Apache Kafka

- **Architecture**
  - Broker, Topic, Partition, Offset, Producer, Consumer, Consumer Group
  - Replication Factor and ISR (In-Sync Replicas)
  - Zookeeper vs KRaft (Kafka Raft — modern mode)
- **Producer**
  - `KafkaProducer`, `ProducerRecord`
  - Acks — `0` (fire-and-forget), `1` (leader), `all` (all ISR)
  - Idempotent producer
- **Consumer**
  - `KafkaConsumer`, `@KafkaListener` in Spring Boot
  - Consumer groups — partition assignment
  - Offset management — auto commit vs manual commit
  - Rebalancing — what happens to offsets
- **Delivery Semantics**
  - At-most-once — message may be lost
  - At-least-once — message may duplicate
  - Exactly-once — idempotent + transactional
- **Dead Letter Queue (DLQ)** — handling poison messages
- **Kafka Streams** — real-time stream processing
- **Schema Registry + Avro** — schema evolution
- **Kafka Lag** — difference between produced and consumed offsets
- **Retention Policy** — time-based or size-based
- **Spring Boot Kafka Integration**
  - `spring-kafka`, `spring.kafka.bootstrap-servers`
  - `@KafkaListener`, `KafkaTemplate`
  - Error handling, retry, DLQ configuration

### RabbitMQ vs Kafka

| Aspect | RabbitMQ | Kafka |
|---|---|---|
| Role | Message Broker | Event Streaming Platform |
| Storage | Temporary | Persistent (retention-based) |
| Replay | Limited | Native (replay anytime) |
| Throughput | Medium | Extremely High |
| Routing | Strong (Exchanges) | Simple (Topics + Partitions) |
| Consumer Model | Push-based | Pull-based |
| Best For | Task queues, workflows | Streaming, analytics, event sourcing |

### Other Messaging
- **JMS** (Java Message Service) — `ActiveMQ`
- **RabbitMQ** — Exchanges (direct, topic, fanout), Queues, AMQP

---
