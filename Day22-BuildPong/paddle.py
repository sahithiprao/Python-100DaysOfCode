from turtle import Turtle


class Paddle(Turtle):
    # 2) create a paddle and move it.
    # paddle width= 20, height = 100, x_pos = 350, y_pos = 0

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # 20 x 5 = 100
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)