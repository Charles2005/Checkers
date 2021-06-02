import pygame
from constants import BOARD_BLACK, BOARD_WHITE, AI_COLOR, PLAYER_COLOR
from constants import ROWS, COLS, SQUARE_SIZE
from piece import Piece


class Board:
    def __init__(self):
        self.board = [[]]
        self.selected_piece = None
        self.orange_left = self.green_left = 12
        self.orange_kings = self.green_kings = 0
        self.create_board()

    def board_squares(self, screen):
        """
        Draw the WHITE SQUARES OF THE BOARD
        """
        screen.fill(BOARD_BLACK) # FIll the board with black first
        # Loop to
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, BOARD_WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        Creating the whole board with pieces
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, AI_COLOR))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, PLAYER_COLOR))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_board(self, screen ):
        """
        Draw the whole board
        """
        self.board_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(screen)







