import menu
import pygame
import sys
from constants import WIDTH, HEIGHT
from constants import ICON

# Pygame Initialization
pygame.init()

# Screen Customization
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
pygame.display.set_icon(ICON)

# Main function
def main():
    # Blitting Menu Choices in the screen
    menu_screen = menu.Menu()
    menu_screen.display_menu()
    # Variables needed in main
    play = True
    clock = pygame.time.Clock()
    # Game loop
    while play:
        clock.tick(60)
        # Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                play = False
                sys.exit()

        # Updating the screen
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
