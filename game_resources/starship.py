from turtle import Turtle

class Starship(Turtle):

    def __init__(self, starship_shape):
        super().__init__()
        self.color("green")
        self.left(90)
        self.penup()
        self.shape(starship_shape)
        self.shapesize(3, 3)
        self.goto(0, -400)



    def move_right(self):
        x = self.xcor()
        if x < 420:
            x += 15
            self.setx(x)


    def move_left(self):
        x = self.xcor()
        if x > -420:
            x += -15
            self.setx(x)