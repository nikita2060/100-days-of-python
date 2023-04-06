import time
from random import randint
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
INITIAL_TIME_SPEED = 0.05
MOVING_ANGLE_RIGHT = randint(40, 60)
MOVING_ANGLE_LEFT = randint(120, 140)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

screen.update()

game_is_on = True
while game_is_on:
    time.sleep(INITIAL_TIME_SPEED)
    ball.move_ball()
    ball.detect_collision_with_wall()

    # detect collision with right paddle
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.setheading(220)
        ball.move_ball()

    # detect collision with left paddle
    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:  # Taken 50 since ball will always come from either
        # upside or downside
        ball.setheading(45)
        ball.move_ball()

    # detect if ball has crossed the border

    if ball.xcor() < -390:  # left side
        ball.penup()
        ball.setheading(MOVING_ANGLE_RIGHT)
        ball.move_ball()
        ball.setposition(0, 0)
        scoreboard.update_right_score()
        INITIAL_TIME_SPEED *= 1.01
    if ball.xcor() > 390:  # right side
        ball.penup()
        ball.setposition(0, 0)
        ball.setheading(MOVING_ANGLE_LEFT)
        ball.move_ball()
        scoreboard.update_left_score()
        INITIAL_TIME_SPEED *= 0.001


    screen.update()

screen.exitonclick()
