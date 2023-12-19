# private_method.py
# Demonstration of using a private method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_details(self, name, age):
        self.name = name
        self.age = age
        self.__update_db()

    def __update_db(self):
    	print('TODO: update the database with', self.name, self.age)


if __name__ == '__main__':
	person = Person('Penny Lane', 67)
	
	print('\nCalling change_details():\n')
	person.change_details('Penny Smith', 67)
	
	print('\nAttempting to access private method outside an object:\n')
	person.__update_db()
