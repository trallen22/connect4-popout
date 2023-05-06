from board import Board
from node import Node
from evaluate import winning_move
import random
from math import sqrt, log
from mcts import mcts

class MctsBot:

    def __init__(self, piece):
        self.piece = piece
        self.root = None

    def playMove(self, board, myPiece, oppPiece):
        if self.root != None:
            self.root = self.getLastMove(board, oppPiece)
        bestMove, self.root = mcts(board, myPiece, oppPiece, self.root)
        if bestMove[1] == 0:
            board.drop_piece(bestMove[0], myPiece)
        else:
            board.popout_piece(bestMove[0])
            
    def getLastMove(self, curBoard, oppPiece):
        
        children = self.root.children
        for i in range(len(children)):
            b_copy = self.root.curBoard.copyBoard()
            if children[i].curMove[1] == 0:
                b_copy.drop_piece(children[i].curMove[0], oppPiece)
            else:
                b_copy.popout_piece(children[i].curMove[0])
            if (b_copy.state == curBoard.state).all():
                return children[i]
    
    def __str__(self):
        return 'MCTSBOT'