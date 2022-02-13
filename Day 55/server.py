import random
from flask import Flask

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif'>"


@app.route("/<int:number>")
def guess(number):
    if number < random_number:
        return "<h1 style='color: red'>Too low, try again</h1>" \
               "<img src='https://media.giphy.com/media/cJfY82h8ijUFQEmDKa/giphy.gif'>"
    elif number > random_number:
        return "<h1 style='color: purple'>Too high, try again</h1>" \
               "<img src='https://media.giphy.com/media/WEb7qDoPJixO0/giphy.gif'>"
    elif number == random_number:
        return "<h1 style='color: green'>Correct guess!</h1>" \
               "<img src='https://media.giphy.com/media/MuyUK01ZmM5H2/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
