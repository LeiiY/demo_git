import re

words = ["a1", "b5", "v62"]

# Regular expression
regex = r"^[A-Za-z]\d$"

for word in words:
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
