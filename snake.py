from turtle import Turtle

S_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
    
    def increase_body(self):
        last_block = self.blocks[-1].clone()
        self.blocks.append(last_block)
            
    def head_hit_tail(self):
        if len(self.blocks)>3 and self.blocks[0].distance(self.blocks[-1])<5:
            return True
        else:
            return False

            
    def move(self):
        """Moving the snake"""
        for block in range(len(self.blocks) - 1, 0, -1):
            n_x = self.blocks[block - 1].xcor()
            n_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(n_x, n_y)
        self.head.forward(MOVE_D)
    
    
    def up(self):
        """Moving the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
        
    def down(self):
        """Moving the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        """Moving the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
       
    
    def right(self):
        """Moving the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        