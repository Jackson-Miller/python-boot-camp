from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """ Create a player object """
        super().__init__()
        self.finish_line = FINISH_LINE_Y
        self.shape("turtle")
        self.color("darkgreen")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_player(self):
        """ Move the player forward along the Y axis"""
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        """ Set the player back to the starting position """
        self.clear()
        self.goto(STARTING_POSITION)