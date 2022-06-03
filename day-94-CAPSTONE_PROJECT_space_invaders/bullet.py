from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, position, alien=False):
        super().__init__()
        self.shape()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.shapesize(1, 1)
        self.setheading(90)
        self.y_move = 10
        if alien:
            self.setheading(270)
        self.move_speed = 0.1

    def move(self):
        self.forward(self.y_move)

    def hide_bullet(self):
        self.hideturtle()

    def show_bullet(self, position):
        self.goto(position)
        self.forward(20)
        self.showturtle()
