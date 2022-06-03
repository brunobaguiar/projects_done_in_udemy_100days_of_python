from turtle import Turtle
MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())
