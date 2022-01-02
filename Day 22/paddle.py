from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)



