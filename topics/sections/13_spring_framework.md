<!-- Part of Java Learning Roadmap — Section 13 -->

## 🌿 10. Spring Framework

- **Spring Core**
  - Inversion of Control (IoC)
  - Dependency Injection — Constructor (recommended), Setter, Field
  - `@Autowired`, `@Qualifier`, `@Primary`, `@Lazy`
  - `@Component`, `@Service`, `@Repository`, `@Controller`
  - `@Configuration`, `@Bean`
  - Spring Bean Lifecycle — `@PostConstruct`, `@PreDestroy`, `InitializingBean`, `DisposableBean`
  - Bean Scopes — Singleton, Prototype, Request, Session, Application
  - `ApplicationContext` vs `BeanFactory`
  - `CommandLineRunner` / `ApplicationRunner`
  - `@Value` vs `@ConfigurationProperties`
  - `SpringFactoriesLoader` — auto-configuration mechanism
- **Spring AOP** (Aspect-Oriented Programming)
  - Advice types: `@Before`, `@After`, `@AfterReturning`, `@AfterThrowing`, `@Around`
  - Pointcuts and Joinpoints
  - Cross-cutting concerns: logging, security, transactions
- **Spring MVC**
  - `DispatcherServlet` and full Request Lifecycle
  - `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, `@PatchMapping`
  - `@RequestBody`, `@ResponseBody`, `@PathVariable`, `@RequestParam`
  - `@ResponseStatus`, HTTP status codes
  - View Resolvers (Thymeleaf, JSP)
  - `@RestController` vs `@Controller`
- **Spring Security**
  - Authentication vs Authorization
  - JWT-based stateless auth flow
  - OAuth2 — Authorization Code flow, Client Credentials
  - Method-Level Security (`@PreAuthorize`, `@PostAuthorize`)
  - RBAC (Role-Based Access Control)
- **Spring Data JPA**
  - `JpaRepository`, `CrudRepository`, `PagingAndSortingRepository`
  - Derived query methods
  - `@Query` (JPQL and native SQL)
  - Pagination (`Pageable`, `Page<T>`) and Sorting (`Sort`)
- **Spring WebFlux** (Reactive)
  - `Mono<T>`, `Flux<T>`
  - `WebClient` vs `RestTemplate`
  - Reactive vs traditional — when to choose

---
