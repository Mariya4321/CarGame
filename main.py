import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.title("Cross Road")
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.ycor() > 280:
        score.update()
        car.level_up()
        player.restart()

    for cars in car.new_car:
        if cars.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
