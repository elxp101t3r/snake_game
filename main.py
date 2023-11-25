from turtle import Screen, Turtle
from config import *
from snake import Snake
import time


snake = Snake()



game_mode = True

while game_mode:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
        



screen.exitonclick()
