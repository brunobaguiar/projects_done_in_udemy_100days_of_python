import time
from turtle import Screen
from player import Player
from car_management import CarManager
from scoreboard import Scoreboard
import random

restart_game = True
while restart_game:
    # Setup Screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Create and move turtle
    player = Player()
    screen.listen()
    screen.onkeypress(player.up, "Up")

    # Create scoreboard
    scoreboard = Scoreboard()

    # Create cars
    cars = []

    n = 0

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        scoreboard.increase_score(player.level)
        if n % (random.randint(1, 20)) == 0:
            cars.append(CarManager())
        for x in range(len(cars)):
            cars[x].move(player.level)
        for car in cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()
        screen.update()
        n += 1

    if screen.textinput("Restart", "Want to play again? Type 'y' or 'n'. ") != "n":
        screen.clearscreen()
        restart_game = True
    else:
        restart_game = False

screen.exitonclick()
