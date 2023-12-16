from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score=0
        self.write( f'Score: {self.score}', align='center', font=('Arial',12,'normal'))
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write( f'Score: {self.score}', align='center', font=('Arial',12,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=('Arial', 12, 'normal'))