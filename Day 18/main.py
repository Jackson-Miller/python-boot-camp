from turtle import Turtle, Screen
import random

# # # Used to get the colors from the image to be used to recreate the image digitally # # #
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)

image_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def random_color():
    return random.choice(image_colors)


def draw_row(num_dots):
    for _ in range(num_dots):
        r_color = random_color()
        brush.dot(circle_size, r_color)
        brush.forward(circle_distance)


brush = Turtle()
screen = Screen()
brush.hideturtle()
brush.penup()
brush.speed(0)
screen.colormode(255)
num_rows = 10
num_columns = 10
# below variables work for my resolution
circle_size = 30
circle_distance = 50
x_position = -225
y_position = -225


for _ in range(num_rows):
    brush.goto(x_position, y_position)
    draw_row(num_rows)
    y_position += circle_distance

screen.exitonclick()
