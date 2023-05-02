from board import Board 
from random import choice

def randomMove(board, myPiece):
    return choice(board.get_valid_moves(myPiece))