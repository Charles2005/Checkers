import pygame
import sys
from constants import WIDTH, HEIGHT

# Screen Customization
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# Main function
def main():
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
    pygame.quit()


if __name__ == '__main__':
    main()
