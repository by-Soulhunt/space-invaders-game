from turtle import Turtle

class Alien(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(3, 3)
        self.right(90)


def create_all_alien(alien_step: int, line_step: int, list_of_alien: list, all_aliens: list):
    for line in range(6):
        for _ in range(12):
            alien = Alien()
            alien.goto(-400 + alien_step, 100 + line_step)
            list_of_alien.append(alien)
            alien_step += 71
        alien_step = 5
        line_step += 50
        all_aliens.append(list_of_alien)



