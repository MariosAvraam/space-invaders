# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Space Invaders"

# Player settings
PLAYER_SHAPE = "square"
PLAYER_COLOR = "blue"
PLAYER_START_Y = -250
PLAYER_BOUND_LEFT = -SCREEN_WIDTH // 2 + 20  # Adjust these values if needed
PLAYER_BOUND_RIGHT = SCREEN_WIDTH // 2 - 20

# Alien settings
ALIEN_SHAPE = "circle"
ALIEN_COLOR = "red"
ALIEN_START_Y = 250
ALIEN_SPEED = 0.2
NUMBER_OF_ALIENS = 5


# Bullet settings
BULLET_SHAPE = "triangle"
BULLET_COLOR = "yellow"
BULLET_SPEED = 0.7
