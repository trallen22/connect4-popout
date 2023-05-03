from board import Board 
from random import choice

class RandomBot:
    
    def __init__(self, piece):
        self.piece = piece

    def chooseMove(self, board, myPiece, oppPiece):
        return choice(board.get_valid_moves(myPiece))
    
    def __str__(self):
        return 'RANDOMBOT'