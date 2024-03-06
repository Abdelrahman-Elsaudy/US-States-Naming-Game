from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


class Brain(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.answers_list = []

    def positioning(self, x, y, text, color, font_size):
        statement = Turtle()
        statement.hideturtle()
        statement.penup()
        statement.color(color)
        statement.goto(x, y)
        statement.write(text, move=False, font=('Arial', font_size, 'normal'))

    def evaluate(self, answer):
        if answer not in self.answers_list:  # The input was not provided before
            self.answers_list.append(answer)
            right_answer_row = data[data.state == answer]
            self.positioning(int(right_answer_row["x"].iloc[0]), int(right_answer_row["y"].iloc[0]), answer,
                             "black", 8)
        else:
            return False
