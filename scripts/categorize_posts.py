import re
import os

KEYWORDS = {
    'java_coding': ['array', 'string', 'linked list', 'tree', 'graph', 'logic', 'dsa', 'algorithm', 'coding puzzle', 'coding challenge', 'sort', 'search', 'reverse', 'palindrome', 'duplicate'],
    'java_concepts': ['jvm', 'hashmap', 'concurrent', 'thread', 'interface', 'abstract', 'polymorphism', 'inheritance', 'exception', 'garbage collection', 'final', 'static', 'java 8', 'stream', 'lambda', 'serialization', 'reflection', 'generics'],
    'spring_microservices': ['spring', 'boot', 'microservice', 'rest api', 'jwt', 'oauth', 'security', 'bean', 'autowired', 'controller', 'feign', 'eureka', 'gateway', 'resilience4j', 'circuit breaker'],
    'system_design': ['system design', 'scalability', 'load balanc', 'kafka', 'rabbitmq', 'redis', 'cache', 'architecture', 'distributed', 'hld', 'lld', 'consistent hashing', 'sharding', 'stateless'],
    'database_sql_jpa': ['sql', 'query', 'index', 'hibernate', 'jpa', 'nosql', 'mongo', 'acid', 'transaction', 'join', 'view', 'entity', 'persistence'],
    'career_resources': ['resume', 'ats', 'job', 'hiring', 'interview tip', 'salary', 'career', 'community', 'referral', 'community', 'join our', 'newsletter']
}

CAT_FILES = {
    'java_coding': 'java_coding_questions.txt',
    'java_concepts': 'java_concept_questions.txt',
    'spring_microservices': 'spring_boot_microservices.txt',
    'system_design': 'system_design_architecture.txt',
    'database_sql_jpa': 'database_sql_jpa.txt',
    'career_resources': 'career_resources.txt',
    'misc': 'misc_technical.txt'
}

def categorize_posts(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split by the separator we used in the previous step
    posts = re.split(r'### POST \d+ ###', content)
    
    # Track statistics
    stats = {cat: 0 for cat in CAT_FILES.keys()}
    
    for post in posts:
        post = post.strip()
        if not post:
            continue
            
        lower_post = post.lower()
        scores = {cat: 0 for cat in KEYWORDS.keys()}
        
        for cat, words in KEYWORDS.items():
            for word in words:
                if word in lower_post:
                    scores[cat] += lower_post.count(word)
        
        # Determine the best category
        max_score = 0
        best_cat = 'misc'
        
        for cat, score in scores.items():
            if score > max_score:
                max_score = score
                best_cat = cat
        
        # Append to the corresponding file
        file_path = os.path.join(output_dir, CAT_FILES[best_cat])
        with open(file_path, 'a', encoding='utf-8') as out_f:
            out_f.write(f"{post}\n\n" + "="*80 + "\n\n")
        
        stats[best_cat] += 1
        
    return stats

if __name__ == "__main__":
    infile = "/home/seq_vishnu/Documents/java/LinkedIn_feeds_cleaned.txt"
    outdir = "/home/seq_vishnu/Documents/java/categorized"
    
    # Clean output dir if exists
    if os.path.exists(outdir):
        import shutil
        shutil.rmtree(outdir)
        
    print(f"Categorizing posts from {infile}...")
    stats = categorize_posts(infile, outdir)
    
    print("\nCategorization Results:")
    for cat, count in stats.items():
        print(f" - {CAT_FILES[cat]}: {count} posts")
    print("\nProcesses completed successfully!")
