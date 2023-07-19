from turtle import Turtle
starting_position = [(0,0),(-20,0),(-40,0)]
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for i in starting_position:
            self.add_segment(i)
    
    def move(self):
        for i in range(len(self.segment)-1 ,0,-1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.head.forward(20)
    
    def add_segment(self, i):
        sq = Turtle("square")
        sq.color("white")
        sq.pu()
        sq.goto(i)
        self.segment.append(sq)
        
    def extend(self):
        self.add_segment(self.segment[-1].position())
    
    
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)