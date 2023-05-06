from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score} ", align=ALIGNMENT, font=FONT)
        # move parameter in this function moves the text to the right each time it is called.That's why I was not
        # getting expected results thus I removed it

    def increase_score(self):
        self.score += 1
        self.display_scoreboard()

    def reset_scoreboard(self):
        if self.high_score < self.score:
            with open("data.txt", "w") as file:
                data = str(self.score)  # We can also write score in string form using fstrings write(f"{self.score}")
                file.write(data)
        self.high_score = self.get_high_score()
        self.score = 0
        self.display_scoreboard()

    def get_high_score(self):
        with open("data.txt") as file:
            data = int(file.read())
            return data