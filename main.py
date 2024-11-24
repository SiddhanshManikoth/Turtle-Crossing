import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
level=Scoreboard()
timmy = Player(level)
cars = CarManager(level)

screen.onkeypress(timmy.move_Timmy_up,"w")
screen.onkeypress(timmy.move_Timmy_down,"s")
game_is_on = True
cars.genrate_Traffic()
while game_is_on:
    for c in cars.trafficList:
        if c.xcor()<-350:
            cars.trafficList.remove(c)
            cars.add_car()
    for c in cars.trafficList:
        if timmy.distance(c)<20:
            game_is_on=False
            level.game_over()
    cars.move_traffic()

    timmy.next_level()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
