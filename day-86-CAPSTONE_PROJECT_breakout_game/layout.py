from turtle import Turtle
ALIGNMENT = "center"


class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.screen_line = Turtle()
        self.screen_line.hideturtle()
        self.screen_line.pensize(10)
        self.screen_line.color("white")
        self.screen_line.penup()
        self.screen_line.goto(-397, -320)
        self.screen_line.left(90)
        self.screen_line.pendown()
        self.screen_line.forward(700)
        self.screen_line.penup()
        self.screen_line.goto(390, -320)
        self.screen_line.pendown()
        self.screen_line.forward(700)
        self.screen_line.penup()
        self.screen_line.goto(-390, 290)
        self.screen_line.pensize(40)
        self.screen_line.right(90)
        self.screen_line.pendown()
        self.screen_line.forward(1000)
        self.screen_line.penup()
        self.screen_line.goto(-400, -300)
        self.screen_line.pensize(40)
        self.screen_line.pendown()
        self.screen_line.forward(1000)


