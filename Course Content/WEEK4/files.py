settings = open("settings.txt")

print(settings.read(5))
print(settings.readline())
print(settings.readline())

for x in settings:
	print(x)

settings.close()	

settings = open("settings.txt", "a")
settings.write("\nAdding more settings")
settings.close()

settings = open("settings.txt", "r")
print(settings.read())

settings = open("settings.txt", "w")
settings.write("Adding more settings")
settings.close()

newFile = open("myFile.txt", "x")

import os
os.remove("myFile.txt")