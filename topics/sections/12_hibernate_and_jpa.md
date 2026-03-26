<!-- Part of Java Learning Roadmap — Section 12 -->

## 🔗 9. Hibernate & JPA

- ORM (Object-Relational Mapping) Concepts
- **JPA (Java Persistence API)**
  - `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`
  - `EntityManager` and Persistence Context
  - JPQL (Java Persistence Query Language)
  - Named Queries and Native Queries (`@Query`)
  - DTO Projection — read-only performance APIs
- **Hibernate as a JPA Implementation**
  - Hibernate Session and Session Factory
  - **Entity States**: Transient → Persistent → Detached → Removed
  - `save()` vs `persist()` vs `merge()` vs `saveAndFlush()`
  - First-Level Cache (Session) and Second-Level Cache (SessionFactory)
  - Lazy vs Eager Loading — performance implications
  - **N+1 Query Problem** — detection and fixes (JOIN FETCH, `@EntityGraph`, `@BatchSize`, DTO Projection, `SUBSELECT`)
  - Dirty Checking — how Hibernate detects changes automatically
- **Entity Relationships**
  - `@OneToOne`, `@OneToMany`, `@ManyToOne`, `@ManyToMany`
  - Cascade Types (`PERSIST`, `MERGE`, `REMOVE`, `ALL`)
  - Fetch Types (`LAZY`, `EAGER`)
  - `@EmbeddedId` — composite keys
- HQL (Hibernate Query Language)
- Hibernate Criteria API
- **`@Transactional` Deep Dive**
  - Internal working (Spring proxy-based AOP)
  - Self-invocation pitfall — `this.method()` bypasses proxy; fix: inject self-reference
  - `rollbackFor = Exception.class` — by default only `RuntimeException` triggers rollback
  - `readOnly = true` — disables dirty checking, can use read replica
  - **Transaction Propagation Types**

    | Propagation | Behaviour |
    |---|---|
    | `REQUIRED` *(default)* | Join existing or create new |
    | `REQUIRES_NEW` | Always create new, suspend existing |
    | `NESTED` | Nested transaction — inner rollback doesn't affect parent |
    | `SUPPORTS` | Join existing if present, else no transaction |
    | `NOT_SUPPORTED` | Suspend existing, run without transaction |
    | `NEVER` | Must run without transaction — throws if one exists |
    | `MANDATORY` | Must run within existing transaction — throws if none |

- **Optimistic vs Pessimistic Locking**
  - **Optimistic** — no DB lock taken; `@Version` field checked on update; `OptimisticLockException` if version mismatch; best for high-read, low-write
  - **Pessimistic** — DB row locked for transaction duration; `@Lock(LockModeType.PESSIMISTIC_WRITE)`; best for financial/inventory writes

---
