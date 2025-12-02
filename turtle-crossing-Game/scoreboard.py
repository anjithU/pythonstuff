from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.level =1
        self.update_score_boadrd()

    def update_score_boadrd(self):
        self.clear()
        self.write(f"level = {self.level}" , align="left",font = FONT) 

    def level_increase(self):
        self.level +=1
        self.update_score_boadrd()

    
