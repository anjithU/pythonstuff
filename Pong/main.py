from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Score


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# creating a screen and width and direction
screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # 50% of screen width and height
screen.bgcolor("black")  # Set background color
screen.title("Pong!")

screen.tracer(0)



# Paddle Class

#_________Left Paddle ______________


left_paddle =Paddle()
left_paddle.setpos(350,0)




#_________Right Paddle ______________



right_paddle =Paddle()
right_paddle.setpos(-350,0)


		
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")



screen.listen()

#_______________Ball___________


ball = Ball()
score = Score()

#_______________Game______________

game_is_on = True



while game_is_on:
	screen.update()
	
	time.sleep(.005)
	ball.move()

	if ball.ycor() >280 or ball.ycor() <-280:
		ball.bounce_y()


	# detect collision with right paddle

	
	if ball.distance(right_paddle) <10 and ball.xcor()>320:
		self.bounce_x()


	# detect when right paddle misses

	if ball.xcor()>380:
		ball.reset_position()
		ball.bounce_x()

	if ball.xcor()<-380:
		ball.reset_position()
		ball.bounce_y()


		
		


#________________Events __________________




screen.exitonclick()