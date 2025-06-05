from turtle import Screen
from game_resources.starship import Starship
from game_resources.aliens import create_all_alien
from game_resources.player_bullet import PlayerBullet
from game_resources.alien_bullet import AlienBullet
import random
import os


class SpaceInvadersGame:
    def __init__(self):

        # Game screen
        self.screen = Screen()
        self.screen.setup(width=900, height=900)
        self.screen.bgcolor("black")
        self.screen.title("Space Invaders Game")
        self.screen.tracer(0)

        # Images
        explosion_path = os.path.join("game_resources", "img", "explosion.gif")
        alien_starship_path = os.path.join("game_resources", "img", "alien_starship.gif")
        starship_path = os.path.join("game_resources", "img", "starship.gif")
        if os.path.exists(explosion_path) and os.path.exists(alien_starship_path):
            self.screen.register_shape(explosion_path)
            self.screen.register_shape(alien_starship_path)
            self.screen.register_shape(starship_path)
        else:
            print(f"Image not found.")

        # Starship
        self.starship = Starship("game_resources\\img\\starship.gif")

        # Bullets
        self.bullets = []
        self.alien_bullets = []
        self.alien_bullets_delay = 10
        self.alien_fighters_pull = [[0,0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8],
                                    [0, 9], [0, 10], [0, 11]]

        # Alien
        self.list_of_alien = []
        self.all_aliens = []
        self.alien_step = 5
        self.line_step = 0
        self.move_list = [-1, -1, -1, -1, 1, 1, 1, 1]
        self.move_index = 0

        # Create all aliens
        create_all_alien(alien_step=self.alien_step,
                         line_step=self.line_step,
                         list_of_alien=self.list_of_alien,
                         all_aliens=self.all_aliens,
                         alien_shape="game_resources\\img\\alien_starship.gif")


        # Onkey function
        self.screen.listen()
        self.screen.onkeypress(self.starship.move_left, "Left")
        self.screen.onkeypress(self.starship.move_right, "Right")
        self.screen.onkeypress(self.create_player_bullet, "space")


        # Flag
        self.game_is_on = True


    def create_player_bullet(self):
        """
        Create bullet and Add to list, for Onkey function
        :return: None
        """
        bullet = PlayerBullet(self.starship.xcor(), self.starship.ycor())
        self.bullets.append(bullet)


    def create_alien_bullet(self):
        """
        Create alien bullet at the random first row alien. Add to list.
        :return: None
        """
        number_of_aliens = self.count_all_aliens(self.all_aliens) # Count all aliens for define level of game
        if len(self.all_aliens) > 0:
            can_strike_aliens = []
            print(self.alien_fighters_pull) # TEST
            for alien in self.alien_fighters_pull:
                can_strike_aliens.append(self.all_aliens[alien[0]][alien[1]])
            print(self.alien_fighters_pull)  # TEST
            random_alien = random.choice(can_strike_aliens)
            alien_bullet = AlienBullet(random_alien.xcor(), random_alien.ycor())
            self.alien_bullets.append(alien_bullet)
        else: # TEST
            print("You WIN!") # TEST

        self.screen.ontimer(self.create_alien_bullet, self.alien_bullets_delay * number_of_aliens)


    def alien_bullet_strike(self):
        for alien_bullet in self.alien_bullets:
            alien_bullet.showturtle()
            alien_bullet.bullet_move()
            if alien_bullet.ycor() < -450:
                alien_bullet.hideturtle()
                self.alien_bullets.remove(alien_bullet)
        self.screen.ontimer(self.alien_bullet_strike, 30)


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
                    if bullet.distance(alien) < 20:
                        # Remove last index alien, avoid index out of range
                        self.alien_fighters_pull.pop()
                        if self.all_aliens.index(row) < 5:
                            # Add new alien from upper line into pull aliens that can strike
                            self.alien_fighters_pull.insert(0,[self.all_aliens.index(row) + 1, row.index(alien)])
                        self.bullets.remove(bullet)
                        alien.shape("game_resources\\img\\explosion.gif")
                        self.screen.update()
                        alien.hideturtle()
                        row.remove(alien)
                        bullet.hideturtle()
                if len(row) < 1:
                    self.all_aliens.remove(row) # Check empty rows without aliens and delete them
        self.screen.ontimer(self.alien_destroy, 1)


    def starship_destroy(self):
        for alien_bullet in self.alien_bullets:
            if alien_bullet.distance(self.starship) < 10:
                self.alien_bullets.remove(alien_bullet)
                self.starship.shape("game_resources\\img\\explosion.gif")
                self.screen.update()
                self.starship.hideturtle()
                alien_bullet.hideturtle()
                print("You LOSE") # TEST

        self.screen.ontimer(self.starship_destroy, 1)


    def count_all_aliens(self, lst: list):
        """
        Count all items in list including sublist
        :param lst: List of lists
        :return: int
        """
        count = 0
        for item in lst:
            if isinstance(item, list):
                count += self.count_all_aliens(item)  # recursively count the sublist
            else:
                count += 1
        return count


    def run(self):
        self.alien_move()
        self.alien_bullet_strike()
        self.player_bullet_strike()
        self.create_alien_bullet()
        self.alien_destroy()
        self.starship_destroy()
        self.screen.mainloop()


if __name__ == "__main__":
    app = SpaceInvadersGame()
    app.run()