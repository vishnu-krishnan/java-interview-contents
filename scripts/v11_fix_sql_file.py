import os

sql_file = "/home/seq_vishnu/Documents/java/categorized/6_sql_nosql_databases.md"
scenario_file = "/home/seq_vishnu/Documents/java/categorized/11_java_scenario_based.md"

with open(sql_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The blocks are separated by \n---\n
blocks = content.split('\n---\n')

new_sql_blocks = []
block_to_move = None

for block in blocks:
    if "Java Developer Interview Prep Checklist" in block:
        # Before moving, clean out the ad at the bottom
        clean_block = block.split("Preparing for interviews? Start revising these today")[0].strip()
        block_to_move = clean_block
    elif "Introducing Reindeer" in block:
        # Ignore this block entirely (delete it)
        pass
    else:
        new_sql_blocks.append(block.strip())

# Rewrite sql file
with open(sql_file, 'w', encoding='utf-8') as f:
    # Filter empty blocks
    valid_blocks = [b for b in new_sql_blocks if b]
    f.write('\n\n---\n\n'.join(valid_blocks) + '\n\n')

# Append moved block to scenario file
if block_to_move:
    with open(scenario_file, 'a', encoding='utf-8') as f:
        f.write("\n\n---\n\n" + block_to_move + "\n\n")

print("Cleanup and migration successful.")
