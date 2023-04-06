from turtle import Turtle
from random import randint

STEP = 10   # 10 pixel because small steps help to detect collisions properly
MOVING_ANGLE = randint(40, 60)  # I experimentally calculated this value
AFTER_COLLISION_MOVING_ANGLE_R = 270 + MOVING_ANGLE
AFTER_COLLISION_MOVING_ANGLE_L = 180 + MOVING_ANGLE
WIDTH_OF_WALL = 800
HEIGHT_OF_WALL = 600
BUFFER_BORDER = 20
UP_BORDER = HEIGHT_OF_WALL/2 - BUFFER_BORDER
DOWN_BORDER = -UP_BORDER

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(MOVING_ANGLE)

    def move_ball(self):
        self.penup()
        self.forward(STEP)

    def detect_collision_with_wall(self):
        if self.ycor() > UP_BORDER:
            if self.xcor() > 0:
                self.setheading(AFTER_COLLISION_MOVING_ANGLE_R)
            else:
                self.setheading(AFTER_COLLISION_MOVING_ANGLE_L)

            self.move_ball()
        if self.ycor() < DOWN_BORDER:
            self.setheading(135)
            self.move_ball()


