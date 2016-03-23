from turtle import *
class Paddle(Turtle):
	def __init__(self, x, y,width ,height ,dx, color="black"):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.dx = dx
		self.width = width*20
		self.height = height*20 
		self.shape("square")
		self.shapesize(width,height,2)
		self.pu()	
		self.goto(x,y)
	
	#def get_dx(self):
	#	return self.dx
	#def set_dx(self, new_dx):
	#	self.dx = new_dx
	
	def move(self):
		self.goto(self.xcor()+self.dx , self.ycor())
		self.dx = 0
