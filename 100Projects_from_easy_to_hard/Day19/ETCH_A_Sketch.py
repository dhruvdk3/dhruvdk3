from turtle import Turtle, Screen
import turtle
from Colors import colors, direction
import random
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,b,g)

a_turtle = Turtle()
a_turtle.shape("turtle")
a_turtle.speed("fastest")

def move_right():
    a_turtle.setheading(a_turtle.heading()-10)
def move_forward():
    a_turtle.forward(10)
def move_backwards():
    a_turtle.backward(10)
def move_left():
    a_turtle.setheading(a_turtle.heading()+10)
def clear():
    a_turtle.clear()
    a_turtle.pu()
    a_turtle.home()
    a_turtle.pd()


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()