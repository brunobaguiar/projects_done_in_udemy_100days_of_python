from turtle import Turtle
import random

COLOURS = ["#33EEFF", "#24A2AE", "#1C7C85", "#13545A", "#0E3F44"]


class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_block(position)

    def create_block(self, position):
        self.shape("square")
        self.setheading(270)
        self.turtlesize(stretch_wid=0.8, stretch_len=0.4)
        self.color(random.choice(COLOURS))
        self.penup()
        self.goto(position)
