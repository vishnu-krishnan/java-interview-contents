<!-- Part of Java Learning Roadmap — Section 12 -->

# 🔗 12. Hibernate & JPA

---

## 1. Definition

*   **ORM (Object-Relational Mapping):** A technique to map database tables to object-oriented classes, allowing you to query and manipulate data using Java objects instead of raw SQL strings.
*   **JPA (Java Persistence API):** A set of rules and interfaces defining how ORM should work in Java. It is just a specification, not executable code.
*   **Hibernate:** The most popular actual framework (implementation) that executes the JPA specification.

---

## 2. Why It Exists

*   **No more JDBC Boilerplate:** Eliminates `try-catch`, manual `Connection` handling, and mapping `ResultSet` rows to variables field-by-field.
*   **Database Independence (Dialects):** You write JPA logic once. If you switch from PostgreSQL to Oracle, you just change the Hibernate "Dialect" config, and Hibernate translates your Java code into Oracle-specific SQL automatically.
*   **Caching & Optimization:** Hibernate automatically groups SQL statements together (batching) and caches queried objects in RAM to prevent hitting the database multiple times for the same record.

---

## 3. How It Works Internally

### 3.1 The First Level (L1) Cache & The `EntityManager`
The `EntityManager` (or `Session` in raw Hibernate) manages a "Persistence Context" (the L1 Cache).
When you query a `User` with ID=1, Hibernate checks the L1 Cache. If missing, it queries the database, instantiates the `User` object, stores it in the L1 Cache, and hands it to you. If you query ID=1 again *within the same transaction*, Hibernate just gives you the cached object. It does not hit the DB again.

