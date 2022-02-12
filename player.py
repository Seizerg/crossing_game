from turtle import Turtle

INIT_POS = (0, -200)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(INIT_POS)
        self.setheading(90)

    def turtle_move(self):
        self.fd(10)

    def reset_position(self):
        self.goto(INIT_POS)
