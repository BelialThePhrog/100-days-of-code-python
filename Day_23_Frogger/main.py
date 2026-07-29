import turtle as tur
import time
import random as r
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = tur.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Cross Roads")
screen.tracer(0)
screen.colormode(255)

player_turtle = Player()
scoreboard = Scoreboard()
cars = []

time_to_spawn = 0
car_speed = 10
reflexes = 0.1

screen.listen()
screen.onkeypress(player_turtle.up, "Up")
screen.onkeypress(player_turtle.down, "Down")
screen.onkeypress(player_turtle.right, "Right")
screen.onkeypress(player_turtle.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(reflexes)
    time_to_spawn += 1
    
    # Spawn cars
    if time_to_spawn % 5 == 0:
        new_car = CarManager(car_speed)
        cars.append(new_car)
        
    # Move cars
    for car in cars:
        car.move()
        
    # Detect successful crossing
    if player_turtle.player_turtle.ycor() > 280:
        scoreboard.increase_score_player()
        player_turtle.reset_position()
        reflexes /= 1.2
        
    # Detect collision with a car
    for car in cars:
        if player_turtle.player_turtle.distance(car.car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()
