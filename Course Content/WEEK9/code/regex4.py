import re

words = ["sit", "sat", "seat", "s6t"]

# Regular expression
regex = r"^s.t$"

for word in words:
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
