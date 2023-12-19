# Handling student data - a class

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

students = [
    Student("Larken Rose", 20, "2023 Jones Plantation"),
    Student("Julie Smith", 21, "14 Cliff Lane"),
    Student("Brian Ferry", 19, "192 Long Road")
    ]

def print_student_info(index):
    print(students[index].name)
    print(students[index].age)
    print(students[index].address)

def add_student(name, age, address):
    global students
    students += [Student(name, age, address)]

if __name__ == '__main__':
    print_student_info(0)

    add_student("Terry Morley", 21, "1 Small Avenue")
    print_student_info(3)

    #print(students)
