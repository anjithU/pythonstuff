from turtle import Turtle

STARTING_POSITIONS =  [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class  Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_segments(position)
			

	def add_segments(self , position):
		new_segment = Turtle("square")
		new_segment.color("White")
		new_segment.penup()
		new_segment.goto(position)
		self.segments.append(new_segment)



	def extend(self):
		self.add_segments(self.segments[-1].position())

	def move(self):
		for seg_num in range(len(self.segments) -1 ,0,-1):
			new_x = self.segments[seg_num -1].xcor()
			new_y = self.segments[seg_num -1].ycor()
			self.head.forward(MOVE_DISTANCE)

	def up(self):
		self.segments[0].setheading(90)



	def down(self):
		self.segments[0].setheading(270)


	def left(self):
		self.segments[0].setheading(180)


	def right(self):
		self.segments[0].setheading(0)

