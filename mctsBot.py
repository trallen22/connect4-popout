from board import Board
from node import Node
from evaluate import winning_move
import random
from math import sqrt, log
from mcts import mcts

class MctsBot:

    def __init__(self, piece):
        self.piece = piece

    def playMove(self, board, myPiece, oppPiece):
        bestMove = mcts(board, myPiece, oppPiece)
        if bestMove[1] == 0:
            board.drop_piece(bestMove[0], myPiece)
        else:
            board.popout_piece(bestMove[0])
    
    def __str__(self):
        return 'MCTSBOT'