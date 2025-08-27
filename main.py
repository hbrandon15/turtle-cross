import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the player
player = Player()

# create the car
car_manager = CarManager()


# Keyboard bindings
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False

    # detect if the player has reached the finish line
    if player.finish_line():
        player.reset_position()
        car_manager.level_up()


screen.exitonclick()






# first we need to create a turtle player that starts at the bottom of the screen and listens for the "UP" keyword.