### 3.2 Dirty Checking
Hibernate tracks every property of the objects sitting in the L1 Cache. If you change a setter (`user.setName("Alice")`), Hibernate detects the difference (it's "Dirty"). When the transaction commits, Hibernate automatically generates an `UPDATE` SQL statement for you. You don't need to call `.save()`!

### 3.3 Proxies and Lazy Loading
If a `User` has 10,000 `Posts`, downloading all posts when querying the User is terrible for performance.
Hibernate solves this with **Lazy Loading**. It creates a fake subclass (a **Proxy**) of `Post` using byte-code manipulation (CGLIB/ByteBuddy). When you call `user.getPosts()`, it returns the proxy. The actual SQL `SELECT` to fetch the posts is only fired if you call a method inside the proxy, like `user.getPosts().size()`.

### 3.4 Entity States
1.  **Transient:** `new User()`. Exists in JVM memory, completely unknown to Hibernate. No DB ID.
2.  **Persistent:** Attached to the `EntityManager`. `entityManager.persist(user)`. It has a DB ID. Changes are tracked (Dirty Checking active).
3.  **Detached:** The transaction finished. The object still exists in JVM RAM, but Hibernate is no longer tracking it. Setter changes won't trigger `UPDATE`s unless you reattach it via `.merge()`.
4.  **Removed:** Scheduled for `DELETE` upon commit.

---

## 4. Code Examples

### 4.1 A Complete Entity
```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String email;

    // Optimistic Locking: Prevents two threads from overwriting each other
    @Version 
    private Integer version;

    // Lazy load a huge collection!
    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY)
    private List<Post> posts = new ArrayList<>();
}
```

### 4.2 Spring Data JPA Repository
```java
// Spring fully abstracts away the EntityManager handling
public interface UserRepository extends JpaRepository<User, Long> {
    
    // Auto-generates: SELECT * FROM users WHERE email = ?
    Optional<User> findByEmail(String email);

    // Fixing N+1: JOIN FETCH forces Hibernate to fetch posts in the SAME query
    @Query("SELECT u FROM User u JOIN FETCH u.posts WHERE u.id = :id")
    Optional<User> findByIdWithPosts(@Param("id") Long id);
}
```

### 4.3 Transactional Dirty Checking
```java
@Service
public class UserService {
    
    @Transactional
    public void updateUserEmail(Long id, String newEmail) {
        // 1. SELECT query fires, User placed in L1 Cache
        User user = userRepository.findById(id).orElseThrow(); 
        
        // 2. Object becomes Dirty
        user.setEmail(newEmail);
        
        // 3. Method ends -> Transaction commits -> Hibernate auto-fires UPDATE 
        // No userRepository.save(user) needed!
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| What is the N+1 Query Problem? | You query 10 Users (1 query). Then loop through them calling `user.getPosts()`, triggering 10 separate queries. Total: 1+10 = 11 queries. **Fix:** Use `@Query` with `JOIN FETCH`, or `@EntityGraph`. |
| `save()` vs `saveAndFlush()`? | `save()` queues the action in the cache. It executes the SQL just before commit. `saveAndFlush()` forces Hibernate to execute the SQL instantly, blocking the thread until the DB acknowledges. |
| Difference between L1 and L2 Caching? | **L1 Cache (Session level):** Enabled by default. Dies when the transaction ends. **L2 Cache (Application level):** Disabled by default. Shared across all transactions and threads using providers like Ehcache or Redis. |
| Why does my `@Transactional` rollback not work? | Spring AOP **only** rolls back for `RuntimeException`s (Unchecked). It commits if an `IOException` or `SQLException` (Checked) occurs! Override with: `@Transactional(rollbackFor = Exception.class)`. |
| What is Optimistic Locking (`@Version`)? | Two threads read `Version 1`. Thread A updates DB → `Version 2`. Thread B tries to update where `version=1`, fails, and throws `OptimisticLockException`. Perfect for low-collision safety without expensive DB read-locks. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| FetchType.EAGER on Collections | If `User` EAGER loads `Posts`, querying `findAll()` on Users will execute thousands of queries instantly, crashing the server. | Collections (`@OneToMany`, `@ManyToMany`) EXCLUSIVELY use `FetchType.LAZY`. Use `JOIN FETCH` when eagerness is needed. |
| Self-Invocation Proxy Bypass | Calling a `@Transactional` method from *inside the same class*: `this.updateDb();`. The Spring Proxy is bypassed! No transaction starts! | The method must be called from *outside* the class by an injected bean. Or use `AopContext.currentProxy()`. |
| Using `List` for `@ManyToMany` | Hibernate struggles to optimize `List` removals in many-to-many join tables, sometimes deleting ALL rows and re-inserting the ones that survived. | Use `Set<T>` for `@ManyToMany` relationships. |
| Overusing `@OneToOne` | Using it on purely related functional data forces an unwanted JOIN on every query because Hibernate cannot proxy one-to-one cleanly without knowing if the child is null. | Combine them into the same `@Entity` table if possible using `@Embedded`. |

---

## 7. Real-World Usage

| Concept | Where it shows up |
|---|---|
| **Pessimistic Locking** | Banking Systems. `@Lock(LockModeType.PESSIMISTIC_WRITE)` translates to `SELECT ... FOR UPDATE`. Forces all other threads to physically wait on the database row until you finish withdrawing money. |
| **Spring Data Projections** | Querying a massive `User` entity just to get the `name` wastes RAM. Projections allow JPA to map directly to a small `UserNameDTO` using `SELECT u.name FROM User u`. |
| **Auditing** | Adding `@CreatedDate` and `@LastModifiedDate` to entities. Spring Data JPA auto-fills the timestamps on insert/update. |

---

## 8. Practice Tasks

1.  **N+1 Simulator:** Create a `Department` with many `Employees`. Create 5 departments with 5 employees each. Write a standard `findAll()` API that loops and prints employee names. Look at the console log (hibernate.show_sql=true). Count the queries. Then add `JOIN FETCH` to the repository method and see the query drop to exactly 1.
2.  **Dirty Check Test:** Write a `@Transactional` service method. Fetch a user, change their name. Do NOT call `save()`. Query the database manually and verify the name changed.
3.  **Optimistic Lock Crash:** Add a `@Version int version` to an entity. Write a test that opens two separate threads, reads the exact same entity, modifies it, and both try to save. Catch and print the `OptimisticLockException`.

---

## 9. Quick Revision

### Fetch Type Defaults
*   `@OneToMany` / `@ManyToMany` → **LAZY** by default.
*   `@ManyToOne` / `@OneToOne` → **EAGER** by default. (DANGEROUS).

### Cascade Types
If `Parent` cascades to `Child`:
*   `PERSIST`: Saving Parent automatically saves new Child.
*   `REMOVE`: Deleting Parent automatically deletes children.
*   `MERGE`: Updating detached Parent updates children.
*   `ALL`: Combines all of the above.

### Entity State Transition
`new()` → [Transient] → `persist()` → [Persistent] → `commit()` → [Detached] → `merge()` → [Persistent] → `remove()` → [Removed (Deleted)]
