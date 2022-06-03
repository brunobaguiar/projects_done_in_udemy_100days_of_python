from tkinter import *
import math

SENTENCE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
           "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
           "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " \
           "mollit anim id est laborum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
           "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
           "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate " \
           "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, " \
           "sunt in culpa qui officia deserunt mollit anim id est laborum".lower()
n = 0
typing_counting = 0
timer = None

# Position variables for progress indication color, initial position = [1.0, 1.0]
line = 1
column = 0
position_list = [str(line), str(column)]
correct_answer_position = [1.0, float(".".join(position_list))]


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global n, typing_counting, column
    window.after_cancel(timer)
    timer_text.delete("1.0", "1.5")
    timer_text.insert(INSERT, f"0:00")
    wpm_text.delete("1.0", "1.5")
    wpm_text.insert(INSERT, f"0")
    n = 0
    typing_counting = 0
    column = 0
    start()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    work_sec = 60
    count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    time_passed = abs(count_min+(count_sec/60)-1)
    wpm_calc = (typing_counting/5)/(time_passed+0.0001)
    print(wpm_calc)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    timer_text.delete("1.0", "1.5")
    timer_text.insert(INSERT, f"{count_min}:{count_sec}")
    wpm_text.delete("1.0", "1.5")
    wpm_text.insert(INSERT, f"{int(wpm_calc)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        end_game()


def right_answer():
    global n, typing_counting, column
    typing_counting += 1
    column += 1
    n = n + 1
    position_list = [str(line), str(column)]
    correct_answer_position = [1.0, float(".".join(position_list))]
    # Coloring the text based on the users typing
    text.tag_add("current_position", correct_answer_position[1])
    text.tag_add("correct_answer", correct_answer_position[0], correct_answer_position[1])
    text.tag_config("current_position", background="yellow")
    text.tag_config("correct_answer", background="green")


# Checking typing function
def check_typing(*args):
    user = (var.get().strip()[-1])
    if user == SENTENCE[n]:
        right_answer()


def jump():
    right_answer()


def end_game():
    global n, typing_counting, column
    window.after_cancel(timer)
    timer_text.delete("1.0", "1.5")
    timer_text.insert(INSERT, f"0:00")

# GUI Interface

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, bg="grey")
var = StringVar()

# WPM E1 value, need to make the calculation
Label(text="WPM:").grid(column=0, row=0)
wpm_text = Text(window, bg="#B7E3E9", height=1, width=10)
wpm_text.grid(column=1, row=0)

# Timer E2, need to implement the timer
Label(text="TIMER:").grid(column=2, row=0)
timer_text = Text(window, bg="#B7E3E9", height=1, width=10)
timer_text.grid(column=3, row=0)

# Random text, need to implement random text and script to color and progress
text = Text(window, bg="#B7E3E9", height=10, width=60)
text.insert(INSERT, SENTENCE)
text.grid(column=0, row=1, columnspan=4, pady=20)
text.config(state=DISABLED)

# User entry text box for typing
type_entry = Entry(window, textvariable=var)
type_entry.grid(column=0, row=2, columnspan=4)
type_entry.focus_set()

# Buttons

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=0, row=3)

# Solution for space between words
window.bind('<space>', lambda event: jump())
# ‘observer’ callback to the variable, calls the function with the user key input as var
var.trace('w', check_typing)

start()

window.mainloop()
