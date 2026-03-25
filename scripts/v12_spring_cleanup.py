import re

filepath = "/home/seq_vishnu/Documents/java/categorized/5_spring_hibernate_springboot.md"

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove specific promo lines and footers
patterns_to_remove = [
    r'Join our developer community 👇\n💬 Comment “JAVA” if you want a full list of 100\+ Java \+ Spring Boot interview questions\.',
    r'Comment the number\.\n\nI’ll share the detailed PDF individually with interested folks\.',
    r'𝗞𝗲𝗲𝗽𝗶𝗻𝗴 𝘁𝗵𝗶𝘀 𝗶𝗻 𝗺𝗶𝗻𝗱,.*?Use JAVA\d+ to get \d+% off\.\n\nStay Hungry, Stay FoolisH!',
    r'📌 If you want the answers in PDF, comment “PDF”.*?learning resources\. 👇',
    r'## Spring Boot - Build Your Project Faster\n\nImage preview\nSpring Boot - Build Your Project Faster\n\n---'
]

for pattern in patterns_to_remove:
    text = re.sub(pattern, '', text, flags=re.DOTALL | re.MULTILINE)

# Clean up any triple dashes with no content between them
text = re.sub(r'---\s+---', '---', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text.strip())

print("Deep cleaned spring boot file promos.")
