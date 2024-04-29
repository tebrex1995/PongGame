from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

L_PADDLE = (-450, 0)
R_PADDLE = (450, 0)

screen = Screen()
r_paddle = Paddle(R_PADDLE)
l_paddle = Paddle(L_PADDLE)
ball = Ball()
scoreboard = Scoreboard()

screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Naru-Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with a wall
    if ball.ycor() == 400 or ball.ycor() == -400:
        #Ball bounces
        ball.bounce_y()
    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 400 or ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.bounce_x()
        ball.bounce_y()
    #R paddle misses
    if ball.xcor() > 460:
        ball.reset_position()
        scoreboard.l_score()
    #L paddle misses
    if ball.xcor() < -460:
        ball.reset_position()
        scoreboard.r_score()

screen.exitonclick()
