from board import Board
from evaluate import score_board, winning_move
import math
import random
import sys

def minimax(board, depth, alpha, beta, maximizing_player):
    action = 0

    curPiece = 2 # AI is maximizing
    oppPiece = 1

    if depth == 0:
        return (None, score_board(board, curPiece, oppPiece), 0)
    
    # if the current board is not terminal and we are maximizing
    if maximizing_player:
        if winning_move(board, oppPiece):
            return (None, sys.maxsize, 0)
        elif winning_move(board, curPiece):
            return (None, -sys.maxsize-1, 0)

        valid_moves = board.get_valid_moves(curPiece)

        # initial value is what we do not want - negative infinity
        value = -math.inf

        # this will be the optimal column. Initially it is random
        column = -1

        # for every valid column, we simulate dropping a piece with the help of a board copy
        # and run the minimax on it with decresed depth and switched player
        for move in valid_moves:
            b_copy = board.copyBoard()
            if move[1] == 0:
                b_copy.drop_piece(move[0], curPiece)
            elif move[1] == 1:
                b_copy.popout_piece(move[0])
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = move[0]
                action = move[1]
            # alpha is the best option we have overall
            alpha = max(value, alpha)
            # if alpha (our current move) is greater (better) than beta (opponent's best move), then
            # the oponent will never take it and we can prune this branch
            if alpha >= beta:
                break
        return column, value, action

    # same as above, but for the minimizing player
    else:  # for the minimizing player
        
        if winning_move(board, curPiece):
            return (None, sys.maxsize, 0)
        elif winning_move(board, oppPiece):
            return (None, -sys.maxsize-1, 0)

        valid_moves = board.get_valid_moves(oppPiece)
        value = math.inf
        column = 0

        for move in valid_moves:
            b_copy = board.copyBoard()
            if move[1] == 0:
                b_copy.drop_piece(move[0], oppPiece)
            elif move[1] == 1:
                b_copy.popout_piece(move[0])
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = move[0]
                action = move[1]
            beta = min(value, beta)
            if alpha >= beta:
                break
        return column, value, action