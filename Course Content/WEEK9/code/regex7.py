import re

words = ["a5", "b15", "v300"]

# Regular expression
regex = r"^[A-Za-z]\d{3}$"

for word in words:
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
