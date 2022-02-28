from turtle import Turtle

STEP = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + STEP)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - STEP)
