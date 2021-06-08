from copy import deepcopy
import pygame
from constants import PLAYER_COLOR, AI_COLOR


def minimax_algorithm(pos, depth, player_max, game):
    if depth == 0 or pos.get_winner() != None:
        return pos.eval(), pos

    if player_max:
        max_eval = float('-inf')
        best_move = None

        for move in all_moves(pos, AI_COLOR, game):
            evaluation = minimax_algorithm(move, depth-1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move

    else:
        min_eval = float('inf')
        best_move = None
        for move in all_moves(pos, PLAYER_COLOR, game):
            evaluation = minimax_algorithm(move, depth-1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move


def all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = move_simulation(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def move_simulation(piece, move, board, game, skip):
    board.movement(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board



