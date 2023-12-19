import re

words = ["colour", "color", "colours"]

# Regular expression
regex = r"^colou?r$"

for word in words:
    # Find if the pattern appears in the text
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
