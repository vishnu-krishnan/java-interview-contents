import re
import os

def clean_linkedin_feed(input_file, output_file):
    print(f"Opening {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    all_posts = []
    current_post = []
    
    start_found = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Profile header pattern detection
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # If line is 'Name' (or NameStatus) and next_line is 'NameView Name’s profile'
            if line and next_line.startswith(line.split('Status')[0]) and "View " in next_line and ("profile" in next_line or "’s" in next_line):
                # Found new post start. Save current buffer.
                if current_post:
                    post_text = "".join(current_post).strip()
                    if post_text:
                        all_posts.append(post_text)
                
                current_post = []
                start_found = True
                
                # We need to find the END of the metadata block.
                # Usually it ends with a visibility line like "4h • 4h Visible to everyone"
                # or "1d • 1d Visible to group only"
                j = i
                visibility_line_idx = -1
                for k in range(j, min(j + 15, len(lines))):
                    if "Visible to" in lines[k]:
                        visibility_line_idx = k
                        break
                
                if visibility_line_idx != -1:
                    # Start scanning for content after the visibility line
                    m = visibility_line_idx + 1
                    while m < len(lines):
                        m_line = lines[m].strip()
                        if not m_line:
                            m += 1
                            continue
                        if m_line in ["Image preview", "Status is reachable"]:
                            m += 1
                            continue
                        # Found first real content line
                        i = m - 1 # Will be incremented to m in loop
                        break
                else:
                    # Fallback if no visibility line found (shouldn't happen for posts)
                    i = j + 5
                
                i += 1
                continue
        
        if start_found:
            line_val = lines[i].rstrip()
            # Remove "...see more"
            line_val = re.sub(r'(?:…|\.\.\.)see more$', '', line_val)
            current_post.append(line_val + "\n")
            
        i += 1

    # Add remaining post
    if current_post:
        post_text = "".join(current_post).strip()
        if post_text:
            all_posts.append(post_text)

    # Write cleaned results
    print(f"Writing {len(all_posts)} posts to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, post in enumerate(all_posts):
            f.write(f"### POST {idx+1} ###\n\n{post}\n\n")

if __name__ == "__main__":
    infile = "/home/seq_vishnu/Documents/java/LinkedIn feeds.txt"
    outfile = "/home/seq_vishnu/Documents/java/LinkedIn_feeds_cleaned.txt"
    if os.path.exists(infile):
        clean_linkedin_feed(infile, outfile)
        print("Success!")
    else:
        print(f"Error: {infile} not found.")
