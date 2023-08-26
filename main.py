import turtle
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BG_COLOR, SCREEN_TITLE, 
    NUMBER_OF_ALIENS, ALIEN_COUNT_INCREASE, ALIEN_SPEED, ALIEN_SPEED_INCREASE_FACTOR, MAX_ALIENS_PER_ROW
)
from player import Player
from alien import Alien
from bullet import Bullet
from scoreboard import Scoreboard
import time

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

# Initialize the scoreboard
scoreboard = Scoreboard()

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
    time.sleep(0.02)

    # Move the bullet
    bullet.move()

    # Flag to track if any alien hits the boundary
    change_direction_flag = False

    # Move the aliens
    for alien in aliens:
        alien.move()
        # Check if an alien hits the boundary
        if alien.xcor() > 230 or alien.xcor() < -230:
            change_direction_flag = True

        # Check if the bullet has collided with the alien
        if bullet.is_collision(alien):
            # Reset the bullet
            bullet.hideturtle()
            bullet.state = "ready"
            bullet.goto(-1000, 1000)  # Move bullet out of the screen

            # Remove the alien
            alien.hideturtle()
            aliens.remove(alien)

            break  # Exit the loop to prevent iterating over a modified list

    # Check if all aliens are removed
    if not aliens:
        scoreboard.increase_level()
        scoreboard.display_message(f"Congratulations!\nNow on Level {scoreboard.level}")
        time.sleep(3)  # Display the message for 3 seconds
        scoreboard.clear()

        # Increase difficulty
        NUMBER_OF_ALIENS += ALIEN_COUNT_INCREASE
        ALIEN_SPEED *= ALIEN_SPEED_INCREASE_FACTOR

        # Repopulate the aliens for the next level
        aliens = []

        # Calculate rows and columns
        num_rows = NUMBER_OF_ALIENS // MAX_ALIENS_PER_ROW
        if NUMBER_OF_ALIENS % MAX_ALIENS_PER_ROW > 0:
            num_rows += 1

        num_columns = min(NUMBER_OF_ALIENS, MAX_ALIENS_PER_ROW)

        for row in range(num_rows):
            for col in range(num_columns):
                alien = Alien()
                alien.speed_val = ALIEN_SPEED
                x = -200 + (col * 50)
                y = 250 - (row * 50)
                alien.goto(x, y)
                aliens.append(alien)
                if len(aliens) >= NUMBER_OF_ALIENS:
                    break


    # Change direction for all aliens if any of them hit the boundary
    if change_direction_flag:
        for alien in aliens:
            alien.change_direction()

