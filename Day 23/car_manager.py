from turtle import Turtle
import random
COLORS = ["crimson", "dark orange", "gold", "chartreuse", "navy", "indigo"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        """ Create the car manager object """
        self.car_fleet = []
        self.car_movement = STARTING_MOVE_DISTANCE
        self.car_volume = 6
        self.create_car()

    def create_car(self):
        """ Create a car and add to the car managers fleet """
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300, random.randint(-250, 250))
        self.car_fleet.append(car)

    def move_cars(self):
        """ Move the car forward along the X axis"""
        for car in self.car_fleet:
            car.forward(self.car_movement)

    def increase_speed(self):
        """ Increase the movement speed of the cars """
        self.car_movement += MOVE_INCREMENT
        self.increase_traffic()

    def increase_traffic(self):
        """ Increase the volume of cars on screen  """
        if self.car_volume > 1:
            self.car_volume += 1
