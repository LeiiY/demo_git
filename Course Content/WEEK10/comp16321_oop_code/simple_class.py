# simple.py
# Simple example of using a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age)


    def age_check(self):
        if self.age >= 18:
            print(self.name, "is over 18.")
        else:
            print(self.name, "is a minor.")

    def print(self):
        print("Name: " + self.name + " Age: " + str(self.age))


fred = Person("Fred Bloggs", 25)
print(type(fred))

print(fred)

print(fred.name)

susan = Person("Susan Smith", 14)

susan.name = "Susan Bloggs"

print(susan.name)
susan.print()
susan.age_check()
susan.age = 19
print("-- Changed Susan's age to 19")
susan.age_check()
