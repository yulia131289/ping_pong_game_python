from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=500)
screen.title("Ping Pong")
screen.tracer(0)
scoreboard = Scoreboard()

# setup ball
ball = Ball()

# setup paddle
paddle_right = Paddle(330, 0)
paddle_left = Paddle(-330, 0)

screen.listen()

screen.onkey(paddle_right.up, "i")
screen.onkey(paddle_right.down, "k")

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.bounce_top_or_down()
        ball.move_speed *= 0.9

    # Detect collision with paddle
    if ball.distance(paddle_right) < 30 and ball.xcor() > 280 or ball.distance(paddle_left) < 30 and ball.xcor() < -280:
        ball.bounce_from_paddle()
        ball.move_speed *= 0.9

    # Detect right paddle misses
    if ball.xcor() > 340:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -340:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
