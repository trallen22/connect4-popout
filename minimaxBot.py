from new_minimax import minimax
from math import inf

class MiniMaxBot:
    def __init__(self, piece):
        self.piece = piece

    def playMove(self, board, myPiece, oppPiece):
        DEPTH = 4
        col, val, action = minimax(board, DEPTH, -inf, inf, True, myPiece, oppPiece)
        bestMove = [col, action]
        if bestMove[1] == 0:
            board.drop_piece(bestMove[0], myPiece)
        else:
            board.popout_piece(bestMove[0])
    
    def __str__(self):
        return 'MINIMAXBOT'