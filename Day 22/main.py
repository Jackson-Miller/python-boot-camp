from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("🕹️ PONG 🕹️")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((250, 280))
l_scoreboard = Scoreboard((-250, 280))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with the top or bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect the ball going past the paddle
    if ball.xcor() > 380:
        l_scoreboard.add_point()
        ball.refresh()
    elif ball.xcor() < -380:
        r_scoreboard.add_point()
        ball.refresh()

    # End game if someone reaches 10
    if l_scoreboard.score >= 10 or r_scoreboard.score >= 10:
        r_scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
