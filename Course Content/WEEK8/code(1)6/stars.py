from tkinter import Tk, Canvas
from random import randint as rand

window = Tk()
canvas = Canvas(window, width=800, height=400)
canvas.pack()
canvas.config(bg="black")

star = []
c = ["white", "#fefefe", "#dfdfdf"]



for i in range(400):
	x = rand(1,799)
	y = rand(1,200)

	size = rand(2,5)
	f = rand(0,2)

	xy = (x, y, x+size, y+size)
	tmp_star = canvas.create_oval(xy)

	canvas.itemconfig(tmp_star, fill=c[f])

	star.append(tmp_star)


window.mainloop()