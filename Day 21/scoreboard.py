from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 280)
        message = f"Score: {self.score}    High Score: {self.high_score}"
        self.write(message, align="center", font=("Arial", 14, "normal"))

    def add_point(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Courier", 32, "bold"))
