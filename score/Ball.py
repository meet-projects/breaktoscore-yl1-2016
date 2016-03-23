from turtle import *
class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy, color="blue"):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.radius = radius*20
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius,radius,2)

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
	
	def move(self,WIDTH,HEIGHT):
		self.goto(self.xcor()+self.dx , self.ycor()+self.dy)
		if (self.xcor() > WIDTH) or (self.xcor() < -WIDTH):
			self.dx=-self.dx 
		if (self.ycor() > HEIGHT) :
			self.dy=-self.dy
		
