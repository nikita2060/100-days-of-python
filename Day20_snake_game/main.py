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
INITIAL_SLEEP_TIME = 0.3
MIN_SLEEP_TIME = 0.04
INCREASE_SPEED_RATE = 0.05

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # animation of screen is off because it was showing movement of each block due to which it looked like
# movement of caterpillar instead of snake haha
snake = Snake()
food = Food()
score = 0
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
scoreboard = Scoreboard()
scoreboard.display(score)
# displaying scoreboard
game_is_on = True
current_sleep_time = INITIAL_SLEEP_TIME

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(current_sleep_time)  # it helps to slow down the movement else snake will move too fast and won't be seen. I had
    # tried but the snake moved too fast

    # Detect collision with food
    if snake.snake[0].distance(food) < 15:
        snake.increase_snake_body()
        food.random_position()
        scoreboard.clear()
        score += 1
        if current_sleep_time > MIN_SLEEP_TIME:
            current_sleep_time -= INCREASE_SPEED_RATE
            INCREASE_SPEED_RATE = max(INCREASE_SPEED_RATE - 0.006, 0.01)
        scoreboard.display(score)

    # detect collision with wall
    if snake.snake[0].xcor() > RIGHT_BORDER - BUFFER_BORDER or snake.snake[0].xcor() < LEFT_BORDER - BUFFER_BORDER or \
            snake.snake[0].ycor() > UP_BORDER - BUFFER_BORDER or snake.snake[0].ycor() < DOWN_BORDER - BUFFER_BORDER:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.snake[1:]:
        distance = snake.snake[0].distance(segment)
        if distance < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
