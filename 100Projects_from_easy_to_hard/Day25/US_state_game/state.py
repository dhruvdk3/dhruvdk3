from turtle import Turtle
FONT = ("Courier", 8, "normal")
class Stategoto(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        self.hideturtle()
        self.pu()
        self.goto(x,y)
        self.write(f"{state}", align="center", font=FONT)