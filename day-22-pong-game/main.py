from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


while True:
    # Screen Setup
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Nabashi Pong Game")
    screen.tracer(0)

    # Middle dashed line
    screen_line = Turtle()
    screen_line.hideturtle()
    screen_line.color("white")
    screen_line.penup()
    screen_line.goto(0, -300)
    screen_line.left(90)
    screen_line.pendown()
    for n in range(15):
        screen_line.forward(20)
        screen_line.pendown()
        screen_line.forward(20)
        screen_line.penup()
    screen.update()

    l_scoreboard = Scoreboard(1)
    r_scoreboard = Scoreboard(-1)
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(l_paddle.up, "w")
    screen.onkeypress(l_paddle.down, "s")
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")

    is_game_on = True
    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_wall()

        # Detect collision with r_paddle
        if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
            ball.bounce_paddle()
        # Detect when paddle misses
        if ball.xcor() == 380:
            l_scoreboard.refresh(1)
            ball.refresh()
        elif ball.xcor() == -380:
            r_scoreboard.refresh(-1)
            ball.refresh()
    screen.clearscreen()



screen.exitonclick()