from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SnakeGame')
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]

blocks = []

for p in positions:
    new_block = Turtle()
    new_block.penup()
    new_block.shape('square')
    new_block.color('white')
    new_block.setposition(p)
    blocks.append(new_block)
   
screen.update()
game_mode = True

while game_mode:
    screen.update()
    time.sleep(0.1)
    
    for block in range(len(blocks) - 1, 0, -1):
        n_x = blocks[block - 1].xcor()
        n_y = blocks[block - 1].ycor()
        blocks[block].goto(n_x, n_y)
    blocks[0].forward(20)
    
        



screen.exitonclick()
