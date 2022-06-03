from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from block import Block
from layout import Layout
import time

restart_game = True
while restart_game:
    # Screen Setup
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Nabashi Breakout Game")
    screen.tracer(0)

    # Layout
    layout = Layout()
    screen.update()

    # Creating scoreboard
    scoreboard = Scoreboard(1)
    # Creating paddle
    paddle = Paddle((0, -260))
    # Creating ball
    ball = Ball()
    # Creating blocks
    blocks = [Block((column, line)) for line in range(0, 116, 15) for column in range(-365, 361, 60)]

    screen.listen()
    screen.onkeypress(paddle.left, "a")
    screen.onkeypress(paddle.right, "d")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if ball.xcor() > 365 or ball.xcor() < -370:
            ball.bounce_wall()
        if ball.ycor() > 250:
            ball.bounce_roof()
        # Detect collision on visible blocks, hide them, sum score
        for block in blocks:
            if (ball.distance(block) < 15 or (ball.distance((block.xcor()-19, block.ycor())) or ball.distance((block.xcor()+19, block.ycor()))) < 19) and block.isvisible():
                block.hideturtle()
                ball.bounce_roof()
                scoreboard.refresh(1)

        # Detect collision with paddle
        if ball.ycor() < -240 and ball.distance(paddle) < 50:
            ball.bounce_paddle()
        # Detect when paddle misses
        if ball.ycor() == -280:
            game_is_on = False
    if screen.textinput("Restart", "Want to play again? Type 'y' or 'n'. ") != "n":
        screen.clearscreen()
        restart_game = True
    else:
        restart_game = False
    screen.clearscreen()
