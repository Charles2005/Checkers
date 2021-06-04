import menu
import pygame
import sys
from board import Board
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from constants import ICON
from constants import PLAYER_COLOR
from game import Game

# Pygame Initialization
pygame.init()

# Screen Customization
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")
pygame.display.set_icon(ICON)


# Getting position of piece using mouse click
def get_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# Main function
def main():
    # Class objects
    board = Board()
    game = Game(sc)
    # Blitting Menu Choices in the screen
    menu_screen = menu.Menu()
    menu_screen.display_menu()
    # Variables needed in main
    play = True
    clock = pygame.time.Clock()

    # Game loop
    while play:
        clock.tick(60)
        # Printing the winner
        if game.winner() != None:
            print(game.winner())
            play = False
        # Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                play = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos(pos)
                game.select(row, col)

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
