from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
#speed increases with level up
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.list_cars = []
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(x=300, y=random.randint(-250, 250))
        # self.cars.append(self)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*level)

    # def add_car(self):
    #     self.shape("square")
    #     self.turtlesize(stretch_wid=1, stretch_len=2)
    #     self.penup()
    #     self.setheading(180)
    #     self.color(random.choice(COLORS))
    #     self.goto(x=290, y=random.randint(-280, 280))
    #     self.list_cars.append(self)
