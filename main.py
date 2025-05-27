from turtle import Screen
from game_resources.starship import Starship
from game_resources.aliens import Alien, create_all_alien


class SpaceInvadersGame:
    def __init__(self):

        # Game screen
        self.screen = Screen()
        self.screen.setup(width=900, height=900)
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders Game")
        self.screen.tracer(0)

        # Starship
        self.starship = Starship()

        # Alien
        self.list_of_alien = []
        self.all_aliens = []
        self.alien_step = 5
        self.line_step = 0
        self.move_list = [-1, -1, -1, -1, 1, 1, 1, 1]
        self.move_index = 0

        create_all_alien(alien_step=self.alien_step,
                         line_step=self.line_step,
                         list_of_alien=self.list_of_alien,
                         all_aliens=self.all_aliens)


        # Onkey function
        self.screen.listen()
        self.screen.onkeypress(self.starship.move_left, "Left")
        self.screen.onkeypress(self.starship.move_right, "Right")

        self.game_is_on = True

    def alien_move(self):
        dx = self.move_list[self.move_index]
        for rows in self.all_aliens:
            for alien in rows:
                alien.setx(alien.xcor() + dx)

        self.move_index += 1
        if self.move_index >= len(self.move_list):
            self.move_index = 0
            self.move_list.reverse()

        self.screen.update()
        self.screen.ontimer(self.alien_move, 60)

    def run(self):
        self.alien_move()
        self.screen.mainloop()


if __name__ == "__main__":
    app = SpaceInvadersGame()
    app.run()