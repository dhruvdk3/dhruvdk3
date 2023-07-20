FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-260,260)
        self.level = 1
        self.level_no()
        
    def level_no(self):
        self.write(f"Level: {self.level}",align="left", font=FONT)
    
    def level_up(self):
        self.clear()
        self.level +=1
        self.level_no()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center", font=FONT)