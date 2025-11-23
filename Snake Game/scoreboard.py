from turtle import Turtle

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.goto(0,270)
		self.color('white')
		
		self.hideturtle()
		self.score_board_update()


	def score_board_update(self):
		self.write(f"Score:{self.score}",align="center",font=("Arial",24,'normal'))



	def increase_score(self):
		self.score +=1 
		self.clear()
		self.score_board_update()


	

