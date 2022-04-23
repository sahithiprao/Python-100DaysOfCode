from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
def turtle_square():
    for _ in range(4):
        timmy_turtle.right(90)
        timmy_turtle.forward(100)

def dashed_turtle():
    for _ in range(15):
        timmy_turtle.forward(10)
        timmy_turtle.penup()
        timmy_turtle.forward(10)
        timmy_turtle.pendown()

colors = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue","wheat","SeaGreen","IndianRed"]
def diff_shapes(side):
    for i in side:
        angle = 360 / i
        timmy_turtle.color(random.choice(colors))
        for _ in range(i):
            timmy_turtle.forward(100)
            timmy_turtle.right(angle)

colors = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue","wheat","SeaGreen","IndianRed"]
directions = [0, 90, 180, 270]
# timmy_turtle.pensize(15)
timmy_turtle.speed("fastest")
def random_walk():
    for _ in range(200):
        # timmy_turtle.color(random.choice(colors))
        timmy_turtle.color(random_color())
        timmy_turtle.forward(30)
        timmy_turtle.left(random.choice(directions))

#r,g,b colors---tuple---colormode - 0 to 255
import turtle as t
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_color = (r, g, b)
    return ran_color

def spirograph(size_of_gap):
    timmy_turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        timmy_turtle.color(random_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)



spirograph(5)
# random_walk()
#diff_shapes([3,4,5,6,7,8,9,10])
# turtle_square()
#dashed_turtle()



screen = Screen()
screen.exitonclick()