<!-- Part of Java Learning Roadmap — Section 16 -->

# 🧪 16. Testing in Java (JUnit, Mockito, Spring Test)

---

## 1. Definition

**Testing** represents the automated verification of your code's correctness. In the modern Java ecosystem, this is dominated by three main tools:
1.  **JUnit 5 (Jupiter):** The foundational framework that runs the tests (`@Test`, Assertions).
2.  **Mockito:** A framework to create fake (Mock) objects of dependencies to isolate the class being tested.
3.  **Spring Test Framework:** Utilities (`@SpringBootTest`, `MockMvc`) to test how your code integrates with the Spring IoC container, Databases, and Web layers.

### The Testing Pyramid
*   **Unit Tests (Bottom):** Test a single class in total isolation. Fast (~5ms), numerous, uses Mockito.
*   **Integration Tests (Middle):** Test how multiple classes/layers work together (e.g., Service + Database). Slower (~500ms), uses Spring Test.
*   **E2E / System Tests (Top):** Spin up the entire running application, a real database, and hit the HTTP endpoints like a real user. Slowest (~5s+), uses Testcontainers.

---

## 2. Why It Exists

*   **Regression Prevention:** When you refactor a method or upgrade a library, running the test suite instantly tells you if you broke existing functionality.
*   **Developer Confidence:** Without tests, developers are terrified to touch legacy code. With tests, you can aggressively refactor knowing the automated suite acts as a safety net.
*   **Living Documentation:** A well-written test explicitly proves *exactly* how a class is supposed to behave in edge cases.

---

## 3. How It Works Internally

### 3.1 JUnit 5 Execution
JUnit uses Java Reflection heavily. When you run `mvn test`, the Maven Surefire plugin scans your compiled test classes for the `@Test` annotation. JUnit instantiates a brand new instance of your Test class for *every single test method* (to ensure absolute isolation and prevent state bleeding between tests), then invokes the method.

### 3.2 Mockito Proxies
When you use `@Mock UserRepository repo;`, Mockito uses ByteBuddy (bytecode manipulation) to generate a fake proxy subclass of `UserRepository` in RAM. By default, every method on that mock returns `null`, `0`, or `false`. You have to "stub" it (teach it what to do) using `when().thenReturn()`.

### 3.3 Spring Test Context Caching
Integration testing is notoriously slow because starting the Spring `ApplicationContext` takes 3-5 seconds. Spring caches the context! If you have 50 test classes that all use `@SpringBootTest`, Spring only spins up the framework *once* and reuses it for all 50 tests, saving massive amounts of time. (Unless you use `@MockBean` which forces a context reload).

---

## 4. Code Examples

### 4.1 Pure Unit Test (JUnit 5 + Mockito)
*Follows the AAA Pattern: Arrange, Act, Assert.*
```java
@ExtendWith(MockitoExtension.class) // Enables Mockito
class UserServiceTest {

    @Mock   // The fake dependency
    private UserRepository userRepository;

    @InjectMocks // The real object we are testing. Mockito injects the mock into it.
    private UserService userService;

    @Test
    void testFindUser_Success() {
        // 1. Arrange (Setup)
        User fakeUser = new User(1L, "Alice");
        when(userRepository.findById(1L)).thenReturn(Optional.of(fakeUser));

        // 2. Act (Execute the method under test)
        String name = userService.getUserName(1L);

        // 3. Assert (Verify the result)
        assertEquals("Alice", name);
        verify(userRepository, times(1)).findById(1L); // Verify the mock was called
    }
}
```

