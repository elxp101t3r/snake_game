from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-50, 270)
        self.score = 0
        self.write(f'Score: {self.score} ', move=False, font=('Courier', 15, 'normal'))
    
    
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write('GAME OVER.', align='center', font=('Courier', 25, 'normal'))
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score} ', move=False, font=('Courier', 15, 'normal'))
              