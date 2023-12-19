# factory_method.py

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def from_separate_names(cls, first_name, family_name, age, address):
        return cls(first_name + " " + family_name, age, address)

if __name__ == '__main__':
    student1 = Student("Larken Rose", 20, "2023 Jones Plantation")
    student2 = Student.from_separate_names("Julie", "Smith", 21, "14 Cliff Lane")

    print(student1.name)
    print(student2.name)
