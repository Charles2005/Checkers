import pygame
from constants import PLAYER_COLOR, AI_COLOR, WHITE
from constants import SQUARE_SIZE


class Piece:
    padding = 8
    outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == PLAYER_COLOR:
            self.direction = - 1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        """
        Getting the position of the piece
        """
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def king(self):
        self.king = True

    def draw_piece(self, screen):
        """
        Drawing the piece and calculating the size of it
        """
        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(screen, WHITE, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)

    def __repr__(self):
        return str(self.color)
