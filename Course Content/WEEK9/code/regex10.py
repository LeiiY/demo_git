import re

text = "I call my dog, doggy."

# Regular expression
regex = r"\bdog\b"

# Find all matches in text
matches = re.findall(regex, text)

# Print out the matches
print(matches)
