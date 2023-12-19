# inherit1.py
# This is an example of 'Aggregation' not 'Inheritance'

class Pet:
    def __init__(self, avg_price):
        self.avg_price = avg_price
	
    def eat(self):
        print( "Munch, munch.")

class Mouse:
    def __init__(self, avg_price):
        self.pet = Pet(avg_price)

    def scurry(self):
        print("I'm scurrying.")


if __name__ == '__main__':
    mouse = Mouse(4.5)
    mouse.scurry()
    mouse.pet.eat()
    print("£{}".format(mouse.pet.avg_price))
