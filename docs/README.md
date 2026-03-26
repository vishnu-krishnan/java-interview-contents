# Architecture: Java Interview Preparation Repository

## Project Type
R&D / Study Guide — Java Backend Engineering

---

## 📁 Folder Structure

```
java/
├── 00_java_learning_roadmap.md            ← Master roadmap (28 sections)
├── 01_core_java.md                        ← Section deep-dives
├── 02_oop_in_java.md
├── ...
├── 28_learning_resources.md
├── README.md                              ← Entry point for the repository
├── ProjectPlan.md                         ← Project scope & phase tracker
└── docs/
    ├── ACTIVITY_LOG.md                    ← All session change logs
    ├── Architecture.md                    ← This file
    ├── Java Interview Guide.docx          ← Source reference document
    ├── linkedin_feeds_raw.txt             ← Original LinkedIn feed dump
    └── linkedin_feeds_cleaned.txt         ← Cleaned/deduplicated feed
```

## Section Ordering Rationale

| Layer | Sections | What |
|---|---|---|
| **Java Foundations** | 1–6 | Core Java, OOP, Collections, Concurrency, Functional, I/O |
| **Language Evolution** | 7 | Java 8 / 11 / 17 / 21 features |
| **Java Internals** | 8–9 | JVM/GC/Memory, Design Patterns |
| **Data Layer** | 10–12 | JDBC, SQL/NoSQL Databases, Hibernate/JPA |
| **Spring Ecosystem** | 13–14 | Spring Framework, Spring Boot |
| **API & Testing** | 15–16 | Web/API Design, Testing (JUnit/Mockito) |
| **Infrastructure** | 17–19 | Build Tools, Docker/K8s, Deployment/Cloud |
| **Distributed Systems** | 20–22 | Microservices, Kafka, Observability |
| **Architecture** | 23 | System Design (HLD) |
| **Interview Prep** | 24–27 | DSA, Agile, Strategy, Coding Programs |
| **Resources** | 28 | Books, courses, tools |

## Design Decisions

- **Master roadmap** (`00_java_learning_roadmap.md`) is the single source of truth — all 28 sections in one navigable file
- **Section files** (`01_*.md` to `28_*.md`) are individual deep-dive references — one topic per file for focused study
- **`docs/`** stores reference material, logs, and source documents — never study notes
- Raw LinkedIn feeds preserved in `docs/` as archival source; all useful content is distilled into section files
- No scripts or processing artifacts in the repository — only final polished content
