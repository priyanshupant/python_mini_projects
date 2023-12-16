from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.x_shift = 10
        self.y_shift = 10

    def move(self):
        new_x = self.xcor() + self.x_shift
        new_y = self.ycor() + self.y_shift
        self.goto(new_x, new_y)

    def bounce_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_shift *= -1

    def bounce_pad(self):
        if self.xcor() > 330 or self.xcor() < -330:
            self.x_shift *= -1


