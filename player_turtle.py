from turtle import Turtle
MOVE_DISTANCE = 20
DEFAULT_POSITION = (0, -275)

class Player_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Yellow")
        self.penup()
        self.shapesize(1.2)
        self.setheading(90)
        self.reset_position()
        self.speed("fastest")


    def move(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_backward(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_right(self):
        x = self.xcor() + MOVE_DISTANCE
        self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - MOVE_DISTANCE
        self.goto(x, self.ycor())

    def reset_position(self):
        self.goto(DEFAULT_POSITION)













