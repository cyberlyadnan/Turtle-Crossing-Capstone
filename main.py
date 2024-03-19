import time
from turtle import Screen
from player_turtle import Player_Turtle
from car import Car
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player_turtle = Player_Turtle()
car = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player_turtle.move, "w")
screen.onkey(player_turtle.move_backward, "s")
screen.onkey(player_turtle.move_right, "d")
screen.onkey(player_turtle.move_left, "a")





is_game = True
while is_game:
    # scoreboard.display()
    car.create_car()
    time.sleep(.2)
    car.move_cars()
    screen.update()

    for position in car.all_cars:
        if player_turtle.distance(position) < 20:
            is_game = False

    if player_turtle.ycor() > 290:
        player_turtle.reset_position()
        car.level_up()
        scoreboard.increase_score()





















screen.exitonclick()