<!-- Part of Java Learning Roadmap — Section 21 -->

# 📨 21. Apache Kafka & Messaging

---

## 1. Definition

**Apache Kafka** is a distributed, high-throughput, low-latency event streaming platform. At its core, it is a highly scalable **distributed commit log**. 
Instead of sending a direct REST API call from Service A to Service B, Service A produces an "Event" to a Kafka **Topic**. Service B (and C, and D) actively listens to that Topic and consumes the event whenever it is ready.

---

## 2. Why It Exists

*   **Total Decoupling:** If the `PaymentService` is offline, and `OrderService` uses a REST API to call it, the Order fails. With Kafka, `OrderService` just dumps an `OrderCreatedEvent` onto Kafka and returns HTTP 200 to the user instantly. When `PaymentService` reboots 3 hours later, it picks up the message from Kafka. Zero data is lost.
*   **Massive Throughput:** Kafka can handle millions of messages per second by writing them directly to the file system sequentially (bypassing slow random-disk-seeking).
*   **Event Sourcing & Replay:** Unlike RabbitMQ where messages are deleted after being read, Kafka keeps messages on disk for days/weeks. A new microservice can be deployed today, connect to Kafka, and "replay" the last 30 days of historical events from scratch.

---

## 3. How It Works Internally

### 3.1 Topics, Partitions, and Offsets
A **Topic** (like `user-logins`) is a logical category. To scale horizontally, a Topic is divided into **Partitions** spread across multiple physical servers (**Brokers**).
Messages are appended to a Partition in order. Each message gets a permanent, sequential ID called an **Offset**. Order is *only* guaranteed within a specific partition, not across the whole topic!

### 3.2 Consumer Groups
If you have a massive topic and 1 Consumer instance doing the reading, it will fall behind.
You spin up 5 identical instances of `EmailService` and put them in the same `Consumer Group`. Kafka automatically assigns different Partitions to different instances in the group. If an instance crashes, Kafka performs a **Rebalance**, moving its partitions to the surviving instances.
*Rule:* You cannot have more consumers in a group than you have partitions!

### 3.3 Reliability and ACKs
When a Producer sends a message, how does it know it arrived safely?
*   `acks=0`: Fire and forget. Maximum speed, high data loss risk.
*   `acks=1`: The Leader broker acknowledged it. Moderate speed, slight risk if the leader crashes before replicating.
*   `acks=all`: The Leader *and* all Follower brokers acknowledged it. Slowest, but mathematically guarantees zero data loss (Enterprise default for financial data).

---

## 4. Code Examples

### 4.1 Sending a Message (Spring Boot)
```java
@Service
public class OrderProducer {

    private final KafkaTemplate<String, OrderEvent> kafkaTemplate;

    public OrderProducer(KafkaTemplate<String, OrderEvent> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void createOrder(OrderEvent event) {
        // The Key (event.getUserId()) is crucial! 
        // Kafka hashes the Key to ensure all orders for the SAME user 
        // go to the EXACT SAME partition, guaranteeing ordering for that user.
        kafkaTemplate.send("orders-topic", event.getUserId(), event);
    }
}
```

