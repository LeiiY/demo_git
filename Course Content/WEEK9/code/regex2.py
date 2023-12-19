import re

words = ["tk", "tok", "took"]

# Regular expression
regex = r"^to+k$"

for word in words:
    # Find if the pattern appears in the text
    if(re.search(regex, word)):
        print(word, "-- match")
    else:
        print(word, "-- no match")
