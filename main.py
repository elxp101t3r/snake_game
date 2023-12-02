from turtle import Screen
from config import *
from snake import Snake
from food import Food
import time


snake = Snake()
food = Food()

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
    
    
screen.exitonclick()
