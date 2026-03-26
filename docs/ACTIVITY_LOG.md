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
