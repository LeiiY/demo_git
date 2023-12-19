import re

words = ["a5", "b15", "v3000", "z12345"]

# Regular expression
regex = r"^[A-Za-z]\d{2,4}$"

for word in words:
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
