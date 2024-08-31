import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# create a player
player = Player()

#control the player
screen.listen() # type: ignore
screen.onkeypress(player.move,'up') # type: ignore

#initialising car manager
car_manager = CarManager()

#create scoreboard
scoreboard = Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move the car 
    car_manager.make_car()
    car_manager.move()

    #detect collision with car 
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over() # type: ignore
            game_is_on = False

    #detect successful crossing and speed up cars
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        score.update_scoreboard() # type: ignore

screen.exitonclick()
