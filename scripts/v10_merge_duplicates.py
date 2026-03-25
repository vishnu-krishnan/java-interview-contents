import os

base_dir = "/home/seq_vishnu/Documents/java/categorized/"

pairs_to_merge = [
    # (Source -> Dest)
    ("11_java_scenario_questions.md", "11_java_scenario_based.md"),
    ("6_databases_sql_jpa.md", "6_sql_nosql_databases.md"),
    ("7_microservices_kafka_rabbitmq.md", "7_microservices_kafka.md"),
    ("0_misc_uncategorized.md", "11_java_scenario_based.md")
]

for src_name, dest_name in pairs_to_merge:
    src_path = os.path.join(base_dir, src_name)
    dest_path = os.path.join(base_dir, dest_name)
    
    if os.path.exists(src_path):
        with open(src_path, 'r', encoding='utf-8') as sf:
            content = sf.read().strip()
            
        if content:
            # Append cleanly with space
            mode = 'a' if os.path.exists(dest_path) else 'w'
            with open(dest_path, mode, encoding='utf-8') as df:
                df.write("\n\n---\n\n" + content + "\n\n")
                
        # Remove source file
        os.remove(src_path)
        print(f"Merged {src_name} into {dest_name}")
