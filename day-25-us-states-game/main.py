import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=730, height=500)
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
with open("50_states.csv") as file:
    data = pandas.read_csv("50_states.csv")
is_game_on = True
score = 0
states = []
guess_state_list = []
while is_game_on:
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name?").title()
    states = data.state
    answer_correct = False
    if answer_state == "Exit":
        break
    for state in states:
        if answer_state == state:
            guess_state_list.append(state)
            answer_correct = True
            state_writer = Turtle()
            state_writer.penup()
            state_writer.hideturtle()
            state_writer.goto(int(data[data.state == answer_state]["x"]), int(data[data.state == answer_state]["y"]))
            state_writer.write(f"{answer_state}")
            score += 1
    if score == 50:
        is_game_on = False

states_to_learn = []

for state in states:
    if state not in guess_state_list:
        states_to_learn.append(state)

final_data = pandas.DataFrame(states_to_learn)
print(final_data)

# Error on above line, is not creating the file, don't know why, tried relative and absolute paths

final_data.to_csv("/Users/PC/PycharmProjects/pythonProject/us-states-game-start/states_to_learn")
