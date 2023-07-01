from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

score = Scoreboard()

l_bar = Paddle((-350, 0))
r_bar = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_bar.go_up, "Up")
screen.onkey(r_bar.go_down, "Down")
screen.onkey(l_bar.go_up, "w")
screen.onkey(l_bar.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    # Collision with wall
    if abs(ball.ycor()) >= 288:
        ball.change_y_direction()
    # Collision with paddle
    if abs(ball.xcor()) == 330 and (ball.distance(l_bar) < 70 or ball.distance(r_bar) < 70):
        ball.change_x_direction()
    # Out of Boundary
    if ball.xcor() > 410:
        score.inc1()
        ball.restart()
    if ball.xcor() < -410:
        score.inc2()
        ball.restart()
    if score.l_score == 11 or score.r_score == 11:
        score.exit()
        game_is_on = False

screen.exitonclick()
