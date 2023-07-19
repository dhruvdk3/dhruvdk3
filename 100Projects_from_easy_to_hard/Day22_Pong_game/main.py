from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle_cord = [(350,0), (-350,0)]


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

rpaddle = Paddle(paddle_cord[0])
lpaddle = Paddle(paddle_cord[1])


screen.onkey(key="Up", fun=rpaddle.up)
screen.onkey(key="Down", fun=rpaddle.down)
screen.onkey(key="w", fun=lpaddle.up)
screen.onkey(key="s", fun=lpaddle.down)
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    if ball.ycor()>280 or ball.ycor()<-270:
        ball.bounce()
    if ball.xcor()>320 and rpaddle.distance(ball) < 50 or ball.xcor() < -320 and lpaddle.distance(ball) < 50:
        ball.bounce_x()
    ball.move()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()
        if scoreboard.lscore == 10 :
            scoreboard.l_win()
            break
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()
        if scoreboard.rscore == 10 :
            scoreboard.l_win()
            break
screen.exitonclick()