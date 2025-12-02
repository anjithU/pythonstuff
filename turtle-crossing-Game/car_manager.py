import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # def __init__(self):
    #     super().__init__()
    #     self.penup()
    #     self.color(random.choice(COLORS))
    #     self.shapesize(2, 4)
    #     self.shape("square")



    def __init__(self):
        self.all_cars = []


    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(2,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y =random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car) 
       


    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

