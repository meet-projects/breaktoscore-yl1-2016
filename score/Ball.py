from turtle import *
from Paddle import *
class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy, color="blue"):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.radius = radius
		self.dx = dx
		self.dy = dy
		self.shape("circle")

	def get_radius(self):
		return self.radius
	def get_dx(self):
		return self.dx
	def get_dy(self):
		return self.dy
	def set_radius(self, new_radius):
		self.radius= new_radius
	def set_dx(self, new_dx):
		self.dx = new_dx
	def set_dy(self, new_dy):
		self.dy = new_dy
	
	def move(self,CANVAS_WIDTH,CANVAS_HEIGHT):
		self.goto(self.xcor()+self.dx , self.ycor()+self.dy)
		if (self.xcor() > CANVAS_WIDTH/2) or (self.xcor() < CANVAS_WIDTH/-2):
			self.dx=-self.dx 
			return self.dx
		if (self.ycor() > CANVAS_HEIGHT/2) :
			self.dy=-self.dy
		