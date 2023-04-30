import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.up)
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    #  if we began to create car at each loop then our screen will be full of cars so to prevent that we are creating a
    #  car previous car has already moved 6 loops so that cars won't be directly one after another
    if count == 6:
        car_manager.create_car()
        count = 0
    count += 1
    # to  detect collision we need to check that if the distance from center of any car on the screen is less than 20
    # pixel (that is half of length of car )then it means there is collision. Distance method measures distance  from
    # centre of object that's why half of length is considered here
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.show_game_over()

    # if player.ycor() > 280:
    # player.setposition(STARTING_POSITION)
    # I wrote this code  to restart after finishing, but we can create more optimised version by  dealing with change in
    # player in player package and speed of car in car_manager package only so make functions there and use here

    # leveling up
    if player.crossed_finish_line():
        player.goto_start_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
