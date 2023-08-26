# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Space Invaders"

# Player settings
PLAYER_SHAPE = "square"
PLAYER_COLOR = "blue"
PLAYER_START_Y = -250
PLAYER_BOUND_LEFT = -SCREEN_WIDTH // 2 + 20
PLAYER_BOUND_RIGHT = SCREEN_WIDTH // 2 - 20

# Alien settings
ALIEN_SHAPE = "circle"
ALIEN_COLOR = "red"
ALIEN_START_Y = 250
ALIEN_SPEED = 4
ALIEN_SPEED_INCREASE_FACTOR = 1.02 # Increase speed by 2% each level
NUMBER_OF_ALIENS = 5
ALIEN_COUNT_INCREASE = 2  # Increase by 2 aliens every level

# Bullet settings
BULLET_SHAPE = "triangle"
BULLET_COLOR = "yellow"
BULLET_SPEED = 8
