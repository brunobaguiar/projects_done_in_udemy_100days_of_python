from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = 1
current_card = {}

# Creating dictionary from english_words
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/english_words.csv")
    to_learn = data.to_dict(orient="records")
    data.to_csv("./data/words_to_learn.csv", index=False)


def remove_card():
    global current_card
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global timer
    global current_card
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front_image)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=(current_card["English"]), fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    translated_card = current_card["Português"]
    canvas.itemconfig(card_bg, image=card_back_image)
    canvas.itemconfig(title_text, text="Português", fill="white")
    canvas.itemconfig(word_text, text=translated_card, fill="white")


# Creating GUI Interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_button_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_button_image, highlightthickness=0, command=remove_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
