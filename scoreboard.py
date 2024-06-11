from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write(f"Level = {self.level}", font=FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}", font=FONT)

    def game_over(self):
        self.goto(-20, 20)
        self.write("Game Over", font=FONT)

