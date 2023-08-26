import turtle
from settings import BULLET_SHAPE, BULLET_COLOR, BULLET_SPEED

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape(BULLET_SHAPE)
        self.color(BULLET_COLOR)
        self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.penup()
        self.hideturtle()
        self.speed_val = BULLET_SPEED
        self.state = "ready"

    def fire(self, x, y):
        """Fire the bullet from a specific position.

        Args:
        - x: x-coordinate from which the bullet is fired.
        - y: y-coordinate from which the bullet is fired.
        """
        if self.state == "ready":
            self.state = "fire"
            self.goto(x, y + 15)  # Adjusting y to start a bit above the player
            self.showturtle()

    def move(self):
        """Move the bullet upwards."""
        if self.state == "fire":
            y = self.ycor()
            y += self.speed_val
            self.sety(y)

        # Check if bullet goes out of the screen
        if self.ycor() > 275:
            self.hideturtle()
            self.state = "ready"
