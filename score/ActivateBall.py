from turtle import *
from Ball import *
from Paddle import *

canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height
def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)

# This function returns the height of the screen
def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)

ball1= Ball(0,0,10,5,3)
paddle1= Paddle(0,-200,1,5,0)
def right(event):
	global paddle1
	print("right")
	paddle1.dx=5
	paddle1.move()
	paddle1.dx=5
def left(event):
	global paddle1
	print("left")
	paddle1.dx=-5
	paddle1.move()
	paddle1.dx=-5

canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
getscreen().listen() # this line tells the screen in turtle to listen to the keyboard and the mouse, because we are using them
	
while True:
	print(CANVAS_WIDTH)
	ball1.move(CANVAS_WIDTH,CANVAS_HEIGHT)
	paddle1.move()

