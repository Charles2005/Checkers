import pygame
import sys
from constants import MENU_BG, CHOICE_COLOR, TITLE_COLOR, CLICKED_COLOR
from constants import WIDTH, HEIGHT


class Menu:
    def __init__(self):
        self.title_font = pygame.font.Font("C:/WINDOWS/FONTS/CASCADIAMONOPL.ttf", 64)
        self.choice_font = pygame.font.Font("C:/WINDOWS/FONTS/CASCADIAMONOPL.ttf", 48)
        self.clicked = False
        self.bg_color = MENU_BG
        self.title_color = TITLE_COLOR
        self.choice_color = CHOICE_COLOR
        self.choice_clicked_color = CLICKED_COLOR

    def display_menu(self):
        from main import sc
        menu = True
        while menu:
            # Putting background
            sc.fill(MENU_BG)

            # Rendering the Fonts
            title = self.title_font.render("Checkers", True, TITLE_COLOR)
            start = self.choice_font.render("Start", True, CHOICE_COLOR)
            match_history = self.choice_font.render("Match History", True, CHOICE_COLOR)
            quit = self.choice_font.render("Quit", True, CHOICE_COLOR)

            # Blitting the text to the screen
            sc.blit(title, (WIDTH // 4, HEIGHT // 10))

            # Handling Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    menu = False
                    pygame.quit()
                    sys.exit()
            # Updating the Screen
            pygame.display.update()
