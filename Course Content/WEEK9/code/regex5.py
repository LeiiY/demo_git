import re

words = ["sit", "sat", "seat", "sot"]

# Regular expression
regex = r"^s[aei]t$"

for word in words:
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
