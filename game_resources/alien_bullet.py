from turtle import Turtle


class AlienBullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=0.3, stretch_len=1)
        #self.hideturtle()
        self.goto(x, y)
        self.setheading(270)


    def bullet_move(self):
        self.forward(10)


