from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from bullet import Bullet
from layout import Layout
from alien import Alien
from alien_bullet import AlienBullet
from block import Block
import random
import time

restart_game = True
while restart_game:
    # Screen setup
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Nabashi Space Invaders Game")
    screen.tracer(0)

    # Layout
    layout = Layout()
    screen.update()

    # Creating scoreboard
    scoreboard = Scoreboard()

    # Creating paddle
    paddle = Paddle((0, -220))

    # Create bullet
    bullet = Bullet((0, -200))

    # Create blocks in 1/5 probability
    blocks = []
    for line in range(-100, 30, 10):
        for column in range(-380, 380, 20):
            if 3 == random.randint(0,5):
                blocks.append(Block((column, line)))

    # Create aliens
    aliens = [Alien((column, line)) for line in range(100, 200, 45) for column in range(-270, 270, 60)]


    def fire():
        if not bullet.isvisible() or bullet.ycor() > 280:
            bullet.show_bullet(paddle.current_position())


    screen.listen()
    screen.onkeypress(paddle.left, "a")
    screen.onkeypress(paddle.right, "d")
    screen.onkeypress(fire, "space")

    alien_bullets = []
    is_game_on = True
    change_direction = False
    while is_game_on:
        time.sleep(bullet.move_speed)
        screen.update()
        bullet.move()

        # Aliens fire alien_bullets at a 1/100 probability
        for alien in aliens:
            if 15 == random.randint(0, 100):
                alien_bullets.append(AlienBullet(alien.pos()))
        for alien_bullet in alien_bullets:
            alien_bullet.move()

        # Move aliens left and right
        if change_direction:
            for alien in aliens:
                alien.right()
                if alien.xcor() > 350:
                    change_direction = False
        else:
            for alien in aliens:
                alien.left()
                if alien.xcor() < -350:
                    change_direction = True
        # Move aliens down
        if 15 == random.randint(0, 50):
            for alien in aliens:
                alien.down()

        if scoreboard.lives < 1:
            is_game_on = False

        # Check collision bullet with aliens (alien hide, bullet hide, +10 points)
        for alien in aliens:
            if (bullet.distance(alien) < 15 and alien.isvisible()) and bullet.isvisible():
                alien.hideturtle()
                bullet.hide_bullet()
                scoreboard.refresh()

        # Check collision paddle with aliens (Game Over)
        for alien in aliens:
            if paddle.distance(alien) < 30 and alien.isvisible():
                is_game_on = False

        # Check collision alien_bullets with paddle (lose a life, back to center)
        for alien_bullet in alien_bullets:
            if alien_bullet.distance(paddle) < 15 and alien_bullet.isvisible():
                alien_bullet.hide_bullet()
                scoreboard.lose_life()

        # Check collision alien_bullets with bullet (both hidden)
        for alien_bullet in alien_bullets:
            if alien_bullet.distance(bullet) < 8 and alien_bullet.isvisible() and bullet.isvisible():
                alien_bullet.hide_bullet()
                bullet.hide_bullet()

        # Check collision alien_bullets and bullets with blocks (both hidden)
        for block in blocks:
            for alien_bullet in alien_bullets:
                if block.distance(alien_bullet) < 15 and alien_bullet.isvisible() and block.isvisible():
                    alien_bullet.hide_bullet()
                    block.hideturtle()
            if block.distance(bullet) < 15 and bullet.isvisible() and block.isvisible():
                bullet.hide_bullet()
                block.hideturtle()
    if screen.textinput("Restart", "Want to play again? Type 'y' or 'n'. ") != "n":
        screen.clearscreen()
        restart_game = True
    else:
        restart_game = False
    screen.clearscreen()
