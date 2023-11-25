from turtle import Turtle


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.blocks = []
    def snake_create(self):
        for p in self.positions:
            new_block = Turtle()
            new_block.penup()
            new_block.shape('square')
            new_block.color('white')
            new_block.setposition(p)
            self.blocks.append(new_block)
    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            n_x = self.blocks[block - 1].xcor()
            n_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(n_x, n_y)
        self.blocks[0].forward(20)