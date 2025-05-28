import time
from turtle import Screen
from game_resources.starship import Starship
from game_resources.aliens import Alien, create_all_alien
from game_resources.player_bullet import PlayerBullet
import os


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

        # Bullets
        self.bullets = []

        # Alien
        self.list_of_alien = []
        self.all_aliens = []
        self.alien_step = 5
        self.line_step = 0
        self.move_list = [-1, -1, -1, -1, 1, 1, 1, 1]
        self.move_index = 0

        # Explosion
        explosion_path = os.path.join("game_resources", "img", "explosion.gif")
        if os.path.exists(explosion_path):
            self.screen.register_shape(explosion_path)
        else:
            print(f"File not found: {explosion_path}")

        print(self.screen.getshapes())

        create_all_alien(alien_step=self.alien_step,
                         line_step=self.line_step,
                         list_of_alien=self.list_of_alien,
                         all_aliens=self.all_aliens)


        # Onkey function
        self.screen.listen()
        self.screen.onkeypress(self.starship.move_left, "Left")
        self.screen.onkeypress(self.starship.move_right, "Right")
        self.screen.onkeypress(self.create_player_bullet, "space")

        # Flag
        self.game_is_on = True


    def create_player_bullet(self):
        bullet = PlayerBullet(self.starship.xcor(), self.starship.ycor())
        self.bullets.append(bullet)

    def player_bullet_strike(self):
        for bullet in self.bullets:
            bullet.showturtle()
            bullet.bullet_move()
            if bullet.ycor() > 450:
                bullet.hideturtle()
                self.bullets.remove(bullet)
        self.screen.ontimer(self.player_bullet_strike, 30)


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


    def alien_destroy(self):
        for bullet in self.bullets:
            for row in self.all_aliens:
                for alien in row:
                    if bullet.distance(alien) < 10:
                        self.bullets.remove(bullet)
                        alien.shape("game_resources\\img\\explosion.gif")
                        self.screen.update()
                        alien.hideturtle()
                        row.remove(alien)
                        bullet.hideturtle()


        self.screen.ontimer(self.alien_destroy, 1)

    def run(self):
        self.alien_move()
        self.player_bullet_strike()
        self.alien_destroy()
        self.screen.mainloop()


if __name__ == "__main__":
    app = SpaceInvadersGame()
    app.run()