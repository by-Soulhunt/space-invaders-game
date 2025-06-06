from turtle import Turtle

class Alien(Turtle):

    def __init__(self, alien_shape):
        super().__init__()
        self.penup()
        self.color("orange")
        self.shapesize(3, 3)
        self.right(90)
        self.shape(alien_shape)


def create_all_alien(alien_step: int, line_step: int, all_aliens: dict, alien_shape):
    for line in range(72):
        if line % 12 == 0:
            alien_step = 5
            line_step += 60
        alien = Alien(alien_shape)
        alien.goto(-400 + alien_step, 10 + line_step)
        all_aliens[line] = alien
        alien_step += 71



