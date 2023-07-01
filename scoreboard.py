from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.shape("blank")
        self.penup()
        self.color("white")
        self.goto(-120, 200)
        self.write(self.l_score, font=("Arial", 50, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, font=("Arial", 50, "normal"))

    def inc1(self):
        self.l_score += 1
        self.display()

    def inc2(self):
        self.r_score += 1
        self.display()

    def display(self):
        self.clear()
        self.goto(-120, 200)
        self.write(self.l_score, font=("Arial", 50, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, font=("Arial", 50, "normal"))

    def exit(self):
        self.goto(0, 0)
        if self.l_score == 11:
            self.write("Player 1 Won", align="center", font=("Arial", 50, "normal"))
        if self.r_score == 11:
            self.write("Player 2 Won", align="center", font=("Arial", 50, "normal"))
