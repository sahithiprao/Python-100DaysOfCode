# breakdown the problem
# 1) Snake body
# 2) move the snake
# 3) control snake by using keys
# 4) Detect collision with food
# 5) Create a scoreboard
# 6) Detect collision with wall - game over
# 7) Detect collision with tail - game over

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# create a screen with black bg
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # tracer-animation off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# bind a keystroke to listener
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # need to use this update function after using tracer
    time.sleep(0.1)
    # move the snake
    snake.move()
    # 4) detect collision with food
    if snake.head.distance(food) < 15:
        # turtle has distance function that can be compared with another instance of turtle
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 6) Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # 7) Detect collision with tail
    # if the head collides with any segment in the tail, then game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

