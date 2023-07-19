from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.goto(cord)
    
    def up(self):
        if self.ycor()<250:
            self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(),self.ycor()-20)
    
