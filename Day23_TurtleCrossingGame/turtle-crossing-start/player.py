from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the
    # turtle north.
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_start_position()

    #  creating a function to move turtle up
    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def crossed_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start_position(self):
        self.setposition(STARTING_POSITION)



