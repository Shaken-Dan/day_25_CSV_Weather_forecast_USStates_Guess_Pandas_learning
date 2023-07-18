import csv

import pandas
import turtle

# with open("weather_data.csv") as data:
#     data = data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
# print(temperatures)


# data = pandas.read_csv("weather_data.csv")

# print(data["temp"].max())
# print(data.condition)

""" Get data in row """
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday.condition

""" create a data frame and convert to .csv file """

# data_dict = {}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

""" Squirell counting (my code) """
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# color_column = data["Primary Fur Color"].unique().tolist()
# colors_sorted = [color for color in color_column if type(color) == str]

""" US States Guess Game (my solution)"""
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(width=750, height=550, startx=-620, starty=-160)
screen.title("US States Guess")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states_list = data.state.tolist()

# The name of State
name = turtle.Turtle()
name.penup()
name.hideturtle()

correct_guesses = []

while len(correct_guesses) < 51:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()

    # Identify coordinates
    x_axis = data[data.state == answer_state].x
    y_axis = data[data.state == answer_state].y

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        name.goto(int(x_axis), int(y_axis))
        name.write(answer_state, align="center", font=('Arial', 8, 'normal'))
        correct_guesses.append(answer_state)

# turtle.mainloop()
# screen.exitonclick()

states_to_learn = []
for state in states_list:
    if state not in correct_guesses:
        states_to_learn.append(state)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")

""" US States Guess Game (Angela's solution)"""
# screen = turtle.Screen()
# screen.setup(width=750, height=550, startx=-620, starty=-160)
# screen.title("US States Guess")
# screen.addshape("blank_states_img.gif")
# turtle.shape("blank_states_img.gif")
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []
# #
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         states_to_learn = []
#         for state in states_list:
#             if state not in correct_guesses:
#                 states_to_learn.append(state)
#         new_data = pandas.DataFrame(states_to_learn)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_date = data[data.state == answer_state]
#         t.goto(int(state_date.x), int(state_date.y))
#         t.write(state_date.state.item())
