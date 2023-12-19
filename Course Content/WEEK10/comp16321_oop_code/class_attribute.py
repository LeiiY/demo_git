# class_attribute.py
# Keep track of the number of objects that have been instatiated

class Student:
    number_of_students = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        Student.number_of_students += 1

    def __del__(self):
        ''' Destructor: called when an object is destroyed '''
        Student.number_of_students -= 1


def func1():
    student4 = Student("Peter Gabriel", 60, "1 Solsbury Hill"),
    print('In func1(), Total number of instantiated students:', Student.number_of_students)	


if __name__ == '__main__':
    # Instantiate a number of Student objects
    student1 = Student("Larken Rose", 20, "2023 Jones Plantation")
    student2 = Student("Julie Smith", 21, "14 Cliff Lane")
    student3 = Student("Brian Ferry", 19, "192 Long Road")
    
    print('Total number of instantiated students:', Student.number_of_students)
    print('Total number of instantiated students:', student1.number_of_students)

    func1()
    print('After func1(), Total number of instantiated students:', Student.number_of_students)

