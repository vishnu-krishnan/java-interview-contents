<!-- Part of Java Learning Roadmap — Section 16 -->

## 🧪 22. Testing in Java

- **Unit Testing**
  - JUnit 5 — `@Test`, `@BeforeEach`, `@AfterEach`, `@Nested`, `@ParameterizedTest`
  - Mockito — `@Mock`, `@InjectMocks`, `when().thenReturn()`, `verify()`
  - `@ExtendWith(MockitoExtension.class)`
- **Integration Testing**
  - `@SpringBootTest` — full application context
  - `@WebMvcTest` — controller layer only
  - `@DataJpaTest` — repository layer with in-memory DB
  - `MockMvc` — HTTP request simulation
- **Test Doubles** — `@MockBean`, `@SpyBean`
- **Testcontainers** — spin up real Docker containers (Postgres, Redis, Kafka) in tests
- **TDD** (Test-Driven Development) — Red → Green → Refactor cycle
- **Test Best Practices**
  - Field injection → constructor injection for testability
  - Avoid `Optional.get()` without checking
  - No magic numbers — named constants
  - Single responsibility per method

---
