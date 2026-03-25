import os
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    cleaned_lines = []
    
    junk_patterns = [
        re.compile(r'^\s*#\w+'), # Lines starting with hashtag
        re.compile(r'https://lnkd\.in'), # Links
        re.compile(r'(?i)link in comment'),
        re.compile(r'(?i)follow\s+.*?for more'),
        re.compile(r'(?i)subscribe to'),
        re.compile(r'(?i)save this post'),
        re.compile(r'(?i)comment below'),
        re.compile(r'(?i)drop it in the comments'),
        re.compile(r'(?i)feel free to comment'),
        re.compile(r'(?i)hashtags for global reach'),
        re.compile(r'(?i)follow this series'),
        re.compile(r'(?i)share with your team')
    ]
    
    for line in lines:
        is_junk = False
        
        # Check if line is purely hashtags
        words = line.split()
        if len(words) > 0 and all(w.startswith('#') for w in words):
            is_junk = True
            
        for pattern in junk_patterns:
            if pattern.search(line):
                is_junk = True
                break
                
        if not is_junk:
            cleaned_lines.append(line)
            
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

if __name__ == "__main__":
    outdir = "/home/seq_vishnu/Documents/java/categorized"
    
    for filename in os.listdir(outdir):
        if filename.endswith(".txt"):
            clean_file(os.path.join(outdir, filename))
            
    print("Manual junk cleaning simulation completed safely across all files.")
