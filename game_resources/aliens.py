from turtle import Turtle

class Alien(Turtle):

    def __init__(self, alien_shape):
        super().__init__()
        self.penup()
        self.color("orange")
        self.shapesize(3, 3)
        self.right(90)
        self.shape(alien_shape)


def create_all_alien(alien_step: int, line_step: int, list_of_alien: list, all_aliens: list, alien_shape):
    for line in range(6):
        for _ in range(12):
            alien = Alien(alien_shape)
            alien.goto(-400 + alien_step, 50 + line_step)
            list_of_alien.append(alien)
            alien_step += 71
        alien_step = 5
        line_step += 60
        all_aliens.append(list_of_alien)
        list_of_alien = []



