import turtle
from settings import ALIEN_SHAPE, ALIEN_COLOR, ALIEN_SPEED

class Alien(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape(ALIEN_SHAPE)
        self.color(ALIEN_COLOR)
        self.penup()
        self.speed_val = ALIEN_SPEED

    def move(self):
        self.setx(self.xcor() + self.speed_val)

    def change_direction(self):
        self.speed_val *= -1
        self.sety(self.ycor() - 40)
