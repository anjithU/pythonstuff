from turtle import Turtle,Screen
import time

from snake import Snake
from food import Food

from scoreboard import Scoreboard


# Classes

screen = Screen()


# Screen Set up
screen.screensize(600,600)
screen.bgcolor("Black")
screen.title("Snake Game 🐍!")

screen.tracer(1)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(.1)

	snake.move()

	if snake.head.distance(food) <25:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()
		screen.update()


	# Detect collision with tail

	for segment in snake.segments:
		if segment ==snake.head:
			pass
		elif snake.head.distance(segment) <10:
			game_is_on = False
			scoreboard.game_over()


	#___Detect_Collision

	if snake.head.xcor()> 280 or snake.head.xcor()>-280 or snake.head.ycor()>280 or snake.head.ycor()>-280:
		break


screen.exitonclick()





# # turtle

# start_snake_list = []


# def snake_block():

# 	y = 20
# 	y_axis = 0
	
	
# 	for i in range(3):
# 			t_snake =Turtle()
# 			t_snake.penup()
# 			t_snake.ht()
# 			t_snake.color("White")
# 			t_snake.speed(9)
# 			t_snake.shape("square")
# 			y_axis +=y
# 			t_snake.setx(y_axis)
# 			start_snake_list.append(t_snake)


# 	for starting_snake in start_snake_list:
# 		starting_snake.speed(0)
# 		starting_snake.st()

# 	time.sleep(1)

# def moving():
	

# 	def move_forward():
# 		for starting_snake in start_snake_list:
# 			starting_snake.forward(10)
# 			time.sleep(2)
		


# 	def move_backward():
# 		for starting_snake in start_snake_list:
# 			starting_snake.bk(10)



# 	def move_right():
# 		for starting_snake in start_snake_list:
# 			starting_snake.right(90)
# 			starting_snake.forward(10)



# 	def move_left():
# 		for starting_snake in start_snake_list:
# 			starting_snake.left(90)


# 	move_backward()



# snake_block()

# while True:
# 	moving()

# # exit

# screen.listen()
# screen.exitonclick()




# """

# from turtle import Screen,Turtle
# import time

# screen = Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor('black')
# screen.title("My Snake Game")
# screen.tracer(0)

# starting_position = [(0,0),(-20,0),(-40,0)]

# segments = []

# for position in starting_position:
# 	new_segment =Turtle("square")
# 	new_segment.penup()
# 	new_segment.color("White")
# 	new_segment.goto(position)
# 	segments.append(new_segment)


# game_is_on = True




# while game_is_on:
# 	screen.update()
# 	time.sleep(.1)
# 	for segment in segments:
# 		segment.forward(20)


# 	for seg_num in  range(len(segments)-1,0,-1):
# 		new_x = segments[seg_num-1].xcor()
# 		new_y = segments[seg_num-1].ycor()
# 		new_y = segments[seg_num].goto(new_x,new_y)
# 		segments[0].forward(20)


# screen.exitonclick()

# """