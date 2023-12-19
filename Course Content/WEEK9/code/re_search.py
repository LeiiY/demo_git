import re

text = "In the US they use the word dialog but in the UK, it is spelt dialogue"

# Regular expression
regex = r"dialog(ue)?"

# Find if the pattern appears in the text
if(re.search(regex, text)):
    print("Pattern found")
else:
    print("Pattern not found")

# Find first match in text and its position
match = re.search(regex, text)
print(match.group(0), match.start(), match.end())
