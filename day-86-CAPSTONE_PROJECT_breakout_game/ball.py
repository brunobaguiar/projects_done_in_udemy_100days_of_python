from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -250)
        self.shapesize(0.5, 0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.x_move *= -1

    def bounce_roof(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1
        self.move_speed *= 1  # set as 0.9 to increase speed after bounce paddle

    def refresh(self):
        self.clear()
        self.goto(0, -250)
        self.move_speed = 0.1
        self.bounce_paddle()
