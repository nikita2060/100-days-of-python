from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

    def display(self, score):
        self.write(arg=f"Score : {score} ", align=ALIGNMENT, font=FONT)
        # move parameter in this function moves the text to the right each time it is called.That's why I was not
        # getting expected results thus I removed it

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!!!!!", align=ALIGNMENT, font=FONT)
