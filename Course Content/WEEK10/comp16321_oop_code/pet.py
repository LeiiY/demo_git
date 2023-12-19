# pet.py

class Pet:
    def __init__(self, avg_price, sound):
        self.avg_price = avg_price
        self.sound = sound
	
    def make_sound(self):
        print( "{}! {}!".format(self.sound, self.sound) )

    def eat(self):
        print( "Munch, munch.")


if __name__ == '__main__':
	squeaky = Pet(4.5, "Squeak")
	squeaky.make_sound()
	squeaky.eat()
