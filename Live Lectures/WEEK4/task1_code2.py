from deep_translator import GoogleTranslator
import json

message = "Welcome to this lecture Python Programmers!"

# file contains unicode characters. 
json_data = open('languages.json', encoding="utf8")
data = json.load(json_data)

for json_object in data:
	code = json_object["code"]

	try:
		translated = GoogleTranslator(source='auto', target=code).translate(message)
		name = json_object["name"].ljust(22, " ") + ": "
		print(name + translated)
	except:
		print(" not supported")
