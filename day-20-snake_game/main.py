from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Nabashi Snake Game")
    screen.tracer(0)

    scoreboard = Scoreboard()
    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            snake.reset()
            scoreboard.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                snake.reset()
                scoreboard.reset()
    screen.exitonclick()

    if not is_game_on:
        decision = screen.textinput("Play Again?", "Want to play again? 'y' or 'n': ")
        if decision == "y":
            screen.resetscreen()
            start()


start()
