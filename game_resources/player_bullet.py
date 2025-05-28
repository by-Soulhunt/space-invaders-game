from turtle import Turtle


class PlayerBullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.hideturtle()
        self.goto(x, y)
        self.setheading(90)


    def bullet_move(self):
        self.forward(10)