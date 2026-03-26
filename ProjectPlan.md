# Project Plan: LinkedIn Java Interview Prep

**Project Name:** LinkedIn_Java_Interview_Prep
**Project Type:** R&D
**Starting Phase:** Phase 1: Data Cleaning & Extraction

## Initial Scope
- Clean a raw LinkedIn feed copy-paste file (`LinkedIn feeds.txt`).
- Remove personal details, navigation menus, and LinkedIn UI artifacts.
- Preserve all post contents exactly as they appear (including duplicates).
- Prepare the data for further deduplication and categorization in subsequent phases.

## Phases
1. **Phase 1: Data Parsing & Extraction (DONE)**
   - Implement Python scripts for robust parsing of LinkedIn feed patterns.
   - Clean profile metadata and UI clutter.
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
2. **Phase 2: Deduplication & Quality Filtering (ACTIVE)**
   - Extract individual questions/points from posts.
   - Run deduplication algorithms across the extracted items.
3. **Phase 3: Topic Categorization (DONE)**
   - Group deduplicated questions into specific buckets.
   - Performed global cleanup of LinkedIn-specific filler and engagement bait.
   - Re-aligned content across 13 granular category files using keyword-density scripts.
   - Created `13_mixed_interview_reports.md` for company-specific comprehensive lists.
