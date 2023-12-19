from tkinter import Tk, Canvas
from random import randint as rand

def mouse_move(event):
	x = event.x
	y = event.y

	canvas.coords(circle, x-50, y-50, x+50, y+50)

	txt = str(canvas.coords(circle))

	canvas.itemconfig(coords_text, text=txt)

	bounds = canvas.bbox(coords_text)

	xOffset = (800/2) - ((bounds[2] - bounds[0]) /2)

	canvas.coords(coords_text, xOffset, 350)


window = Tk()
canvas = Canvas(window, width=800, height=800)
canvas.pack()
canvas.config(bg="black")

canvas.bind('<B1-Motion>', mouse_move)
xy = (0,0,100,100)

circle = canvas.create_oval(xy, fill="green")
canvas.itemconfig(circle, activefill = "red")

coords_text = canvas.create_text(0, 0, text="", fill="white", font=("Arial Bold", 25), anchor="nw")

coords_label = canvas.create_text(400, 400, text="Left      Top      Right     Bottom", fill="white", font=("Arial", 15))


window.mainloop()