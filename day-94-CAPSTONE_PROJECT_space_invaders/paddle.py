from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('turtle')
        self.turtlesize(stretch_wid=2, stretch_len=1.5)
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(position)

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def current_position(self):
        return self.pos()
