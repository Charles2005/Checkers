import pygame
import sys
from constants import MENU_BG, CHOICE_COLOR, TITLE_COLOR, CLICKED_COLOR
from constants import WIDTH, HEIGHT
from main import sc


class Menu:
    def __init__(self):
        self.title_font = pygame.font.Font("C:/WINDOWS/FONTS/CASCADIAMONOPL.ttf", 64)
        self.choice_font = pygame.font.Font("C:/WINDOWS/FONTS/CASCADIAMONOPL.ttf", 48)
        self.bg_color = MENU_BG
        self.title_color = TITLE_COLOR
        self.choice_color = CHOICE_COLOR
        self.choice_clicked_color = CLICKED_COLOR

    def display_menu(self):
        point = 0
        mouse_pos = pygame.mouse.get_pos()
        while 1:
            # Putting background
            sc.fill(MENU_BG)
            # Rendering the Fonts
            title = self.title_font.render("Checkers", True, TITLE_COLOR)
            # If choice is in start
            if point == 0:
                # Rendering the Fonts
                start = self.choice_font.render("Start", True, CLICKED_COLOR)
                # Quit Text
                quit = self.choice_font.render("Quit", True, CHOICE_COLOR)
            # If choice is in match history
            elif point == 1:
                # Rendering the Fonts
                start = self.choice_font.render("Start", True, CHOICE_COLOR)
                quit = self.choice_font.render("Quit", True, CLICKED_COLOR)

            # Blitting the text to the screen
            sc.blit(title, (WIDTH // 4, HEIGHT // 10))
            sc.blit(start, (WIDTH//6.5, HEIGHT//2))
            sc.blit(quit, (WIDTH// 1.7, HEIGHT // 2))

            # Handling Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    menu = False
                    pygame.quit()
                    sys.exit()
                # Keyboard press down
                if event.type == pygame.KEYDOWN:
                    # down arrow pressed
                    if event.key == pygame.K_RIGHT:
                        point += 1
                        if point > 1:
                            point = 1
                    # Up arrow pressed
                    elif event.key == pygame.K_LEFT:
                        point -= 1
                        if point < 0:
                            point = 0
                    # Enter pressed
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if point == 0:
                            return True
                        elif point == 1:
                            pygame.quit()
                            sys.exit()
            # Updating the Screen
            pygame.display.update()
