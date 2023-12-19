# Handling student data - a slightly better way

students = [
            ["Larken Rose", 20, "2023 Jones Plantation"],
            ["Julie Smith", 21, "14 Cliff Lane"],
            ["Brian Ferry", 19, "192 Long Road"]
            ]

def print_student_info(index):
    print(students[index][0])
    print(students[index][1])
    print(students[index][2])

def add_student(name, age, address):
    global students
    students += [[name, age, address]]

if __name__ == '__main__':
    print_student_info(0)

    add_student("Terry Morley", 21, "1 Small Avenue")
    print_student_info(3)

    print(students)
