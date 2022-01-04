import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐢🏁 Turtle Crossing 🐢🏁")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=player.move_player)
screen.onkeypress(key="Up", fun=player.move_player)


game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.car_fleet:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if the player crosses the finish line
    if player.ycor() >= player.finish_line:
        scoreboard.increase_level()
        car_manager.increase_speed()
        player.reset_player()

    # Manage the volume of cars on the screen
    if counter % car_manager.car_volume == 0:
        car_manager.create_car()
        counter = 0

    counter += 1

screen.exitonclick()
