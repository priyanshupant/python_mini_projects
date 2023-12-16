from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align='center', font=("Courier", '75', "normal"))
