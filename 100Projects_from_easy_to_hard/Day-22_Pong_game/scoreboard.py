from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.pu()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore, align = "center", font = ("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.rscore, align = "center", font = ("Courier", 80, "normal"))
        
    def left_score(self):
        self.lscore +=1
        self.update_scoreboard()
    def right_score(self):
        self.rscore +=1
        self.update_scoreboard()
    
    def l_win(self):
        self.goto(-150,0)
        self.write("WIN",align = "center", font = ("Courier", 40, "normal"))
    def l_win(self):
        self.goto(150,0)
        self.write("WIN",align = "center", font = ("Courier", 40, "normal"))