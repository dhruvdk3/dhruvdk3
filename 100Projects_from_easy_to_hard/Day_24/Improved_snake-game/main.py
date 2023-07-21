from turtle import Screen
import time
from snake import Snake
from food import Food
from scordboard import Scoreboard



screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

speed = 0
dificulty = screen.textinput(title="Select Dificulty", prompt=("Easy/Medium/Hard")).lower()
if dificulty == "easy":
    speed = 0.2
elif dificulty == "medium":
    speed = 0.1
elif dificulty == "hard":
    speed = 0.05

screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
screen.update()
game_is_on  = True
bonous = False
while game_is_on:
    time.sleep(speed)
    screen.update()
    snake.move()
    
    if snake.head.distance(food) < 15 and bonous == False:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
        if food.bonous == 10 :
            bonous = True
    
    if snake.head.distance(food) < 15 and bonous == True:
        for _ in range(5):
            scoreboard.increase_score()
            snake.extend()
        food.refresh()
        if food.bonous == 10 :
            bonous = True
        else : bonous = False
        
    if snake.head.xcor()>280 or snake.head.xcor()< -300 or snake.head.ycor()>300 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segment[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
screen.exitonclick()