### 4.2 Spring Boot Web Layer Test (Integration)
Testing a REST Controller *without* spinning up Tomcat or the Database.
```java
@WebMvcTest(UserController.class) // Only loads the Web Layer beans
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc; // Simulates HTTP requests safely

    @MockBean // Replaces the real service inside the Spring Context with a mock
    private UserService userService;

    @Test
    void testGetUser() throws Exception {
        when(userService.getUserName(1L)).thenReturn("Alice");

        // Act & Assert in one fluid chain
        mockMvc.perform(get("/api/users/1"))
               .andExpect(status().isOk())
               .andExpect(jsonPath("$.name").value("Alice"));
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `@Mock` and `@InjectMocks`? | `@Mock` creates the fake proxy object. `@InjectMocks` creates a real instance of the class you are testing, and injects the `@Mock`s into it automatically. |
| Difference between a Mock and a Spy? | A **Mock** is a 100% fake object (methods do nothing/return null). A **Spy** is a wrapper around a *real* object. It calls the real methods by default, but you can selectively stub specific methods. |
| What is `@SpringBootTest` vs `@WebMvcTest`? | `@SpringBootTest` loads the ENTIRE application context (Services, DB connections). It's slow and meant for E2E testing. `@WebMvcTest` is a "sliced" test; it only loads the Spring MVC components necessary to test a Controller, making it extremely fast. |
| How do you test a `private` method? | **You don't.** You test the `public` method that *calls* the private method. If the private method is too complex, it violates the Single Responsibility Principle and should be extracted into its own class to be tested publicly. |
| What is Code Coverage and what's a good target? | The percentage of your application's source code lines executed during the automated tests. Teams typically aim for 80%. 100% is often a waste of time and leads to meaningless testing just for metrics. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Overusing `@SpringBootTest` | Integration tests take 5 seconds per class. Having 100 of them results in an 8-minute build time, destroying developer productivity. | 90% of your tests should be pure Unit tests (using `@ExtendWith(MockitoExtension.class)`) which execute in milliseconds. |
| Depending on Test Execution Order | Test A creates a user. Test B tries to delete that user. If JUnit runs Test B before Test A, it fails randomly in the CI/CD pipeline (Flaky Tests). | Every single test MUST clean up after itself and be 100% independent. |
| Meaningless Assertions | Writing a test that exercises the code just to get Code Coverage points, but doesn't actually check the outputs. Example: `assertNotNull(result);` (What if the result is wrong?) | Assert exact values. `assertEquals("Expected", result.getName());` |

---

## 7. Real-World Usage

| Tool | Where it shows up |
|---|---|
| **Testcontainers** | Developers used to test DB repositories against H2 (in-memory DB). But H2 doesn't have PostgreSQL's special JSONB columns. **Testcontainers** spins up a *real* PostgreSQL database inside a temporary Docker container, runs your tests against it, and kills the container. |
| **JaCoCo / SonarQube** | A CI/CD Pipeline step. When you push to GitHub, JaCoCo generates a code coverage report. If coverage falls below 80%, SonarQube fails the build, preventing you from merging un-tested code. |
| **WireMock** | If your microservice calls the Stripe Payment API, you don't want to actually hit Stripe during unit tests. WireMock spins up a fake local HTTP server that returns pre-configured JSON responses mimicking Stripe. |

---

## 8. Practice Tasks

1.  **TDD (Test Driven Development) Practice:** Read about Red-Green-Refactor. Let's build a `Calculator` class. Do not write the class yet! First, write a test `testDivisionByZeroThrowsException()`. The code won't compile (Red). Now, create the class and method to make it compile, but make it return 0. Run test (Red). Finally, write the `if (y==0) throw Exception` code. Run test (Green).
2.  **Spy vs Mock:** Create an `EmailValidator` with two methods: `isValid(String)` and `regexCheck(String)`. `isValid` calls `regexCheck` internally. Create a JUnit file. Try using `@Mock` on it, verify both methods return false/null. Now change it to `@Spy`, and observe how calling `isValid` actually runs your real Java logic.
3.  **DataJpaTest:** In a Spring Boot app, create a `UserRepository`. Write a test class annotated with `@DataJpaTest`. Auto-wire the repository, save a User, use `flush()`, and then retrieve it by its email.

---

## 9. Quick Revision

### The AAA Pattern
*   **Arrange:** Prepare data, instantiate objects, set up mocks (`when()`).
*   **Act:** Call the exact method you are trying to test.
*   **Assert:** Verify outputs (`assertEquals`) and verify side-effects (`verify(mock)`).

### JUnit 5 Annotations
*   `@Test`: The method itself.
*   `@BeforeEach`: Setup dummy data before every single test runs.
*   `@AfterEach`: Clean up database rows or un-mock static methods.
*   `@BeforeAll`: Extremely heavy setup (like starting Docker). Must be static.
*   `@Disabled`: Skips the test temporarily.

### Spring Testing Annotations
*   `@SpringBootTest` (Full E2E Context)
*   `@WebMvcTest` (Sliced: Only Controllers)
*   `@DataJpaTest` (Sliced: Only Repositories & In-Memory DB)
