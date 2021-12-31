import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_position = -240
y_position = -125
t_distance = 50
all_racers = []
race_in_progress = False

for t_color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(t_color)
    turtle.penup()
    turtle.goto(x_position, y_position)
    y_position += t_distance
    all_racers.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race?  Enter a color:").lower()

if user_bet:
    race_in_progress = True

while race_in_progress:
    for racer in all_racers:
        if racer.xcor() > 230:
            race_in_progress = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)


screen.exitonclick()
