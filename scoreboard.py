import turtle

class Scoreboard(turtle.Turtle):
    """Manages the game's level and end game messages."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)  
        self.update_level()

    def update_level(self):
        """Update the displayed level."""
        self.clear()
        self.goto(0, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def increase_level(self, points=1):
        """Increase the level."""
        self.level += 1
        self.update_level()

    def display_message(self, message):
        """Display a given message in the center of the screen."""
        self.color("white") 
        self.goto(0, 25)  # Adjusted position to accommodate two lines
        self.write(message, align="center", font=("Courier", 36, "normal"))

    def game_over(self):
        """Display the game over message."""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 36, "normal"))


