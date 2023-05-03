from board import Board 
from random import choice

class RandomBot:
    
    def __init__(self, piece):
        self.piece = piece

    def playMove(self, board, myPiece, oppPiece):
        bestMove = choice(board.get_valid_moves(myPiece))
        if bestMove[1] == 0:
            board.drop_piece(bestMove[0], myPiece)
        else:
            board.popout_piece(bestMove[0])
        
    
    def __str__(self):
        return 'RANDOMBOT'