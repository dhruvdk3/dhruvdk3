import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()


screen.listen()
screen.onkey(key= "Up", fun=player.move)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.create_car()
    carmanager.move_cars(scoreboard.level)
    
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor()>280:
        player.reset()
        scoreboard.level_up()
screen.exitonclick()