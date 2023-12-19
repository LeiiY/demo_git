import re

text = "My favourite units were COMP16321, COMP27112, COMP37212"

# Regular expression
regex = r"\bCOMP[^1]\d{4}\b"

# Find all matches in text
matches = re.findall(regex, text)

# Print out the matches
print(matches)
