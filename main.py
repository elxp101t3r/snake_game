from turtle import Screen
from config import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_mode = True

while game_mode:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.increase_body()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    
    if snake.head_hit_tail() == True:
        score.reset()
        snake.reset()
        
    
screen.exitonclick()
