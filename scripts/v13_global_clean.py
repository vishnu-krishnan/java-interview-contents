import os
import re

directory = "/home/seq_vishnu/Documents/java/categorized/"

global_junk_patterns = [
    # Massive guides promos
    r'Preparing for interviews\? Start revising these today.*?Stay Hungry, Stay FoolisH!',
    r'Preparing for interviews\? Start revising these today.*?𝟏𝟬𝟬𝟬\+ 𝗽𝗲𝗼𝗽𝗹𝗲 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝘂𝘀𝗶𝗻𝗴 𝗶𝘁\.',
    r'𝗜’𝘃𝗲 𝗽𝗿𝗲𝗽𝗮𝗿𝗲𝗱 𝗶𝗻 𝗗𝗲𝗽𝘁𝗵 𝗝𝗮𝘃𝗮 𝗦𝗽𝗿𝗶𝗻𝗴𝗯𝗼𝗼𝘁 𝗯𝗮𝗰𝗸𝗲𝗻𝗱 𝗚𝘂𝗶𝗱𝗲.*?(?:Stay Hungry, Stay FoolisH!|Use code 𝗝𝗔𝗩𝗔𝟰𝟬)',
    r'𝗞𝗲𝗲𝗽𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗶𝗻 𝗺𝗶𝗻𝗱,.*?Use JAVA\d+ to get \d+% off\.\n\nStay Hungry, Stay FoolisH!',
    
    # LinkedIn footers and image previews
    r'Image preview\n[^\n]*\n',
    r'Show more results\n\nAbout\nAccessibility.*?Compose message\nYou are on the messaging overlay\.\s*Press enter to open the list of conversations\.',
    
    # Comment and Follow bait
    r'Follow [A-Z][A-Za-z ]+\s*\n',
    r'💬 Comment “JAVA” if you want a full list.*?questions\.',
    r'Comment the number\.\n\nI’ll share the detailed PDF individually with interested folks\.',
    r'📌 If you want the answers in PDF, comment “PDF”.*?learning resources\. 👇',
    r'💬 #QuestionForGroup:.*?(?:Let’s discuss in the comments! 👇|👇)',
    
    # Empty tags or unlinked video text
    r'🎥 Video I learned from:\n\n\n\nyoutube\.com',
    r'📌 Full Source Code Available on GitHub! \(Link in video description\)'
]

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        for pattern in global_junk_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL | re.MULTILINE)
            
        # Clean up empty horizontal rules created by deleting posts
        content = re.sub(r'---\s+---', '---', content)
        content = re.sub(r'^\s*---\s*$', '---', content, flags=re.MULTILINE)
        content = re.sub(r'\n{3,}', '\n\n', content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            print(f"Cleaned {filename}")

print("Global cleanup complete.")
