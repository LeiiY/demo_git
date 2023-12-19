# public_private2.py
# Demonstation of private attributes
# and getter and setter

class Student:
    def __init__(self, name, age, address):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


if __name__ == '__main__':
    student1 = Student("Terry Morley", 21, "1 Small Avenue")
    student1.set_name("Jimmy White")
    print(student1.get_name())
