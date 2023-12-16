import time
from turtle import Screen, Turtle
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PongGame')
screen.tracer(0)

r_pad = Pad((350, 0))
l_pad = Pad((-350, 0))

r_score = Scoreboard((100, 200))
l_score = Scoreboard((-100, 200))
ball = Ball()


screen.listen()
screen.onkey(r_pad.up, 'i')
screen.onkey(r_pad.down, 'k')
screen.onkey(l_pad.up, 'w')
screen.onkey(l_pad.down, 's')

speed = 0.05
game_on = True
while game_on:
    screen.update()
    ball.move()
    ball.bounce_wall()
    time.sleep(speed)

    if ball.distance(r_pad) < 50 or ball.distance(l_pad) < 50:
        ball.bounce_pad()
        speed *= 0.95


    if ball.xcor() > 400:
        l_score.update()
        ball.goto(0, 0)
        ball.x_shift *= -1
        speed = 0.05

    if ball.xcor() < -400:
        r_score.update()
        ball.goto(0, 0)
        ball.x_shift *= -1
        ball.y_shift *= -1
        speed = 0.05

screen.exitonclick()
