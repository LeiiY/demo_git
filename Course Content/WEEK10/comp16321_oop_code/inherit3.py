# inherit3.py
# Overriding methods

class Pet:
    def __init__(self, avg_price):
        self.avg_price = avg_price
	
    def eat(self):
        print( "Munch, munch.")

class Dog(Pet):
    def __init__(self, avg_price):
        Pet.__init__(self, avg_price)

    def eat(self): # Overrides the function in the base class
        print("Gulp, munch, slurp, splash, snort.")


if __name__ == '__main__':
    fido = Dog(4.5)
    fido.eat()

