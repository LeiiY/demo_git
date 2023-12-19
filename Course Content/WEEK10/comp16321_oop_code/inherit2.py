# inherit2.py

class Pet:
    def __init__(self, avg_price):
        self.avg_price = avg_price
	
    def eat(self):
        print( "Munch, munch.")

class Mouse(Pet):
    def __init__(self, avg_price):
        Pet.__init__(self, avg_price) # Call initialiser of the Base Class

    def scurry(self):
        print("I'm scurrying.")


if __name__ == '__main__':
    mouse = Mouse(4.5)
    mouse.scurry()
    mouse.eat()
    print("£{}".format(mouse.avg_price))

