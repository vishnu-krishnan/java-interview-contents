# Architecture: Java Interview Prep Data System

## Tech Stack
- **Primary Tooling:** Python (Regular Expressions, CSV/JSON processing)
- **Inputs:** `LinkedIn feeds.txt` (Raw paste)
- **Outputs:** `LinkedIn_feeds_cleaned.txt` (Filtered post bodies)

## System Components
### Component 1: Parser (Python)
Responsibilities:
- Detect post boundaries using profile markers.
- Filter out header/nav sections and profile metadata.

### Component 2: Storage
Responsibilities:
- Flat file format for initial cleaning.
- Structured storage (JSON) for later categorization.
