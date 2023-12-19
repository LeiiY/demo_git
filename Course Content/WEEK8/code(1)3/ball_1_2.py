from tkinter import Tk, Canvas
from time import sleep
window = Tk()
window.title("The window")
canvas = Canvas(window,width=400,height=400, bg="black")
ball = canvas.create_oval(110,10,140,40,fill="yellow")
canvas.pack()
y = 1
while True:
	pos = canvas.coords(ball)
	if pos[3] > 400 or pos[1] < 0:
		y = -y
	canvas.move(ball,0,y)
	sleep(0.002)
	window.update()

window.mainloop()