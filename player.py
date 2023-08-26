import turtle
from settings import PLAYER_SHAPE, PLAYER_COLOR, PLAYER_START_Y, PLAYER_BOUND_LEFT, PLAYER_BOUND_RIGHT

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(0, PLAYER_START_Y)

    def move_left(self):
        x = self.xcor()
        if x > PLAYER_BOUND_LEFT:
            x -= 20
            self.setx(x)

    def move_right(self):
        x = self.xcor()
        if x < PLAYER_BOUND_RIGHT:
            x += 20
            self.setx(x)
