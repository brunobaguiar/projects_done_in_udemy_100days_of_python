from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
