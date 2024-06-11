from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.new_car = []
        self.speed = MOVE_INCREMENT

    def create_car(self):
        random_chances = random.randint(1, 6)
        if random_chances == 2:
            NewCar = Turtle("square")
            NewCar.penup()
            NewCar.shapesize(stretch_wid=1, stretch_len=2)
            NewCar.color(random.choice(COLORS))
            random_ps = random.randint(-250, 250)
            NewCar.goto(300, random_ps)
            self.new_car.append(NewCar)

    def move(self):
        for car in self.new_car:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
