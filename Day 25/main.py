import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("US States Game")
screen.screensize()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

map_writer = Writer()
states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()

# # Auto map all states
# for index, state in states_data.iterrows():
#     map_writer.write_to_map(state.state, state.x, state.y)

correct_answers = 0
while correct_answers < 50:
    title = f"{correct_answers}/{len(states_data.state)} "
    user_guess = screen.textinput(title=title, prompt="Guess a state?").title()

    if user_guess in states:
        state = states_data[states_data.state == user_guess]
        map_writer.write_to_map(user_guess, int(state.x), int(state.y))
        correct_answers += 1
        states.remove(user_guess)


screen.exitonclick()
