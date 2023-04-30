from turtle import Turtle
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.setposition(x=-280, y=260)  # these values are set by experimenting on screen
        self.show_score()

    def increase_level(self):
        self.level += 1
        self.show_score()

    def show_score(self):
        self.clear()  # if not cleared then it will be overwritten above previous value
        self.write(arg=f"level:{self.level}", align="left", font=FONT)

    def show_game_over(self):
        self.setposition(0,0)
        self.write(arg="GAME OVER !!!!", align="center", font=FONT)
