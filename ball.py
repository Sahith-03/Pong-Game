from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        self.y_dis = 10
        self.x_dis = 10
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        x = self.xcor() + self.x_dis
        y = self.ycor() + self.y_dis
        self.goto(x, y)

    def change_y_direction(self):
        self.y_dis *= -1

    def change_x_direction(self):
        self.x_dis *= -1

    def restart(self):
        self.goto(0, 0)
        self.x_dis *= -1
