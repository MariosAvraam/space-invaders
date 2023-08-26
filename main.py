import turtle
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BG_COLOR, SCREEN_TITLE, 
    NUMBER_OF_ALIENS
)
from player import Player
from alien import Alien
from bullet import Bullet

# Setting up the screen
screen = turtle.Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.title(SCREEN_TITLE)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)  # Turn off screen updates for smoother animations

# Initialize the player spaceship
player = Player()

# Initialize the alien ships
aliens = []
for i in range(NUMBER_OF_ALIENS):
    alien = Alien()
    x = -200 + (i * 50)
    y = 250
    alien.goto(x, y)
    aliens.append(alien)

# Initialize the player's bullet
bullet = Bullet()

# Function to move the player left
def move_left():
    player.move_left()

# Function to move the player right
def move_right():
    player.move_right()

# Function to fire the player's bullet
def fire_bullet():
    x = player.xcor()
    y = player.ycor()
    bullet.fire(x, y)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    screen.update()

    # Move the bullet
    bullet.move()

    # Move the aliens
    for alien in aliens:
        alien.move()

        # Change alien direction if hit the edge
        if alien.xcor() > 230 or alien.xcor() < -230:
            for a in aliens:
                a.change_direction()
            break

screen.mainloop()
