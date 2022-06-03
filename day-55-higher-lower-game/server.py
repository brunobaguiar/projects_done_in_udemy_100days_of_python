from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def guess_a_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200">'

random_number = random.randint(1,9)
print(random_number)


@app.route('/<int:number>')
def guessed_number(number):
    if number < random_number:
        return f'<h1 style="color: red">{number} is too low</h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_number:
        return f'<h1 style="color: purple">{number} is too high</h1>'\
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return "<h1 style='color: green'>You found me!</h1>"\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


# def make_bold(function):
#     def wrapper_function():
#         text = "<b>" + function() + "</b>"
#         return text
#     return wrapper_function


if __name__ == "__main__":
    app.run(debug=True)
