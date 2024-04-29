from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 300)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 300)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_score(self):
        self.l_score += 1

    def r_score(self):
        self.r_score += 1
