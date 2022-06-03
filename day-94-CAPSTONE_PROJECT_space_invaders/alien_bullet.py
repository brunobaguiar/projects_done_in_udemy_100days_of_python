from turtle import Turtle


class AlienBullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape()
        self.color("yellow")
        self.penup()
        self.goto(position)
        self.shapesize(1, 1)
        self.setheading(270)
        self.forward(20)
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.forward(self.y_move)

    def hide_bullet(self):
        self.hideturtle()

    def show_bullet(self, position):
        self.goto(position)
        self.forward(20)
        self.showturtle()
