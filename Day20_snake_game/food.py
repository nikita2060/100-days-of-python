from turtle import Turtle
from random import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.random_position()

    def random_position(self):
        """moves food to random position"""
        self.goto(randint(-270, 270), randint(-270, 270))
