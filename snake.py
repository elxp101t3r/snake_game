from turtle import Turtle

S_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20

class Snake:
    
    def __init__(self):
        self.blocks = []
        self.snake_create()
        
        
    def snake_create(self):
        for p in S_POSITIONS:
            new_block = Turtle()
            new_block.penup()
            new_block.shape('square')
            new_block.color('white')
            new_block.setposition(p)
            self.blocks.append(new_block)
            
            
    def move(self):
        """Moving the snake"""
        for block in range(len(self.blocks) - 1, 0, -1):
            n_x = self.blocks[block - 1].xcor()
            n_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(n_x, n_y)
        self.blocks[0].forward(MOVE_D)
    
    
    def up(self):
        """Moving the snake up"""
        self.blocks[0].setheading(90)
        
        
    def down(self):
        """Moving the snake down"""
        self.blocks[0].setheading(270)
    
    def left(self):
        """Moving the snake left"""
        self.blocks[0].setheading(180)
       
    
    def right(self):
        """Moving the snake right"""
        self.blocks[0].setheading(0)
        