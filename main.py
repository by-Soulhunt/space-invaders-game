from turtle import Screen
from game_resources.starship import Starship


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


        # Onkey function
        self.screen.listen()
        self.screen.onkeypress(self.starship.move_left, "Left")
        self.screen.onkeypress(self.starship.move_right, "Right")

        self.game_is_on = True

    def run(self):
        while self.game_is_on:
            self.screen.update()


if __name__ == "__main__":
    app = SpaceInvadersGame()
    app.run()