from board import Board
from random import choice


class DefensiveBot:

    def __init__(self, piece):
        self.piece = piece
        self.nextMove = 0
        self.positionc = 0

    def almost_win(self, curBoard, myPiece, oppPiece):
        for c in range(curBoard.cols):
            r = 0
            while r < curBoard.rows:
                if c < curBoard.cols - 3:
                    if curBoard.state[r][c] == oppPiece and curBoard.state[r][c+1] == oppPiece and \
                            curBoard.state[r][c+2] == oppPiece:
                        if curBoard.state[r][c+3] == '0':
                            self.nextMove = 1
                            self.positionc = c+3
                        elif curBoard.is_valid_popout(c+3, myPiece):
                            self.nextMove = 2
                            self.positionc = c+3
                        return True
                    if r >= 3:
                        if curBoard.state[r][c] == oppPiece and curBoard.state[r-1][c+1] == oppPiece and \
                                curBoard.state[r-2][c+2] == oppPiece:
                            if curBoard.state[r-3][c+3] == '0' and (r-2 != -1 and curBoard.state[r-2][c+3] == 0):
                                self.nextMove = 1
                                self.positionc = c+3
                            elif curBoard.is_valid_popout(c+3, myPiece):
                                self.nextMove = 2
                                self.positionc = c+3
                            return True
                # checking vertical 'windows' of 4 for win
                if r < curBoard.rows - 3:
                    if curBoard.state[r][c] == oppPiece and curBoard.state[r+1][c] == oppPiece and \
                            curBoard.state[r+2][c] == oppPiece:
                        if curBoard.state[r+3][c] == '0':
                            self.nextMove = 1
                            self.positionc = c
                        elif curBoard.is_valid_popout(c+3, myPiece):
                            self.nextMove = 2
                            self.positionc = c
                        return True
                # checking negative sloped diagonal
                if c >= 3 and r >= 3 and r < curBoard.rows:
                    if curBoard.state[r][c] == oppPiece and curBoard.state[r-1][c-1] == oppPiece and \
                            curBoard.state[r-2][c-2] == oppPiece:
                        if curBoard.state[r-3][c-3] == '0' and (r-2 != -1 and curBoard.state[r-2][c+3] == 0):
                            self.nextMove = 1
                            self.positionc = c-3
                        elif curBoard.is_valid_popout(c-3, myPiece):
                            self.nextMove = 2
                            self.positionc = c-3
                        return True
                r += 1
        return False

    def playMove(self, board, myPiece, oppPiece):
        valid = self.almost_win(board, myPiece, oppPiece)
        if (valid == False):
            bestMove = choice(board.get_valid_moves(myPiece))
            if bestMove[1] == 0:
                board.drop_piece(bestMove[0], myPiece)
            else:
                board.popout_piece(bestMove[0])
        elif self.nextMove == 1:
            board.dropPiece(self.positionc, myPiece)
            self.nextMove = 0
        elif self.nextMove == 2:
            board.popout_piece(self.positionc)
            self.nextMove = 0

    def __str__(self):
        return 'rulesBot'
