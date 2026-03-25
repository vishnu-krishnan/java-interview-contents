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

def process_and_categorize(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    posts = re.split(r'### POST \d+ ###', content)
    unique_posts = []
    unique_tokens = []
    
    print("Deduplicating posts...")
    for post in posts:
        post = post.strip()
        if len(post) < 10:
            continue
        tokens = get_normalized_tokens(post)
        
        is_duplicate = False
        for ut in unique_tokens:
            if jaccard_similarity(tokens, ut) > 0.8: 
                is_duplicate = True
                break
        if not is_duplicate:
            unique_posts.append(post)
            unique_tokens.append(tokens)
            
    files_data = {k: [] for k in CATEGORIES.keys()}
    files_data['13_mixed_comprehensive_lists.txt'] = []
    files_data['0_misc_uncategorized.txt'] = []
    
    for post in unique_posts:
        lower_post = post.lower()
        scores = {cat: 0 for cat in CATEGORIES.keys()}
        
        for cat, words in CATEGORIES.items():
            for word in words:
                if word in lower_post:
                    scores[cat] += lower_post.count(word)
                    
        # Identify mixed tech lists
        # If a post has a score of >= 2 in at least 4 different categories, it is a mixed list.
        cats_with_hits = sum(1 for s in scores.values() if s >= 2)
        
        # Override for Scenario questions
        scenario_boost = 0
        scenario_keywords = ['scenario', 'in production', 'suddenly', 'pretend you', 'on-call']
        for sk in scenario_keywords:
            if sk in lower_post:
                scenario_boost += 10 # Massive boost
                
        scores['11_java_scenario_questions.txt'] += scenario_boost
        
        best_cat = '0_misc_uncategorized.txt'
        max_score = 0
        for cat, score in scores.items():
            if score > max_score:
                max_score = score
                best_cat = cat
                
        if max_score > 0 and cats_with_hits >= 4 and scenario_boost == 0:
            best_cat = '13_mixed_comprehensive_lists.txt'
            
        files_data[best_cat].append(post)
        
    for filename, post_list in files_data.items():
        # clean the old file
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as out_f:
            for idx, pst in enumerate(post_list):
                 out_f.write(f"### ITEM {idx+1} ###\n\n{pst}\n\n{'='*80}\n\n")

if __name__ == "__main__":
    infile = "/home/seq_vishnu/Documents/java/LinkedIn_feeds_cleaned.txt"
    outdir = "/home/seq_vishnu/Documents/java/categorized"
    
    process_and_categorize(infile, outdir)
    print("Optimization and re-categorization script finished successfully.")
