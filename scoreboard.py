from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-50, 270)
        self.score = 0
        self.highscore = 0
        self.write(f'Score: {self.score} High Score: {self.highscore}', align='center',move=False, font=('Courier', 15, 'normal'))
    
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', align='center', font=('Courier', 15, 'normal'))
    
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
              