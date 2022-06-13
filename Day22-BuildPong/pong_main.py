# breakdown the problem
# 1) Create the screen
# 2) create and move the paddle
# 3) create another paddle
# 4) Create the ball and make it move
# 5) Detect collision with wall and bounce
# 6) Detect collision with paddle
# 7) Detect when paddle misses
# 8) keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 1) create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # animation gets turned off then update the screen in while loop

# 3) Another paddle created
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 5) Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # 6) Detect collision with the paddle
    # check the distance of the paddle and ball and if less than 20 then collision occurs
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 or ball.ycor() < -320:
        ball.bounce_x()

    # 7) Detect when paddle misses
    # r_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # l_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

