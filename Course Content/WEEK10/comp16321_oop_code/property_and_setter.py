# property_and_setter.py
# Demonstration of Python's @property and @xxxx.setter decorators

class Student:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    student1 = Student("Terry Morley", 21, "1 Small Avenue")
    student1.name = "Jimmy White"
    print(student1.name)

    student1.age = 38
    print(student1.age)
