from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
SCOREBOARD_X = 230
SCOREBOARD_Y = -270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.lives = 2
        self.create_score()

    def create_score(self):
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(arg=f"Lives: {self.lives} / Score:{self.score}", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 10
        self.clear()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(arg=f"Lives: {self.lives} - Score:{self.score}", align=ALIGNMENT, font=FONT)

    def lose_life(self):
        self.lives -= 1
        self.clear()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(f"Lives: {self.lives} - Score:{self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.lives = 2
        self.clear()
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.write(f"Lives: {self.lives} - Score:{self.score}", align=ALIGNMENT, font=FONT)
