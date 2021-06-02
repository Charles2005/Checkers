import pygame

# SCREEN CONSTANT
WIDTH, HEIGHT = (680, 680)
ROWS, COLS = (8, 8)
SQUARE_SIZE = WIDTH // COLS

# IMAGES AND ICONS
ICON = pygame.image.load("../Assets/checkers_icon.png")
# COLORS
WHITE = (255, 255, 255)
BOARD_WHITE = pygame.Color("#E6E6E6")
BOARD_BLACK = pygame.Color("#39393A")
MENU_BG = pygame.Color("#85FFC7")
TITLE_COLOR = pygame.Color("#297373")
CHOICE_COLOR = pygame.Color("#297373")
CLICKED_COLOR = pygame.Color("#FF8552")
PLAYER_COLOR = pygame.Color("#FF8552")
AI_COLOR = pygame.Color("#297373")
