from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT = (350, 0)
LEFT = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()

    # Detecting collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
        ball.x_bounce()

    # Detecting r_paddle miss
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()

    # Detecting l_paddle miss
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
