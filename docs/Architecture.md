# Architecture: Java Interview Preparation Repository

## Project Type
R&D / Study Guide — Java Backend Engineering

---

## 📁 Folder Structure

```
java/
├── ProjectPlan.md                         ← Project scope & phase tracker
├── docs/
│   ├── ACTIVITY_LOG.md                    ← All session change logs
│   ├── Architecture.md                    ← This file
│   ├── Java Interview Guide.docx          ← Source reference document
│   ├── linkedin_feeds_raw.txt             ← Original LinkedIn feed dump
│   └── linkedin_feeds_cleaned.txt         ← Cleaned/deduplicated feed
└── topics/
    ├── Java_Learning_Roadmap.md           ← Master roadmap (28 sections, 1554 lines)
    └── sections/                          ← One file per roadmap section
        ├── 01_core_java.md
        ├── 02_oop_in_java.md
        ├── 03_collections_framework.md
        ├── 04_concurrency_and_multithreading.md
        ├── 05_functional_programming.md
        ├── 06_java_io.md
        ├── 07_java_version_features.md
        ├── 08_advanced_java_topics.md
        ├── 09_design_patterns.md
        ├── 10_jdbc.md
        ├── 11_databases_sql_nosql.md
        ├── 12_hibernate_and_jpa.md
        ├── 13_spring_framework.md
        ├── 14_spring_boot.md
        ├── 15_web_development_and_api_design.md
        ├── 16_testing_in_java.md
        ├── 17_build_tools_and_devops.md
        ├── 18_docker_and_kubernetes.md
        ├── 19_deployment_and_cloud.md
        ├── 20_microservices_architecture.md
        ├── 21_apache_kafka_and_messaging.md
        ├── 22_observability_and_monitoring.md
        ├── 23_system_design_hld.md
        ├── 24_dsa_and_competitive_programming.md
        ├── 25_agile_scrum_project_management.md
        ├── 26_interview_preparation_strategy.md
        ├── 27_coding_programs_and_examples.md
        └── 28_learning_resources.md
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

- **Master roadmap** (`Java_Learning_Roadmap.md`) is the single source of truth — all 28 sections in one navigable file
- **Section files** (`sections/`) are individual deep-dive references — one topic per file for focused study
- **`docs/`** stores reference material, logs, and source documents — never study notes
- Raw LinkedIn feeds preserved in `docs/` as archival source; all useful content is distilled into section files
- No scripts or processing artifacts in the repository — only final polished content