### 4.2 Consuming a Message (Spring Boot)
```java
@Service
public class EmailConsumer {

    // Automatically connects to Kafka, assigns partitions, and listens poll-loop
    @KafkaListener(topics = "orders-topic", groupId = "email-service-group")
    public void consume(ConsumerRecord<String, OrderEvent> record, Acknowledgment ack) {
        
        System.out.println("Processing order: " + record.value().getOrderId());
        
        sendWelcomeEmail(record.value().getUserEmail());

        // Manual ACK: Tells Kafka "I successfully processed this offset."
        // If an exception occurs before this line, Kafka will re-deliver the message.
        ack.acknowledge(); 
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Kafka vs RabbitMQ? | **Kafka** is a persistent, distributed append-only log, optimized for massive data streaming and replay ("Pull" model). **RabbitMQ** is a traditional message broker optimized for complex routing rules and task queues where messages are deleted immediately after reading ("Push" model). |
| What is a "Poison Pill" in Kafka? | A message on a topic that the consumer's deserializer (e.g., Jackson JSON) cannot parse. The consumer throws an Exception, fails to ACK, and reads the *exact same broken message* on the next loop, getting stuck in an infinite crash loop. |
| How do you guarantee Message Ordering? | Post the message with a specific **Key** (e.g., `userId`). Kafka hashes the key and routes all messages with that key to the *same* partition. Since order is guaranteed within a single partition, all events for that user process strictly in order. |
| Difference between At-Most-Once and At-Least-Once delivery? | **At-Most-Once:** Consumer ACKs the message the millisecond it receives it, *then* processes it. If the CPU crashes during processing, the message is lost forever. **At-Least-Once:** Consumer processes it fully, *then* ACKs it. If CPU crashes right before the ACK, Kafka will resend it later. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Enabling `enable.auto.commit=true` | Kafka automatically commits the offset every 5 seconds, regardless of whether your Java code actually finished processing the message. Leads to silent data loss if threads crash. | Set to `false`. Use `Acknowledgment.acknowledge()` explicitly at the very end of your `@KafkaListener` method block. |
| Having 1 Partition for a High-Volume Topic | You deploy 10 microservice pods to process the topic, but 9 of them sit completely idle because a single partition can only be read by 1 consumer in a group. | Create topics with at least 3, 6, or 10 partitions so the work can be distributed across your Docker containers. |
| Doing heavy DB lookups in the Consumer thread | The `@KafkaListener` loop blocks. If you take 6 minutes to process an email, Kafka assumes your consumer died (hit `max.poll.interval.ms`) and triggers a massive Rebalance, pausing all other consumers. | Keep consumer processing fast. If doing heavy I/O, pass the processing to an async internal thread pool, and configure Kafka's poll intervals accordingly. |

---

## 7. Real-World Usage

| Pattern | Where it shows up |
|---|---|
| **Website Activity Tracking** | LinkedIn created Kafka for this. Every time you click, hover, or scroll, JS sends an event to a Kafka topic. Stream processing engines (Kafka Streams / Flink) consume this 1M/sec topic to generate real-time analytics. |
| **Saga Pattern Choreography** | In Microservices, `OrderService` places an `{order_id: 1, status: PENDING}` event on Kafka. `PaymentService` listens, charges the card, and places a `{order_id: 1, status: PAID}` event on Kafka. `OrderService` listens to that and updates its DB to `APPROVED`. |
| **Dead Letter Queue (DLQ)** | When a Spring Boot consumer catches an unrecoverable exception (like a JSON parse error), it uses a `DefaultErrorHandler` to automatically redirect that specific message to a `topic-name.DLQ` and ACKs the original, bypassing the poison pill and letting development teams inspect the broken message manually later. |

---

## 8. Practice Tasks

1.  **Spin up Kafka locally:** Run a `docker-compose.yml` file containing Zookeeper (or KRaft) and a Kafka Broker.
2.  **CLI Interaction:** Exec into the docker container. Use `kafka-topics.sh` to create a topic named `test-topic` with 3 partitions. Use `kafka-console-producer.sh` to type messages, and execute `kafka-console-consumer.sh` in another terminal to see them pop up in real time.
3.  **Spring Boot Integration:** Build a producer that sends 10,000 strings in a for-loop. Build a listener that reads them and prints them. Run them and watch the speed.

---

## 9. Quick Revision

### Kafka Architecture
*   **Producer:** Connects to broker, pushes data. 
*   **Broker:** The server holding the data on disk.
*   **Consumer:** Connects to broker, polls for data.
*   **Zookeeper / KRaft:** The consensus controller managing which broker is the "Leader" of which partition.

### Data Model
*   **Topic:** The table.
*   **Partition:** The physical shard of the topic.
*   **Offset:** The line number in the partition.
*   **Consumer Group:** Prevents multiple instances of the *same* app from reading the *same* message twice.
