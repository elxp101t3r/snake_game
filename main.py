from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SnakeGame')


x_pos = 0

for i in range(0, 3):
    i = Turtle()
    i.shape('square')
    i.color('white')
    i.setposition(x=x_pos, y=0)
    x_pos -= 20
   









screen.exitonclick()
