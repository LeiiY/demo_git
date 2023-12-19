import re

text = "COMP16321, COMP56321, COMP27112, COMP37212, COMP3721, COM27112"

# Regular expression
regex = r"\bCOMP[1-3]\d{3}[0-2]\b"

# Find all matches in text
matches = re.findall(regex, text)

# Print out the matches
print(matches)
