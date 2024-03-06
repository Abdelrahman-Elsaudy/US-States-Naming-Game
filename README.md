# USA States Naming Game

---

- On this game you get asked to name the USA states that you know, each time you enter a correct state it appears on the
map in black.

![states screenshot](https://github.com/Abdelrahman-Elsaudy/US-States-Naming-Game/assets/158151388/5415dfd2-1e01-4ed2-852a-c84271cc3454)
- If you decide to quit and type "quit" then each state you missed appears on the map in red.
![states screenshot2](https://github.com/Abdelrahman-Elsaudy/US-States-Naming-Game/assets/158151388/df3446fd-c756-439f-87ea-c0e431535688)

---

## Applied Skills:

---

**1. Object-Oriented Programming**

On the `brain.py` page we define a class that operates the game, it's responsible for:
- Evaluating the user's answer: if it was not provided before, it's added to his right answers list (from which we calculate the score
and determine the unknown states) and then this answer is positioned in its coordinates on the map.
```
    def evaluate(self, answer):
        if answer not in self.answers_list:  # The input was not provided before
            self.answers_list.append(answer)
            right_answer_row = data[data.state == answer]
            self.positioning(int(right_answer_row["x"].iloc[0]), int(right_answer_row["y"].iloc[0]), answer,
                             "black", 8)
        else:
            return False
```
- Positioning: making the text appear on screen, we provide it with the text, its x and y coordinates, color and font size.
    - I used this function to pinpoint the named states, pinpoint the missed states, write the "You Won" statement and write
  the "final score" statement.
```
    def positioning(self, x, y, text, color, font_size):
        statement = Turtle()
        statement.hideturtle()
        statement.penup()
        statement.color(color)
        statement.goto(x, y)
        statement.write(text, move=False, font=('Arial', font_size, 'normal'))
```

**2. GUI with Turtle Module**

- Creating the screen with the background of the blank USA States map on which the states are positioned.
- Creating an interactive text input box to get the user's answer and provide them with a feedback on whether
that answer was right or wrong or entered before, and announce winning when they finish naming the states.

**3. List Comprehension**
```
missed_states = [state for state in states_list if state not in brain.answers_list]
```

**4. Reading/Writing of csv Files with Pandas Module**

- Reading the provided csv file that contains the names of the 50 states and their coordinates on the map picture to 
evaluate the user's answer and position the states on the map.
- Writing the missed states in a separate csv file.
```
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
```

---

## Note:

---

- You can use this code to memorize the states of any country by writing them down in a csv file, getting a blank picture
of the country's map and figuring out the coordinates of each state on that map by trial and error.
---

_Credits to: 100-Days of Code Course on Udemy._