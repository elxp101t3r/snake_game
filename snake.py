from turtle import Turtle

S_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20

class Snake:
    
    def __init__(self):
        self.blocks = []
        self.snake_create()
        self.head = self.blocks[0]
        
        
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
        self.head.forward(MOVE_D)
    
    
    def up(self):
        """Moving the snake up"""
        self.head.setheading(90)
        
        
    def down(self):
        """Moving the snake down"""
        self.head.setheading(270)
    
    def left(self):
        """Moving the snake left"""
        self.head.setheading(180)
       
    
    def right(self):
        """Moving the snake right"""
        self.head.setheading(0)
        