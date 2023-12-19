import re

text = "The UK write 'colour' and the US write 'color'"

# Regular expression
regex = r"colou?r"

# Find all matches in text
matches = re.finditer(regex, text)

for match in matches:
    print(match, "-----", match.group(), "start:", match.start(), "end:", match.end())
