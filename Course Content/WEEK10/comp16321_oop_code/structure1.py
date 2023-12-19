# Handling student data - a poor way

student_names = ["Larken Rose", "Julie Smith",
                "Brian Ferry"]
student_ages = [20, 21, 19]
student_addresses = ["2023 Jones Plantation",
                "14 Cliff Lane",
                "192 Long Road"]

def print_student_info(index):
    print(student_names[index])
    print(student_ages[index])
    print(student_addresses[index])

def add_student(name, age, address):
    global student_names, student_ages, student_addresses
    student_names += [name]
    student_ages += [age]
    student_addresses += [address]

if __name__ == '__main__':
    print_student_info(0)

    add_student("Terry Morley", 21, "1 Small Avenue")
    print_student_info(3)
