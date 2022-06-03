from turtle import Turtle
import random
MOVE_DISTANCE = 5

COLOURS = ["red", "white", "yellow", "green", "purple"]


class Alien(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_block(position)

    def create_block(self, position):
        self.shape("turtle")
        self.setheading(270)
        self.turtlesize(stretch_wid=1.5, stretch_len=1)
        self.color(random.choice(COLOURS))
        self.penup()
        self.goto(position)

    def left(self, **kwargs):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def right(self, **kwargs):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def down(self, **kwargs):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)