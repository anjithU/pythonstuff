from turtle import Turtle 

WIDTH = .10
HEIGHT = 10
FORWARD_LENGTH = 20
BACKWARD_LENGTH = 20

class Paddle(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.color("white")
		self.shape("square")
		self.turtlesize(HEIGHT,WIDTH)

	def move_up(self):
		self.teleport(self.xcor(),self.ycor()+20)

	def move_down(self):
		self.teleport(self.xcor(),self.ycor()-20)
