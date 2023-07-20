COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self, speed_variable):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE+(MOVE_INCREMENT*(speed_variable-1)))
    