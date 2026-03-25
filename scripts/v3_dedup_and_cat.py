import re
import os
import string

def get_normalized_tokens(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)
    tokens = [t for t in text.split() if t.strip()]
    return set(tokens)

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

CATEGORIES = {
    '1_core_java.txt': ['core java', 'hashmap', 'collections', 'jvm', 'memory', 'exception', 'garbage collection', 'oop', 'polymorphism', 'inheritance', 'string', 'object', 'comparable', 'comparator'],
    '2_multithreading.txt': ['multithreading', 'thread', 'concurrent', 'synchroniz', 'volatile', 'executor', 'deadlock', 'runnable', 'callable', 'lock', 'completablefuture'],
    '3_advanced_java.txt': ['advanced java', 'serialization', 'reflection', 'generics', 'design pattern', 'singleton', 'factory', 'strategy', 'builder'],
    '4_java_features.txt': ['java 8', 'java 11', 'java 17', 'stream', 'lambda', 'functional interface', 'optional', 'record', 'virtual thread', 'loom'],
    '5_spring_hibernate_springboot.txt': ['spring', 'boot', 'hibernate', 'mvc', 'autowired', 'bean', 'restcontroller', 'dependency injection', 'actuator', 'ioc', '@component', '@service', '@repository'],
    '6_databases_sql_jpa.txt': ['sql', 'nosql', 'database', 'jpa', 'query', 'index', 'acid', 'transaction', 'join', 'mongo', 'rdbms', 'persist', 'hibernate'],
    '7_microservices_kafka_rabbitmq.txt': ['microservice', 'kafka', 'rabbitmq', 'eureka', 'api gateway', 'circuit breaker', 'msg', 'feign', 'resilience4j', 'distributed'],
    '8_docker_kubernetes.txt': ['docker', 'kubernetes', 'k8s', 'container', 'image', 'pod', 'cluster', 'deployment'],
    '9_git_testing.txt': ['git', 'test', 'junit', 'mockito', 'cucumber', 'tdd', 'bdd', 'ci/cd', 'jenkins', 'pipeline'],
    '10_java_coding_questions.txt': ['reverse', 'palindrome', 'duplicate', 'array', 'link list', 'tree', 'graph', 'coding', 'leetcode', 'sort', 'dsa'],
    '11_java_scenario_questions.txt': ['scenario', 'suddenly', 'in production', 'how would you', 'how will you', 'what happens if', 'real-world', 'architecture'],
    '12_career_resources.txt': ['resume', 'ats', 'job', 'hiring', 'interview tip', 'salary', 'career', 'community', 'referral', 'join our', 'newsletter', 'naukri']
}

# Some keywords overlap (e.g., hibernate in 5 and 6). We'll trust the highest score.

def process_and_categorize(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split by the separator
    posts = re.split(r'### POST \d+ ###', content)
    
    unique_posts = []
    unique_tokens = []
    
    print("Deduplicating posts...")
    duplicates_removed = 0
    for post in posts:
        post = post.strip()
        if len(post) < 10:
            continue
            
        tokens = get_normalized_tokens(post)
        
        # Check against existing to find duplicates
        is_duplicate = False
        for ut in unique_tokens:
            sim = jaccard_similarity(tokens, ut)
            if sim > 0.8: # 80% similarity threshold for considering it a duplicate
                is_duplicate = True
                break
                
        if is_duplicate:
            duplicates_removed += 1
            continue
            
        unique_posts.append(post)
        unique_tokens.append(tokens)
        
    print(f"Removed {duplicates_removed} duplicate posts. {len(unique_posts)} unique posts remain.")
    
    # Categorization
    stats = {cat: 0 for cat in CATEGORIES.keys()}
    stats['0_misc_uncategorized.txt'] = 0
    
    files_data = {k: [] for k in CATEGORIES.keys()}
    files_data['0_misc_uncategorized.txt'] = []
    
    for idx, post in enumerate(unique_posts):
        lower_post = post.lower()
        scores = {cat: 0 for cat in CATEGORIES.keys()}
        
        for cat, words in CATEGORIES.items():
            for word in words:
                if word in lower_post:
                    scores[cat] += lower_post.count(word)
        
        # Determine the best category
        max_score = 0
        best_cat = '0_misc_uncategorized.txt'
        
        # Scenario vs generic Java conflicts
        # If it has a high scenario score, give it a boost
        if scores.get('11_java_scenario_questions.txt', 0) > 0:
             scores['11_java_scenario_questions.txt'] += 3
        
        for cat, score in scores.items():
            if score > max_score:
                max_score = score
                best_cat = cat
        
        files_data[best_cat].append(post)
        stats[best_cat] += 1
        
    # Write to files
    for filename, post_list in files_data.items():
        if post_list:
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as out_f:
                for idx, pst in enumerate(post_list):
                     out_f.write(f"### ITEM {idx+1} ###\n\n{pst}\n\n{'='*80}\n\n")

    return stats, duplicates_removed

if __name__ == "__main__":
    infile = "/home/seq_vishnu/Documents/java/LinkedIn_feeds_cleaned.txt"
    outdir = "/home/seq_vishnu/Documents/java/categorized_v2"
    
    # Clean output dir if exists
    if os.path.exists(outdir):
        import shutil
        shutil.rmtree(outdir)
        
    stats, dedup = process_and_categorize(infile, outdir)
    
    print("\nCategorization Results:")
    for cat, count in stats.items():
        print(f" - {cat}: {count} posts")
