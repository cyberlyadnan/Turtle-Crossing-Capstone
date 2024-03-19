import random
from turtle import Turtle
from player_turtle import Player_Turtle

COLORS = ["blue", "Green", "red", "White", "orange", "purple"]
# DEFAULT_SPEED = 5
SPEED_INCREASE = 10
# CAR_AT_X = 270
# CAR_AT_Y = [-200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190, 220]


class Car:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = 10




    def create_car(self):
        make_cars = random.randint(1,6)
        if make_cars == 1 or make_cars == 4:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.setheading(180)
            y_point = random.randint(-240, 250)
            car.goto(280, y_point)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += SPEED_INCREASE




















