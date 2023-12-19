import re

text = "The UK write 'colour' and the US write 'color'"

# Regular expression
regex = r"colou?r"

# Find all matches in text
matches = re.findall(regex, text)

# Print out each match
for match in matches:
    print(match)
