color_list = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

import turtle, random
from turtle import Turtle,Screen
turtle.colormode(255)


def random_color(rbg):
    return random.choice(rbg)

tut = Turtle()
tut.hideturtle()
tut.speed("fastest")
tut.setheading(225)
tut.up()
tut.forward(325)
tut.setheading(0)
for i in range(10):
    for _ in range(10):
        tut.dot(20,random_color(color_list))
        tut.forward(50)
        
    tut.left(90)
    tut.forward(50)
    tut.left(90)
    tut.forward(500)
    tut.setheading(0)
    


x = Screen()
x.exitonclick()