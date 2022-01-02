from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.location = location
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(self.location)
        message = f"Score: {self.score}"
        self.write(message, align="center", font=("Arial", 14, "normal"))

    def add_point(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 32, "bold"))
