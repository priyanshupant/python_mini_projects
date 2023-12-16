import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 500)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle_list = []
first_position = 0

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    turtle_list.append(new_turtle)
    new_turtle.goto(-220, -100 + first_position)
    first_position += 50

user_bet = screen.textinput("Make a bet: ", "Which turtle will win? Bet on a color: ")
race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() < 220:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            winner = turtle.pencolor()
            if user_bet == winner:
                print("YOU WINN!!")
            else:
                print("YOU LOSE!!")
            print(f"{winner.upper()} won the race.")
            race_on = False

screen.exitonclick()
