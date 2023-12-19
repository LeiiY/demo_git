import re

text = "David has got a dog, Ahmed has got a cat, and Frida owns a mouse."

# Regular expression
regex = r"\bcat|dog|mouse\b"

# Replace all matches with 'pet'
new_text = re.sub(regex, 'pet', text)

print(text)
print(new_text)
