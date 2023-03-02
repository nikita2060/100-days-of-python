from turtle import Turtle

MOVE_POSITION = 20  # we write constants in capital letter
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake_body()
        self.last_position = ()

    def create_snake_body(self):

        #  creating snake body
        for i in range(0, -2, -1):  # previously I arranged them at x=0,20,40 but since we need to move forward in
            # positive direction for implementing input directions so x=0,-20,-40 in this way head moves first in
            # positive direction . I also tried moving backwards but input was being implemented in opposite direction.
            block = Turtle("square")
            block.color("white")
            block.penup()
            block.setposition(x=i * 20, y=0)
            self.snake.append(block)

    def increase_snake_body(self):
        # self.tail += 1
        block = Turtle("square")
        block.color("white")
        block.penup()
        self.last_position = self.snake[-1].position()
        block.goto(self.last_position)
        self.snake.append(block)

    def move(self):
        for block in range(len(self.snake) - 1, 0,-1):  # it will run loop for block in last index and second last index
            # i.e.block =2 then 1
            new_x_cor = self.snake[block - 1].xcor()
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
