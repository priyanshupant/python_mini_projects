import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        x=random.randint(-260,260)
        y=random.randint(-260,260)
        self.goto(x, y)