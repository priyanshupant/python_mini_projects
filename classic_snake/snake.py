from turtle import Turtle
import time

from turtle import Turtle
STARTPOSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVINGDISTANCE=20
UP=90
LEFT=180
RIGHT=0
DOWN=270

class Snake:

    def __init__(self):
        self.snake_segments=[]
        self.create_snake()
        self.head=self.snake_segments[0]

    def create_snake(self):
        for position in STARTPOSITIONS:
            self.extend(position)

    def extend(self,position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg_num].goto(self.snake_segments[seg_num - 1].pos())
        self.snake_segments[0].forward(MOVINGDISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

