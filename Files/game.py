import pygame
from constants import AI_COLOR, PLAYER_COLOR, RED
from constants import SQUARE_SIZE
from board import Board


class Game:
    def __init__(self, screen):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER_COLOR
        self.valid_move = {}
        self.screen = screen

    def update(self):
        self.board.draw_board(self.screen)
        self.draw_valid_moves(self.valid_move)
        pygame.display.update()

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER_COLOR
        self.valid_move = {}

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
                self.board.remove(skip)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        self.valid_move = {}
        if self.turn == PLAYER_COLOR:
            self.turn = AI_COLOR
        else:
            self.turn = PLAYER_COLOR

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, RED,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def winner(self):
        return self.board.get_winner()

