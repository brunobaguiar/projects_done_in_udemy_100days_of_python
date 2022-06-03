from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.create_score(position)

    def create_score(self, position):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((0)*position, 210)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def refresh(self, position):
        self.score += 1
        self.clear()
        self.goto((0)*position, 200)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def reset(self, position):
        self.score = 0
        self.clear()
        self.goto((0)*position, 200)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)
