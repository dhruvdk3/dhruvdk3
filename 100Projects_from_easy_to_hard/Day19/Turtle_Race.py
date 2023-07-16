from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
turtle_colors = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Indigo",
    "Violet"
]


screen = Screen()
screen.setup(800,500)
y = -150
turtle_list = []
for i in range(7):
    a_turtle = Turtle("turtle")
    a_turtle.pu()
    a_turtle.color(turtle_colors[i])
    a_turtle.goto(-380,y)
    y += 50
    turtle_list.append(a_turtle)

user_bet = screen.textinput(title="Make your bet.",prompt="Which turtlr will win the race?\nEnter a color : ")
user_bet = user_bet.title()
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for i in turtle_list:
        if i.xcor()>380:
            won = i.pencolor()
            is_race_on = False
            if won == user_bet:print(f"You won.\n{won} turtle is winner")
            else: print(f"You lost.\n{won} turtle is winner")
            break
        i.forward(random.randint(0,10))
