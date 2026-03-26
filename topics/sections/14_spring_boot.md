<!-- Part of Java Learning Roadmap — Section 14 -->

## 🚀 11. Spring Boot

- Spring Boot vs Spring Framework
- **`@SpringBootApplication` Deep Dive** — combines 3 annotations:
  - `@Configuration` — marks class as Spring config, enables `@Bean` methods
  - `@EnableAutoConfiguration` — auto-configures beans based on classpath (e.g., adds Tomcat if `spring-web` present)
  - `@ComponentScan` — scans package + sub-packages for all stereotype annotations
  - ⚠️ If `@Controller`/`@Service` outside base package: add `@ComponentScan(basePackages = {"..."})`
- **Spring Boot Startup Sequence** (9 steps)
  1. `SpringApplication.run()` called
  2. Creates `ApplicationContext` (IoC container)
  3. `@ComponentScan` discovers all beans
  4. `@EnableAutoConfiguration` reads `META-INF/spring/factories`
  5. All `@Bean`, `@Service`, `@Repository`, `@Controller` instantiated
  6. `@Autowired` dependencies injected
  7. `@PostConstruct` methods called
  8. Embedded Tomcat (or Jetty/Undertow) starts on port 8080
  9. Application ready to serve requests
- Auto-Configuration — how it works (`@EnableAutoConfiguration`, `spring.factories`)
- Starters — `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, etc.
- `application.properties` / `application.yml` — externalized config
- Spring Boot Profiles (`@Profile`, `spring.profiles.active`)
- **Request Flow Internals**
  - Client → DispatcherServlet → HandlerMapping → HandlerAdapter → Controller → Service → Repository → DB → Response (Jackson serialization)
- **Building REST APIs**
  - `@RestController`, `@RequestMapping`
  - DTO pattern — Controller → DTO → Service → Mapper → Entity → Repository
  - Request Validation: `@Valid`, `@NotNull`, `@NotBlank`, `@Size`, `@Email`, `@Min`, `@Pattern`
  - Custom constraint validators (`@UniqueEmail`)
  - Exception Handling: `@ControllerAdvice`, `@ExceptionHandler`, structured error responses
  - `@ResponseStatus`, `ResponseEntity<T>`
  - HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE` — correct usage
  - Idempotency — `PUT`, `DELETE`, `GET` are idempotent
- **Caching**
  - `@Cacheable` — cache the result on first call
  - `@CacheEvict` — remove stale data
  - `@CachePut` — always update cache
  - Redis as distributed cache (`spring-boot-starter-data-redis`)
- **Scheduling**
  - `@Scheduled` — `fixedRate`, `fixedDelay`, `cron`
  - `@EnableScheduling`
- **Async Processing**
  - `@Async`, `@EnableAsync`
  - `CompletableFuture` in async service methods
- **Configuration**
  - `@ConditionalOnProperty`, `@ConditionalOnClass`
  - `@Value` and `@ConfigurationProperties`
- **Data Layer**
  - Spring Data JPA integration
  - Database Migrations: **Flyway** / **Liquibase**
  - HikariCP connection pool tuning — `maximum-pool-size`, `connection-timeout`, `idle-timeout`
- **Actuator & Monitoring**
  - Health checks (`/actuator/health`), metrics, info endpoints
  - Micrometer integration
  - Integration with Prometheus / Grafana
- **Security**
  - JWT + Spring Security full configuration
  - OAuth2 Resource Server
  - `NoSuchBeanDefinitionException` vs `NoUniqueBeanDefinitionException` — fixes
  - **CSRF** — Cross-Site Request Forgery; prevention: CSRF token, `SameSite` cookies, CORS headers
  - **Secrets Management** — never hardcode secrets; use HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Kubernetes Secrets
  - **mTLS** — Mutual TLS for service-to-service authentication in microservices
- **Testing**
  - `@SpringBootTest`, `@WebMvcTest`, `@DataJpaTest`
  - `@MockBean`, `@SpyBean`
  - `MockMvc` — controller testing
  - `Testcontainers` — real DB in tests
- **Packaging**
  - Embedded Tomcat — fat JAR
  - Building JAR / WAR
  - `spring.threads.virtual.enabled=true` — Virtual Thread support
  - Dockerizing a Spring Boot App
- **Production Issues & Real Fixes**
  1. **`OutOfMemoryError: Java heap space`** — Memory leak (unbounded static Map, `ThreadLocal` not cleared, cache without eviction). Fix: `jmap` heap dump → VisualVM/MAT analysis; use `WeakHashMap`, Caffeine cache with limits; always `ThreadLocal.remove()` in `finally`
  2. **`NullPointerException` in prod, not in dev** — Race condition, lazy bean not init'd, external API returns null. Fix: `Optional.ofNullable()`, `@NonNull` annotations
  3. **HikariPool connection timeout** — `@Transactional` holding connection too long, N+1 flooding DB, unclosed `ResultSet`. Fix: tune `maximum-pool-size`, reduce transaction scope, add pagination
  4. **`StackOverflowError` in JPA entity** — Bidirectional `@ManyToMany` with circular `toString()`/Jackson serialization. Fix: `@JsonManagedReference`/`@JsonBackReference` or `@JsonIgnore`
  5. **Slow API (latency spikes)** — N+1 queries, missing index, GC Full pause. Fix: `@EntityGraph`/`JOIN FETCH`, add index, switch to G1GC, use `@Async` for fire-and-forget
  6. **`ConcurrentModificationException`** — Modifying non-thread-safe collection during iteration. Fix: `CopyOnWriteArrayList`, `ConcurrentHashMap`, or `Iterator.remove()`
  7. **REST endpoints return 404** — Controller outside component scan path, wrong context path, wrong HTTP method. Fix: move to base package, check `server.servlet.context-path`
  8. **`@Transactional` not rolling back** — Self-invocation (`this.method()`) bypasses proxy, or checked exception used without `rollbackFor`. Fix: inject self; use `rollbackFor = Exception.class`
  9. **Kafka consumer lag keeps growing** — Consumer too slow, insufficient partitions, frequent rebalancing. Fix: increase `concurrency`, batch-process, add partitions
  10. **HTTP 500 prod but 200 dev** — Missing env variable, wrong DB URL, missing secret. Fix: validate with `@PostConstruct`, use Spring Cloud Config centralised config

---
