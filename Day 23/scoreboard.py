from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """ Create the scoreboard object """
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 275)
        self.write_score()

    def write_score(self):
        """ Write the text to the screen """
        self.clear()
        message = f"Level: {self.level}"
        self.write(message, font=("Courier", 14, "normal"))

    def increase_level(self):
        """ Increase the user leve and update the text on screen """
        self.level += 1
        self.write_score()

    def game_over(self):
        """ Write the game over message on screen """
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 32, "bold"))
