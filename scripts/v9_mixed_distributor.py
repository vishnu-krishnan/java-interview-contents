import os
import re

mixed_file = "/home/seq_vishnu/Documents/java/categorized/13_mixed_comprehensive_lists.md"
target_dir = "/home/seq_vishnu/Documents/java/categorized"

def get_dominant_category(text):
    text_lower = text.lower()
    scores = {
        '1_core_java.md': text_lower.count('core java') + text_lower.count('hashmap') + text_lower.count('oop') + text_lower.count('exception'),
        '2_multithreading.md': text_lower.count('thread') + text_lower.count('concurrency') + text_lower.count('synchronized') + text_lower.count('executor'),
        '4_java_features.md': text_lower.count('java 8') + text_lower.count('stream') + text_lower.count('lambda'),
        '5_spring_hibernate_springboot.md': text_lower.count('spring') + text_lower.count('hibernate') + text_lower.count('jpa') + text_lower.count('boot'),
        '6_sql_nosql_databases.md': text_lower.count('sql') + text_lower.count('database') + text_lower.count('query') + text_lower.count('join'),
        '7_microservices_kafka.md': text_lower.count('microservice') + text_lower.count('kafka') + text_lower.count('rabbitmq') + text_lower.count('gateway'),
        '10_java_coding_questions.md': text_lower.count('dsa') + text_lower.count('leetcode') + text_lower.count('coding') + text_lower.count('array'),
        '11_java_scenario_based.md': text_lower.count('interview') + text_lower.count('experience') + text_lower.count('round') + text_lower.count('lpa'),
        '12_career_resources.md': text_lower.count('roadmap') + text_lower.count('resume') + text_lower.count('job')
    }
    # 11_java_scenario_based is a good default for full interview experiences
    best_file = max(scores, key=scores.get)
    if scores[best_file] == 0:
        return '11_java_scenario_based.md'
    return best_file

if os.path.exists(mixed_file):
    with open(mixed_file, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\n---\n', content)
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        target = get_dominant_category(block)
        target_path = os.path.join(target_dir, target)
        
        with open(target_path, 'a', encoding='utf-8') as tf:
            tf.write("\n\n" + block + "\n\n---\n\n")

    os.remove(mixed_file)
    print("Successfully distributed mixed context into accurate files.")
