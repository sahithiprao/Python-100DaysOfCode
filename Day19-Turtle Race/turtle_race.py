from turtle import Turtle, Screen
import random

screen = Screen()

#set the screen window size for the race--understanding purposes use keyword args
screen.setup(width=500, height=400)
is_race_on = False
#text prompt to select the color
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will run the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    #set the position of the turtle- width is X axis and height y axis
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # 230 is the end point on the x- axis that determines ran endpoint
        if turtle.xcor() > 230:
            is_race_on = False
            winning_clr = turtle.pencolor()
            if winning_clr == user_bet:
                print(f"You've won! The {winning_clr} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_clr} turtle is the winner!")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)



screen.exitonclick()