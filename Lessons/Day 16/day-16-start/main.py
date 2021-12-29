# from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
# print(my_screen.exitonclick())

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)

