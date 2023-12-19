

myList = [['a', 'b'], [2, 4], 3]
print(myList[1][1])  # 4

myDictionary = {
	"name": "Gareth", 
	"age": 123, 
	"weight": 234
}

print(myDictionary.get("weight"))  # 234

myDictionary["weight"] = 456


print(myDictionary)   # 456
print(myDictionary.get("weight"))

choice = input("What would you like to update? ")

if choice == "name":
	new_name = input("What would you like to be called? ") # leiiy
	myDictionary["name"] = new_name

print(myDictionary)	

















