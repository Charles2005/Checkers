import pygame
from constants import AI_COLOR, PLAYER_COLOR, RED
from constants import SQUARE_SIZE
from board import Board


class Game:
    def __init__(self, screen):
        self.board = Board()
        self.valid_move = {}
        self.turn = PLAYER_COLOR
        self.selected = None
        self.screen = screen

    def winner(self):
        return self.board.get_winner()

    def get_board(self):
        return self.board

    def update(self):
        self.board.whole_board(self.screen)
        self.draw_valid_moves(self.valid_move)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            piece_move = self.move(row, col)
            if not piece_move:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_move = self.board.get_valid_moves(piece)
            return True
        return False

    def move(self, row, col):
        """
        Moving the the selected piece
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_move:
            self.board.movement(self.selected, row, col)
            skip = self.valid_move[(row, col)]
            if skip:
                self.board.eaten(skip)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, RED,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_move = {}
        if self.turn == PLAYER_COLOR:
            self.turn = AI_COLOR
        else:
            self.turn = PLAYER_COLOR

    def ai_turn(self, board):
        self.board = board
        self.change_turn()


