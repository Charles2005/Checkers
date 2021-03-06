import pygame
from constants import  WHITE
from constants import SQUARE_SIZE
from constants import KING


class Piece:
    padding = 8
    outline = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        """
        Getting the position of the piece
        """
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def create_king(self):
        self.king = True

    def draw_piece(self, screen):
        """
        Drawing the the pieces, outline, and king
        """
        radius = SQUARE_SIZE // 2 - self.padding
        pygame.draw.circle(screen, WHITE, (self.x, self.y), radius + self.outline)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        # If there is a king draw the king
        if self.king:
            screen.blit(KING, (self.x - KING.get_width()//2, self.y - KING.get_height()//2))

    def piece_move(self, row, col):
        self.row = row
        self.col = col
        self.position()
