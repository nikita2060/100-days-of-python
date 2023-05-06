from turtle import Turtle

MOVE_POSITION = 20  # we write constants in capital letter
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []  # in python, we can create list of objects and this list is list of turtle objects
        self.create_snake_body()
        self.last_position = ()

    def create_snake_body(self):
        for position in STARTING_POSITIONS:
            block = Turtle("square")
            block.color("white")
            block.penup()
            block.setposition(position)
            self.snake.append(block)

    def reset_snake(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake_body()

    def increase_snake_body(self):
        block = Turtle("square")
        block.color("white")
        block.penup()
        self.last_position = self.snake[-1].position()  # returns position as tuple(x,y)
        block.goto(self.last_position)
        self.snake.append(block)

    def move(self):

        for block in range(len(self.snake) - 1, 0, -1):  # it will run loop for block in last index and second lastindex
            # i.e.block =2 then 1
            new_x_cor = self.snake[block - 1].xcor()  # it gives x coordinate of previous block i.e if present index is
            # 1 then snake[1-1] i.e snake[0].xcor
            new_y_cor = self.snake[block - 1].ycor()
            self.snake[block].goto(new_x_cor, new_y_cor)

        self.snake[0].forward(MOVE_POSITION)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
