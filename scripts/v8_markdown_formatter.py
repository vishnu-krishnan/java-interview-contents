import os
import re

def format_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by the separator we created
    items = re.split(r'\n---\n', content)
    formatted_items = []

    for item in items:
        item = item.strip()
        if not item:
            continue
            
        # Remove the '### ITEM X ###'
        item = re.sub(r'### ITEM \d+ ###\s*', '', item)
        
        lines = item.split('\n')
        if not lines:
            continue
            
        # The first non-empty line becomes the title H2
        title_idx = 0
        while title_idx < len(lines) and not lines[title_idx].strip():
            title_idx += 1
            
        if title_idx < len(lines):
            lines[title_idx] = f"## {lines[title_idx].strip()}"
            
        # Clean up bullet points
        for i in range(title_idx + 1, len(lines)):
            line = lines[i]
            # Match pseudo bullets
            line = re.sub(r'^(\s*)[•\-\*]\s+', r'\1- ', line) # Standardize bullet
            line = re.sub(r'^(\s*)👉\s*', r'\1- ', line) # Arrow to bullet
            line = re.sub(r'^(\s*)\d+[️⃣\)]\s+', r'\1- ', line) # Number emoji to bullet
            # Fix pseudo headers
            line = re.sub(r'^━━━━━━━━━━━━━━━━━━━━━━$', '***', line)
            line = re.sub(r'^🔴 (OLD WAY.*?)$', r'### \1', line)
            line = re.sub(r'^🟢 (NEW WAY.*?)$', r'### \1', line)
            lines[i] = line
            
        formatted_items.append('\n'.join(lines))
        
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n\n---\n\n'.join(formatted_items))

if __name__ == "__main__":
    outdir = "/home/seq_vishnu/Documents/java/categorized"
    
    for filename in os.listdir(outdir):
        if filename.endswith(".md"):
            format_markdown(os.path.join(outdir, filename))
            
    print("Markdown semantic formatter completed.")
