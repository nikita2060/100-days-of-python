from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
RIGHT_BORDER = SCREEN_WIDTH / 2
LEFT_BORDER = -RIGHT_BORDER
UP_BORDER = SCREEN_HEIGHT / 2
DOWN_BORDER = -UP_BORDER
BUFFER_BORDER = 10
SLEEP_TIME = 0.1  # Kept this value after experimenting on screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # animation of screen is off because it was showing movement of each block due to which it looked like
# movement of caterpillar instead of snake haha
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
scoreboard = Scoreboard()
# displaying scoreboard
game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(SLEEP_TIME)  # it helps to slow down the movement else snake will move too fast and won't be
    # seen. I had tried but the snake moved too fast

    # Detect collision with food
    if snake.snake[0].distance(food) < 15:
        snake.increase_snake_body()
        food.random_position()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.snake[0].xcor() > RIGHT_BORDER - BUFFER_BORDER or snake.snake[0].xcor() < LEFT_BORDER - BUFFER_BORDER or \
            snake.snake[0].ycor() > UP_BORDER - BUFFER_BORDER or snake.snake[0].ycor() < DOWN_BORDER - BUFFER_BORDER:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.snake[1:]:
        distance = snake.snake[0].distance(segment)
        if distance < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
