from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SnakeGame')


positions = [(0, 0), (-20, 0), (-40, 0)]

for p in positions:
    new_block = Turtle()
    new_block.shape('square')
    new_block.color('white')
    new_block.setposition(p)
   









screen.exitonclick()
