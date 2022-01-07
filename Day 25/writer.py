from turtle import Turtle

FONT = ("Ariel", 8, "normal")


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("black")

    def write_to_map(self, state, x, y):
        self.goto(x, y)
        self.write(state, font=FONT)
