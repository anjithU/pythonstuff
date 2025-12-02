import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_fd, "Up")
screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # Detect collision
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        scoreboard.level_increase()
        player.go_to_start()
        scoreboard.level_increase()

# Stop the game safely AFTER loop ends
screen.exitonclick()
