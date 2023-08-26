import turtle
from settings import ALIEN_SHAPE, ALIEN_COLOR, ALIEN_SPEED

class Alien(turtle.Turtle):
    """Represents an alien ship."""

    def __init__(self):
        """Initialize the alien with default attributes."""
        super().__init__()
        self.speed(0)
        self.shape(ALIEN_SHAPE)
        self.color(ALIEN_COLOR)
        self.penup()
        self.speed_val = ALIEN_SPEED

    def move(self):
        """Move the alien horizontally."""
        self.setx(self.xcor() + self.speed_val)

    def change_direction(self):
        """Change the direction of the alien's movement and move it down a step."""
        self.speed_val *= -1
        self.sety(self.ycor() - 5)
