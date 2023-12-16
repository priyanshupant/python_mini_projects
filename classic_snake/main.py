# create snake, make snake move with pretty animation with keyboard, avoid it moving back

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    collision_with_wall = snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.\
        ycor() > 280

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.create_segment(snake.snake_segments[-1].pos())

    if collision_with_wall:
        score.reset()
        snake.reset_snake()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()

screen.exitonclick()
