import menu
import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from constants import ICON
from game import Game
from constants import AI_COLOR
from ai import minimax_algorithm

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
        # Winner
        if game.winner() != None:
            menu_screen.display_menu()
            main()
        # If AI turn
        if game.turn == AI_COLOR:
            value, new_board = minimax_algorithm(game.get_board(), 3, AI_COLOR, game)
            game.ai_turn(new_board)

        # Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                menu_screen.display_menu()
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos(pos)
                game.select(row, col)

        game.update()
    pygame.quit()


if __name__ == '__main__':
    main()
