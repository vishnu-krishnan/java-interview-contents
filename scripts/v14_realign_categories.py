import os
import re
from collections import Counter

# Configuration
DIRECTORY = "/home/seq_vishnu/Documents/java/categorized/"
BACKUP_DIR = "/home/seq_vishnu/Documents/java/categorized_backup_20260326/"

# Target files mapping
# Priority order: mixed reports first to capture multi-topic interview experiences
CATEGORIES = {
    "13_mixed_interview_reports.md": ["interview experience", "round 1", "round 2", "round 3", "interviewed at", "hcl", "accenture", "zensar", "atlassian", "interview questions asked @"],
    "1_core_java.md": ["core java", "oop ", "encapsulation", "inheritance", "polymorphism", "abstraction", "exception handling", "serialization", "transient", "volatile", "static", "abstract class", "interface", "generics", "type erasure"],
    "2_multithreading.md": ["thread", "multithreading", "concurrency", "runnable", "callable", "executorservice", "synchronized", "deadlock", "race condition", "reentrantlock", "semaphore", "countdownlatch", "forkjoin"],
    "3_advanced_java.md": ["jvm ", "memory model", "heap", "stack", "metaspace", "garbage collection", " gc ", " jit ", "classloader", "aot cache", "compact object headers"],
    "4_java_features.md": ["java 8", "java 11", "java 17", "java 21", "lambda", "stream", "optional", "record", "sealed", "pattern matching", "functional interface", "unaryoperator", "predicate", "consumer", "supplier", "method reference"],
    "5_spring_hibernate_springboot.md": ["spring", "boot", "hibernate", "jpa", "bean", "ioc", "autowired", "restcontroller", "transactional", "n+1", "entitygraph", "batchsize"],
    "6_sql_nosql_databases.md": ["sql", "mysql", "postgresql", "nosql", "mongodb", "redis", "indexing", "acid", "normalization", "inner join", "outer join"],
    "7_microservices_kafka.md": ["microservice", "kafka", "rabbitmq", "circuit breaker", "resilience4j", "api gateway", "service discovery", "eureka", "distributed", "zipkin", "sleuth"],
    "8_docker_kubernetes.md": ["docker", "kubernetes", " k8s ", "container", "pod", "deployment", "helm"],
    "9_git_testing.md": ["git ", "junit", "mockito", "testing", "unit test", "integration test", "mocking"],
    "10_java_coding_questions.md": ["coding round", "coding question", "coding problem", "write a program", "reverse", "palindrome", "factorial", "fibonacci", "anagram", "substring", "duplicate", "frequency", "program to"],
    "11_java_scenario_based.md": ["scenario", "production issue", "performance drop", "design a system", "how will you handle", "what would you do"],
    "12_career_resources.md": ["resume", "job search", "interview tips", "salary negotiation", "career gap", "cheatsheet"]
}

# JUNK PATTERNS (Aggressive)
JUNK_PATTERNS = [
    r'Preparing for interviews\?.*?Stay Hungry, Stay FoolisH!',
    r'𝟏𝟬𝟬𝟬\+ 𝗽𝗲𝗼𝗽𝗹𝗲 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝘂𝘀𝗶𝗻𝗴 𝗶𝘁\.',
    r'Use code 𝗝𝗔𝗩𝗔𝟰𝟬',
    r'Image preview\n[^\n]*\n',
    r'Show more results\n\nAbout\nAccessibility.*?Compose message\nYou are on the messaging overlay\.',
    r'Follow [A-Z][A-Za-z ]+\s*\n',
    r'💬 Comment .*?\n',
    r'Comment the number\.\n\nI’ll share the detailed PDF.*?\.',
    r'📌 If you want the answers in PDF.*?\n',
    r'🎥 Video I learned from:.*?\n',
    r'📌 Full Source Code Available on GitHub!.*?\n',
    r'Connect: [A-Za-z ]+',
    r'Me: .*?\n',
    r'Result - (?:REJECTED|SELECTED|PENDING)',
    r'Hope this helps.*?\n',
    r'I’ll share the detailed.*?\n',
    r'^[.\s]+$', # Stray dots and whitespace
    r'\d+K followers',
    r'\d+[wm] • \d+[wm] Visible to everyone',
    r'View company: [A-Za-z ]+',
    r'Prominent academy',
    r'Send me (?:connection request|CV|your CV).*?\n\d\..*?\n',
    r'\d\.(?:Send me|I will upload|You will get|If you pass).*?\n',
    r'Doc cc : [A-Za-z ]+',
    r'🚫.*?Rejected by.*?(?:\n|$)',
    r'Check here\.\n\nmedium\.com(?:\n|$)'
]

def clean_block(block):
    for pattern in JUNK_PATTERNS:
        block = re.sub(pattern, '', block, flags=re.DOTALL | re.MULTILINE | re.IGNORECASE)
    
    # Remove leading/trailing markers and whitespace
    block = block.strip()
    
    # Remove trailing dots left by removals
    block = re.sub(r'\n\s*\.\s*\n', '\n', block)
    
    block = re.sub(r'^(\s*##\s*)+', '## ', block) # Normalize header
    if block and not block.startswith('## '):
        block = '## ' + block # Add header if missing
    
    return block

def get_best_category(block):
    block_lower = block.lower()
    
    # Check for mixed reports first - high priority
    if any(x in block_lower for x in ["round 1", "round 2", "interview experience", "interviewed at"]):
        return "13_mixed_interview_reports.md"

    scores = Counter()
    for cat, keywords in CATEGORIES.items():
        if cat == "13_mixed_interview_reports.md":
            continue
        for kw in keywords:
            if kw in block_lower:
                # Weighting: give more weight to specific keywords
                weight = 2 if len(kw) > 5 else 1
                scores[cat] += weight
                
    if not scores:
        return "11_java_scenario_based.md" # Default to scenario
    
    return scores.most_common(1)[0][0]


def main():
    all_blocks = []
    
    # Read all blocks from all MD files
    for filename in os.listdir(DIRECTORY):
        if filename.endswith(".md"):
            filepath = os.path.join(DIRECTORY, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                blocks = content.split('---')
                for b in blocks:
                    cleaned = clean_block(b)
                    if len(cleaned) > 50: # Ignore very short/empty blocks
                        all_blocks.append(cleaned)

    # Dictionary to store new content
    new_contents = {cat: [] for cat in CATEGORIES}
    
    # Re-categorize
    for block in all_blocks:
        cat = get_best_category(block)
        new_contents[cat].append(block)
    
    # Write back
    for cat, blocks in new_contents.items():
        filepath = os.path.join(DIRECTORY, cat)
        if blocks:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n---\n'.join(blocks))
            print(f"Updated {cat} with {len(blocks)} blocks")
        else:
            # Even if empty, create/clear the file
            with open(filepath, 'w', encoding='utf-8') as f:
                 pass
            print(f"Cleared {cat} (no relevant content found)")

if __name__ == "__main__":
    main()
