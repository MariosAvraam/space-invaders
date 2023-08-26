import turtle
from settings import PLAYER_SHAPE, PLAYER_COLOR, PLAYER_START_Y, PLAYER_BOUND_LEFT, PLAYER_BOUND_RIGHT

class Player(turtle.Turtle):
    """Represents the player's spaceship."""

    def __init__(self):
        """Initialize the player with default attributes."""
        super().__init__()
        self.speed(0)
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(0, PLAYER_START_Y)

    def move_left(self):
        """Move the player to the left."""
        x = self.xcor()
        if x > PLAYER_BOUND_LEFT: # Check if player is within the left boundary
            x -= 20
            self.setx(x)

    def move_right(self):
        """Move the player to the right."""
        x = self.xcor()
        if x < PLAYER_BOUND_RIGHT:  # Check if player is within the right boundary
            x += 20
            self.setx(x)
