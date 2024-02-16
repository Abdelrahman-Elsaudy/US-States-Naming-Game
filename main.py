from turtle import Screen
import pandas
from brain import Brain, data, states_list

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

brain = Brain()

game_on = True
answer = screen.textinput(f"Your score = {len(brain.answers_list)}/50",
                          "Enter the state name below, or type 'quit' to know the states you missed").title()
message = None

while game_on:
    if answer == "Quit":
        break
    elif answer not in states_list:
        message = "There is no such state. Enter another state:"
    elif answer in states_list and brain.evaluate(answer) is False:
        message = "You already entered that before. Enter another state:"
    else:
        message = "Enter the state name below, or type 'quit' to know the states you missed"

    answer = screen.textinput(f"Your score = {len(brain.answers_list)}/50", message).title()

    if len(brain.answers_list) == 50:
        brain.positioning(0, 0, "YOU WON!", "black", 16)
        break


# Writing the final conclusion on top.
brain.positioning(-230, 260, f"Your scored {len(brain.answers_list)}/50, missed states are written in 'red'.",
                  "black", 16)


# Writing the missed states, each state in its position on the map, each is written in red.
missed_states = [state for state in states_list if state not in brain.answers_list]
for state in missed_states:
    missed_state_row = data[data.state == state]
    brain.positioning(int(missed_state_row["x"].iloc[0]), int(missed_state_row["y"].iloc[0]), state,
                      "red", 8)


# Saving the missed states in a csv file.
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()
