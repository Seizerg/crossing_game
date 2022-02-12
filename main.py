from turtle import Screen
import time
from player import Player
from score import Score
from car_manager import Carmanager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
score = Score()
car = Carmanager()
score.reset_score()
screen.onkey(fun=player.turtle_move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # Detect the turtle reaches the other side of the screen
    if player.ycor() > 190:
        player.reset_position()
        score.level_up()
        score.reset_score()
        car.speed_up()
    # Detect the collision between cars and turtle
    for i in car.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
