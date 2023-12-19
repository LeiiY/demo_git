import time, os

time.sleep(2)
print(os.getlogin())

myList = list(range(1, 101, 2))
print(myList)

[1, 3, 5, 7, 9]

i = 0
while i < 4:
	print("While: " + str(i))
	i += 1

for x in range(4):
	print("For: " + str(x))

for x in range(1, 11, 2):
	print("For sequence: " + str(x))

fruits = ["apple", "banana", "pear"]

for x in fruits:
	print(x)

for x in "banana":
	print(x)

adj = ["warm", "fancy", "big"]
clothes = ["hat", "gloves", "shoes"]

for x in adj:
	for y in clothes:
		print(x, y)
