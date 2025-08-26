from random import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize( stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(COLORS[0])
        self.goto(300, -250 + (random() * 500))



    def move(self):
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)




