from turtle import Screen
from paddle import Paddle

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=500)
screen.title("Ping Pong")
screen.tracer(0)

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
    screen.update()

screen.exitonclick()
