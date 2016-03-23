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

ball1= Ball(0,0,1,5,3)
paddle1= Paddle(0,-200,1,5,0)
def right(event):
	global paddle1
	print("right")
	paddle1.dx=20
	
def left(event):
	global paddle1
	print("left")
	paddle1.dx=-20


canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
getscreen().listen() # this line tells the screen in turtle to listen to the keyboard and the mouse, because we are using them

def collide(ball1, paddle1):
	topsidep = paddle1.ycor() + paddle1.height/2
	bottomsidep = paddle1.ycor() - paddle1.height/2
	rightsidep = paddle1.xcor() + paddle1.width/2
	leftsidep = paddle1.xcor() - paddle1.width/2
	topsideb = ball1.ycor() + ball1.radius
	bottomsideb = ball1.ycor() - ball1.radius
	rightsideb = ball1.xcor() + ball1.radius
	leftsideb = ball1.xcor() - ball1.radius
	if (topsidep >= bottomsideb and rightsidep >= leftsideb and leftsidep <= rightsideb and bottomsidep <= topsideb):
		ball1.dy = -ball1.dy
	
	
while True:
	ball1.move(get_screen_width(),get_screen_height())
#	paddle1_top = paddle1.ycor() + paddle1.height/2 
	paddle1.move()
#	if ((paddle1_top > ball1.ycor() - ball1.radius) and ( paddle1.xcor() - paddle1.width/2 < ball1.xcor()) and (ball1.xcor() < paddle1.xcor() +  paddle1.width/2)):
#		print("working")
	collide(ball1, paddle1)		
