from turtle import Turtle, Screen
from random import *

screen = Screen()
screen.setup(width=1000, height=530)
user_turtle_color = screen.textinput(title="TURTLE GAME",
                                     prompt="Enter color of the turtle which you think will win")  # keyword
# arguments are easy to understand
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#  create multiple turtles
turtle_gap = 60
turtle_list = []
for color in range(6):
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color(colors[color])
    my_turtle.penup()
    my_turtle.goto(x=-450, y=230 - turtle_gap)
    turtle_gap += 60
    turtle_list.append(my_turtle)
is_race_on = False
if user_turtle_color:  # if user hasn't given input race should not start
    is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 470:  # still confused about the size of turtle as its not working according to its sizeof 40*40
            is_race_on = False
            if turtle.pencolor() == user_turtle_color:
                print(f"You won. The winner is {turtle.pencolor()}")
            else:
                print(f"You lost. The winner is {turtle.pencolor()}")
            break  # so that turtle stops and doesn't cross the screen

        random_distance = randint(1, 5)
        turtle.forward(random_distance)

screen.exitonclick()
