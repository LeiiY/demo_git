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
	x = rand(10, 300)
	y = rand(10, 300)

	xy = (x, y, x+diameter, y+diameter)

	ball.append(canvas.create_oval(xy, fill=colour[c_col]))

canvas.pack()

x = [1] * num_balls
y = [1] * num_balls

while True:
	for i in range(num_balls):
		pos = canvas.coords(ball[i])

		if pos[3] > 400 or pos[1] < 0:
			y[i] = -y[i]

		if pos[0] < 0 or pos[2] > 400:
			x[i] = -x[i]

		

		for j in range(num_balls):
			if i == j: continue

			pos2 = canvas.coords(ball[j])

			if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]:
				y[i] = -y[i]
				x[i] = -x[i]
				y[j] = -y[j]
				x[j] = -x[j]

		canvas.move(ball[i], x[i], y[i])



	sleep(0.00000000000001)
	window.update()

window.mainloop()