import re

text = "The quick brown fox jumped over the lazy dog"

# Regular expression
regex = r" "

replace = "_"

# Replace all matches in text
result = re.sub(regex, replace, text)
print(result)
