# class_method.py

class Student:
    __number_of_students = 0

    def __init__(self, name, age, address):
        Student.__number_of_students += 1

    @classmethod
    def get_number_of_students(cls):
        return Student.__number_of_students

if __name__ == '__main__':
    student1 = Student("Larken Rose", 20, "2023 Jones Plantation")
    student2 = Student("Julie Smith", 21, "14 Cliff Lane")
    student3 = Student("Brian Ferry", 19, "192 Long Road")
    print('Total number of students:', Student.get_number_of_students())
