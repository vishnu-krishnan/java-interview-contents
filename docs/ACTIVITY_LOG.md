# Activity Log

[2026-03-25] [Project Bootstrap]
Change Type: Major
Decision Made: Initialized project for cleaning LinkedIn Java interview feed data.
Reason: User request to process raw feed dump into usable interview prep material.
Impact: Maintainability | Data Quality
Rollback Strategy: Keep original LinkedIn feeds.txt file.

[2026-03-25] [Data Extraction]
Change Type: Minor
Decision Made: Implemented Python regex-based extractor to clean LinkedIn feed text.
Reason: Manually cleaning 10k lines is impossible; automated parsing ensures consistency.
Impact: UX | Data Quality
Rollback Strategy: Re-run script from original source file.

[2026-03-25] [Categorization]
Change Type: Minor
Decision Made: Implementing keyword-based classifier to sort posts into category-specific files.
Reason: Organized study material is easier to consume than a single long file.
Impact: Maintainability | UX
Rollback Strategy: Original cleaned file remains as source of truth.

[2026-03-25] [Granular Categorization & Deduplication]
Change Type: Minor
Decision Made: Changing from 7 broad categories to 12 granular categories and starting deduplication.
Reason: User requested more specific topic files (e.g., Multithreading, Jenkins/Git vs Docker, Java 8-17) and requested deduplication to refine the quality.
Impact: Maintainability | Data Quality
Rollback Strategy: Re-run script from original source file.

[2026-03-25] [Category Refinement]
Change Type: Patch
Decision Made: Appended remaining uncategorized misc content into the Java Scenario category and deleted the misc file.
Reason: User request to merge ambiguous or edge cases into a broader conceptual bucket.
Impact: UX
Rollback Strategy: Separate the specific lines back out using Git/backup.

[2026-03-25] [Category Misclassification Fix]
Change Type: Patch
Decision Made: Created '13_mixed_comprehensive_lists.txt' and heavily boosted 'Scenario' keyword scoring natively inside the categorization script.
Reason: Posts that contained massive lists of questions spanning 4+ domains (like Atlassian full-stack interviews) were hijacking specific files like `2_multithreading.txt`.
Impact: Data Quality | UX
Rollback Strategy: Revert to v3 categorization logic.

[2026-03-25] [Line-By-Line Granular Extraction]
Change Type: Major
Decision Made: Re-wrote script to break massive interview posts into individual line-by-line questions safely.
Reason: User requested precise, manual-like separation of individual questions to prevent generic lists from existing. Processed safely via Python to avoid an LLM memory/token crash on 10k lines.
Impact: UX | Data Accuracy
Rollback Strategy: Revert to post-level chunks.

[2026-03-25] [Rollback V5 Extraction]
Change Type: Major
Decision Made: Reverted extraction strategy immediately back to V4 script logic.
Reason: The line-by-line granular extraction was aggressively chopping off context blocks and answers, thereby destroying the details of the items.
Impact: Data Restoration
Rollback Strategy: None, this was the execution of a rollback.

[2026-03-25] [Formatting Conversion]
Change Type: Patch
Decision Made: Converted all category files from .txt to .md and updated custom dividers to native Markdown horizontal rules.
Reason: User requested the final output files be formatted formally as proper MarkDown files for better rendering.
Impact: UX
Rollback Strategy: Rename files back to .txt.

[2026-03-26] [Global Re-alignment and Deep Cleanup]
Change Type: Major
Decision Made: Implemented v14 re-alignment script to perform aggressive junk removal and keyword-based content migration across all categories.
Reason: Files were cluttered with LinkedIn filler (engagement bait, metadata) and topics were misaligned (e.g., Java 8 in Core Java).
Impact: Data Quality | Maintainability | UX
Rollback Strategy: Use backup folder `categorized_backup_20260326`.

[2026-03-26] [Java Learning Roadmap — Comprehensive Expansion]
Change Type: Major
Decision Made: Rewrote `Java_Learning_Roadmap.md` from 19 sections / 359 lines to 25 sections / 600+ lines with full gap analysis integration.
Reason: Gap analysis of 14 categorized source files revealed ~65 high-priority missing topics and 8 entirely missing sections (Microservices, Kafka, Design Patterns, Java 21, System Design HLD, Observability, API Design, Docker/K8s).
Impact: UX | Maintainability | Data Quality
Rollback Strategy: Git checkout previous version of `Java_Learning_Roadmap.md`.

[2026-03-26] [Java Interview Guide DOCX Integration]
Change Type: Minor
Decision Made: Extracted and integrated unique content from `Java Interview Guide.docx` (1.1MB, 3940 paragraphs) into the roadmap. Added: Externalizable, Integer cache pitfall, Wrapper classes, @SpringBootApplication deep dive, Spring Boot startup 9-step sequence, Transaction Propagation table, Optimistic/Pessimistic locking, 10 Production Issues with root causes, REST vs gRPC table, CSRF/mTLS/Vault secrets, and 2 new sections (Section 25: Agile/Scrum; Section 26: Interview Strategy with 3-month plan + annotations reference table).
Reason: User requested all docx unique content be merged into the roadmap to avoid maintaining two separate documents.
Impact: UX | Data Quality | Maintainability
Rollback Strategy: Git checkout previous version of `Java_Learning_Roadmap.md`.

[2026-03-26] [Repository Restructuring & Section Split]
Change Type: Major
Decision Made: Deleted categorized/, categorized_backup_20260326/, and scripts/ folders. Moved LinkedIn feed files into docs/. Split Java_Learning_Roadmap.md into 28 individual section files under topics/sections/ (01_core_java.md → 28_learning_resources.md). Kept master roadmap file intact. Updated Architecture.md to reflect final folder layout.
Reason: User requested clean folder structure with one file per roadmap section for focused study. Old processing scripts and categorized files were no longer needed after content was merged into the roadmap.
Impact: Maintainability | UX
Rollback Strategy: Git checkout to restore deleted folders; remove topics/sections/ directory.
