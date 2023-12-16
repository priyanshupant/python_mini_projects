from turtle import Turtle

class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 60)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 60)
