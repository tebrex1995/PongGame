from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

L_PADDLE = (-450, 0)
R_PADDLE = (450, 0)


screen = Screen()
r_paddle = Paddle(R_PADDLE)
l_paddle = Paddle(L_PADDLE)
ball = Ball()

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
    #Detect if the ball passed the paddle
    elif ball.xcor() > 460 or ball.xcor() < -460:
        r_paddle.setpos(R_PADDLE)
        l_paddle.setpos(L_PADDLE)
        ball.setpos(0,0)

screen.exitonclick()
