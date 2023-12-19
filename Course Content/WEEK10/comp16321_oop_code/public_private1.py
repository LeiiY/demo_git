# public_private1.py
# Demonstation of public attributes

class Student:
    def __init__(self, name, age, address):
        self.name = name


if __name__ == '__main__':
    student1 = Student("Terry Morley", 21, "1 Small Avenue")
    print(student1.name)

    student1.name = "John Jones"
    print(student1.name)
