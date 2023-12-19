import re

text = "I have got a mouse, a dog and a cat. Oh, I forgot another cat."

# Regular expression
regex = r"dog|cat"

# Find all matches in text
matches = re.findall(regex, text)

# Print out the matches
print(matches)
