from tkinter import Tk, Canvas
from time import sleep
from random import randint as rand
window = Tk()
window.title("The window")
canvas = Canvas(window,width=400,height=400, bg="black")

num_balls = int(input("How many balls?"))
diameter = int(input("Diameter: "))

ball = []
colour = ["red", "yellow", "green", "blue"]

for i in range(num_balls):
	c_col = rand(0,3)
	x = rand(0, 400)
	y = rand(0, 400)

	xy = (x, y, x+diameter, y+diameter)

	ball.append(canvas.create_oval(xy, fill=colour[c_col]))

canvas.pack()



window.mainloop()