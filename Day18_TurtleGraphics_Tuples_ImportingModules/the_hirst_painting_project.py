import turtle
from turtle import *
from random import randint

my_turtle = Turtle()
turtle.colormode(255)  # it helps to change rgb composition of our turtle


def random_color():
    """returns  rgb composition of random color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def odd():
    my_turtle.left(90)
    my_turtle.forward(30)
    my_turtle.left(90)


def even():
    my_turtle.right(90)
    my_turtle.forward(30)
    my_turtle.right(90)


#  taking turtle to the lower part of screen so that drawing can be seen properly
my_turtle.setheading(185)
my_turtle.penup()
my_turtle.forward(80)
my_turtle.setheading(0)

line = 1
for _ in range(10):
    for _ in range(9):
        my_turtle.dot(15, random_color())
        my_turtle.penup()
        my_turtle.forward(40)
        my_turtle.dot(15, random_color())

    if line % 2 == 0:
        even()
    else:
        odd()
    line += 1

my_screen = Screen()
my_screen.exitonclick()
