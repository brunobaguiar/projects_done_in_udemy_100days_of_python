from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.write(arg=f"Level:{self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self, level):
        self.level = level
        self.create_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", align="center", font=FONT)
