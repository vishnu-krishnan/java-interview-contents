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
    '1_core_java.txt': ['core java', 'hashmap', 'collections', 'jvm', 'memory', 'exception', 'garbage collection', 'oop', 'polymorphism', 'inheritance', 'string', 'object', 'comparable', 'comparator', 'hashcode', 'equals'],
    '2_multithreading.txt': ['multithread', 'thread', 'concurrent', 'synchroniz', 'volatile', 'executor', 'deadlock', 'runnable', 'callable', 'lock', 'completablefuture', 'race condition'],
    '3_advanced_java.txt': ['advanced java', 'serialization', 'reflection', 'generics', 'design pattern', 'singleton', 'factory', 'strategy', 'builder'],
    '4_java_features.txt': ['java 8', 'java 11', 'java 17', 'stream', 'lambda', 'functional interface', 'optional', 'record', 'virtual thread', 'loom'],
    '5_spring_hibernate_springboot.txt': ['spring', 'boot', 'hibernate', 'mvc', 'autowired', 'bean', 'restcontroller', 'dependency injection', 'actuator', 'ioc', '@component', '@service', '@repository', 'jpa'],
    '6_databases_sql_jpa.txt': ['sql', 'nosql', 'database', 'query', 'index', 'acid', 'transaction', 'join', 'mongo', 'rdbms', 'persist', 'hibernate', 'jpa', 'connection pool'],
    '7_microservices_kafka_rabbitmq.txt': ['microservice', 'kafka', 'rabbitmq', 'eureka', 'api gateway', 'circuit breaker', 'msg', 'feign', 'resilience4j', 'distributed'],
    '8_docker_kubernetes.txt': ['docker', 'kubernetes', 'k8s', 'container', 'image', 'pod', 'cluster', 'deployment'],
    '9_git_testing.txt': ['git', 'test', 'junit', 'mockito', 'cucumber', 'tdd', 'bdd', 'jenkins', 'pipeline', 'ci/cd'],
    '10_java_coding_questions.txt': ['reverse', 'palindrome', 'duplicate', 'array', 'link list', 'tree', 'graph', 'coding', 'leetcode', 'dsa', 'algorithm', 'sort'],
    '11_java_scenario_questions.txt': ['scenario', 'suddenly', 'in production', 'how would you', 'how will you', 'what happens if', 'real-world', 'architecture'],
    '12_career_resources.txt': ['resume', 'ats', 'job', 'hiring', 'interview tip', 'salary', 'career', 'community', 'referral', 'join our', 'newsletter', 'naukri']
}

def remove_hashtags(text):
    # Removes hashtags like #Java, #SpringBoot
    return re.sub(r'#\w+', '', text).strip()

def process_file_granular(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split the document into posts first to maintain some context
    posts = re.split(r'### POST \d+ ###', content)
    
    extracted_items = []
    
    list_item_pattern = re.compile(r'^(\d+[\.\)️⃣/]\s+|[-*•]\s+)')
    
    for post in posts:
        post = remove_hashtags(post)
        if len(post) < 10:
            continue
            
        # Determine Post Context Score (to help classify short items)
        lower_post = post.lower()
        post_context_scores = {cat: 0 for cat in CATEGORIES.keys()}
        for cat, words in CATEGORIES.items():
            for word in words:
                if word in lower_post:
                    post_context_scores[cat] += lower_post.count(word)
                    
        # Find the dominant post category for fallback
        dominant_post_cat = None
        max_c_score = 0
        for cat, score in post_context_scores.items():
            if score > max_c_score:
                max_c_score = score
                dominant_post_cat = cat
        
        # Split post into lines
        lines = post.split('\n')
        current_item = []
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                # Empty line usually breaks a block, save current item
                if current_item:
                    extracted_items.append({
                        'text': '\n'.join(current_item).strip(),
                        'context_cat': dominant_post_cat
                    })
                    current_item = []
                continue
                
            # If line starts a new list item
            if list_item_pattern.match(stripped) or stripped.endswith('?'):
                # Save previous item if exists
                if current_item:
                    extracted_items.append({
                        'text': '\n'.join(current_item).strip(),
                        'context_cat': dominant_post_cat
                    })
                    current_item = []
                current_item.append(stripped)
            else:
                # Append to current item
                current_item.append(stripped)
                
        # Save any remaining item
        if current_item:
            extracted_items.append({
                'text': '\n'.join(current_item).strip(),
                'context_cat': dominant_post_cat
            })
            
    # Deduplication across all extracted items
    print(f"Extracted {len(extracted_items)} raw items.")
    unique_items = []
    unique_tokens_list = []
    duplicates_removed = 0
    
    for item in extracted_items:
        text = item['text']
        if len(text) < 15: # Skip very short useless items like "Answers:"
            continue
            
        tokens = get_normalized_tokens(text)
        if len(tokens) < 3: # Too short to be meaningful
            continue
            
        is_duplicate = False
        for ut in unique_tokens_list:
            if jaccard_similarity(tokens, ut) > 0.8:
                is_duplicate = True
                break
                
        if not is_duplicate:
            unique_items.append(item)
            unique_tokens_list.append(tokens)
        else:
            duplicates_removed += 1
            
    print(f"Removed {duplicates_removed} duplicate items. {len(unique_items)} unique items remain.")
    
    # Categorization per item
    files_data = {k: [] for k in CATEGORIES.keys()}
    files_data['0_misc_uncategorized.txt'] = []
    
    for item in unique_items:
        text = item['text']
        lower_text = text.lower()
        scores = {cat: 0 for cat in CATEGORIES.keys()}
        
        for cat, words in CATEGORIES.items():
            for word in words:
                if word in lower_text:
                    scores[cat] += lower_text.count(word) * 2 # Give direct match more weight
                    
        # Apply context fallback if item has no strong keywords
        if sum(scores.values()) == 0 and item['context_cat']:
            scores[item['context_cat']] += 1
            
        # Scenario override
        scenario_keywords = ['scenario', 'in production', 'suddenly', 'pretend you', 'on-call', 'what happens if']
        for sk in scenario_keywords:
            if sk in lower_text:
                scores['11_java_scenario_questions.txt'] += 10
                
        best_cat = '0_misc_uncategorized.txt'
        max_score = 0
        for cat, score in scores.items():
            if score > max_score:
                max_score = score
                best_cat = cat
                
        files_data[best_cat].append(text)
        
    # Write to files
    for filename, item_list in files_data.items():
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as out_f:
            for idx, txt in enumerate(item_list):
                 out_f.write(f"### Q{idx+1} ###\n{txt}\n\n{'='*60}\n\n")
                 
if __name__ == "__main__":
    infile = "/home/seq_vishnu/Documents/java/LinkedIn_feeds_cleaned.txt"
    outdir = "/home/seq_vishnu/Documents/java/categorized"
    
    process_file_granular(infile, outdir)
    print("Fine-grained line-by-line categorization completed.")
