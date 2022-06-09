from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    new_h = tim.heading() + 10
    tim.setheading(new_h)

def clockwise():
    new_h = tim.heading() - 10
    tim.setheading(new_h)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
#bind a keystroke to listener
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "space")

screen.exitonclick()