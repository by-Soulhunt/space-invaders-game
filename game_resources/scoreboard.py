from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-120, 410)
        self.color("white")
        self.current_score = 0




    def write_score(self):
        self.clear()
        self.write(f"Your score is: {self.current_score}", font=("Colibri", 20, "normal"))

    def you_win(self):
        self.goto(-120, 0)
        self.color("green")
        self.write(f"You WIN!", font=("Colibri", 20, "normal"))

    def you_lose(self):
        self.goto(-120, 0)
        self.color("red")
        self.write(f"You LOSE!", font=("Colibri", 20, "normal"))