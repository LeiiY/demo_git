# Handling student data - a class

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return self.name + '\n' + str(self.age) + '\n' + self.address


if __name__ == '__main__':
    student1 = Student("Kate Bush", 32,
            "16 Wuthering Heights")

    print(student1)
