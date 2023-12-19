# Handling student data - a class

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print(self):
        print(self.name)
        print(self.age)
        print(self.address)


student1 = Student("Kate Bush", 32, "16 Wuthering Heights")
# Print by accessing the attributes
print(student1.name, student1.age, student1.address)
# Print via the class method
student1.print()
print('------------')
# Print by accessing the object through the class
Student.print(student1)
print('------------')

students = [
    Student("Larken Rose", 20, "2023 Jones Plantation"),
    Student("Julie Smith", 21, "14 Cliff Lane"),
    Student("Brian Ferry", 19, "192 Long Road")
    ]


def add_student(name, age, address):
    global students
    students += [Student(name, age, address)]

if __name__ == '__main__':
    students[0].print()

    add_student("Terry Morley", 21, "1 Small Avenue")
    students[3].print()

    #print(students)
