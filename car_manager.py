from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Carmanager:
    def __init__(self):
        self.all_cars = []
        self.speed=5

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(300, (random.randint(-150, 150)))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.speed)

    def speed_up(self):
        self.speed +=3
