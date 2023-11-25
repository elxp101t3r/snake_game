from turtle import Screen, Turtle
from config import *
from snake import Snake
import time


snake = Snake()


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
