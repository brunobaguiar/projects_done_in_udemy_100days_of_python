from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.create_score(position)

    def create_score(self, position):
        """"Position 1 for player 1 position -1 for player 2"""
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((-100)*position, 200)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def refresh(self, position):
        self.score += 1
        self.clear()
        self.goto((-100)*position, 200)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)