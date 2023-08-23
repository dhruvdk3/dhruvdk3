from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.bonous = 0
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-280,280), random.randint(-280,280))
    
    def refresh(self):
        self.bonous = random.randint(1,10)
        if self.bonous == 10 :
            self.shapesize(stretch_len=1, stretch_wid=1)
            self.goto(random.randint(-280,280), random.randint(-280,280))   
        else:
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.goto(random.randint(-280,280), random.randint(-280,280))