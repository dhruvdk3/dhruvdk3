from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):   
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("highscore.txt","r+") as f:
            self.high_score = int(f.read())
            
        self.score = 0
        self.pu()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("highscore.txt","w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        