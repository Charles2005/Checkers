import pygame
from constants import BOARD_BLACK, BOARD_WHITE, AI_COLOR, PLAYER_COLOR
from constants import ROWS, COLS, SQUARE_SIZE
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.orange_left = self.green_left = 12
        self.orange_kings = self.green_kings = 0
        self.create_board()

    def board_squares(self, screen):
        """
        Draw the WHITE SQUARES OF THE BOARD
        """
        screen.fill(BOARD_BLACK)  # Fill the board with black first
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

    def draw_board(self, screen):
        """
        Draw the whole board
        """
        self.board_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(screen)

    def movement(self, piece, row, col):
        """
        Tracking the movement of the piece
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.piece_move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.create_king()
            if piece.color == AI_COLOR:
                self.green_kings += 1
            else:
                self.orange_kings += 1

    def remove(self, pieces):
        """
        Removing the piece if it is eaten
        """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == PLAYER_COLOR:
                    self.orange_left -= 1
                else:
                    self.green_left -= 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        """
        Getting the valid moves for a piece
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == PLAYER_COLOR or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == AI_COLOR or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skip=[]):
        """
        Creating a move through left diagonal
        """
        moves = {}
        last = []
        for i in range(start, stop, step):
            if left < 0:
                break
            current_pos = self.board[i][left]
            if current_pos == 0:
                if skip and not last:
                    break
                elif skip:
                    moves[(i, left)] = last + skip
                else:
                    moves[(i, left)] = last

                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)

                    moves.update(self._traverse_left(i+step, row, step, color, left-1, skip=last))
                    moves.update(self._traverse_right(i + step, row, step, color, left + 1, skip=last))
                break
            elif current_pos.color == color:
                break
            else:
                last = [current_pos]

            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skip=[]):
        """
        Creating a move through right diagonal

        """
        moves = {}
        last = []
        for i in range(start, stop, step):
            if right >= COLS:
                break
            current_pos = self.board[i][right]
            if current_pos == 0:
                if skip and not last:
                    break
                elif skip:
                    moves[(i, right)] = last + skip
                else:
                    moves[(i, right)] = last

                if last:
                    if step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, ROWS)

                    moves.update(self._traverse_left(i + step, row, step, color, right - 1, skip=last))
                    moves.update(self._traverse_right(i + step, row, step, color, right + 1, skip=last))
                break
            elif current_pos.color == color:
                break
            else:
                last = [current_pos]

            right += 1
        return moves

    def get_winner(self):
        """
        Getting the winner of the game
        """
        if self.orange_left <= 0:
            return AI_COLOR
        elif self.green_left <= 0:
            return PLAYER_COLOR

        return None








