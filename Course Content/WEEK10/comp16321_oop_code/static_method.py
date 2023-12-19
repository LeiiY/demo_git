# static_method.py

class Student:
    def __init__(self, name, age, address):
        pass
		
    @staticmethod
    def is_cs_student(id):
        return id.startswith('CS')

if __name__ == '__main__':
    print(Student.is_cs_student('MA25542'))
    print(Student.is_cs_student('CS77421'))
