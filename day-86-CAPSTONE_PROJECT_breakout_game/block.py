from turtle import Turtle
import random

COLOURS = ["red", "blue", "yellow", "green", "purple"]

class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_block(position)

    def create_block(self, position):
        self.shape("square")
        self.turtlesize(stretch_wid=0.5, stretch_len=2.75)
        self.color(random.choice(COLOURS))
        self.penup()
        self.goto(position)
