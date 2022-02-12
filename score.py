from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

    def reset_score(self):
        self.clear()
        self.goto(-240, 240)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 15, "normal"))
