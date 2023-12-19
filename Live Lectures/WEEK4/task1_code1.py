from deep_translator import GoogleTranslator

message = "Welcome to this lecture Python Programmers!"

translated = GoogleTranslator(source='auto', target="zh-CN").translate(message)

print(translated)