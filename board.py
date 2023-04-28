import numpy as np

class Board:
    def __init__(self, rows=None, cols=None, copy=None):
        if type(copy) != np.ndarray:
            self.state = np.zeros((rows, cols))
        else:
            self.state = copy
        self.rows = rows
        self.cols = cols

    def get_valid_drops(self):
        valid_locations = []
        for column in range(self.cols):
            if self.is_valid_drop(column):
                valid_locations.append(column)
        return valid_locations

    def is_valid_drop(self, col):
        if col >= self.cols or col < 0:
            return False
        else:
            return self.state[0][col] == 0

    def drop_piece(self, col, piece):
        for r in range(self.rows-1, -1, -1):
            if self.state[r][col] == 0:
                self.state[r][col] = piece
                break

    def get_valid_popouts(self, cur_piece):
        valid_popouts = []
        for column in range(self.cols):
            if self.is_valid_popout(column, cur_piece):
                valid_popouts.append(column)
        return valid_popouts

    def is_valid_popout(self, col, player_piece):
        if col >= self.cols or col < 0:
            return False
        else:
            return player_piece == self.state[self.rows - 1][col]

    def popout_piece(self, col):
        for i in range(self.rows - 1, 0, -1):
            # moves every piece down one spot
            self.state[i][col] = self.state[i-1][col]
        self.state[0][col] = 0

    def get_valid_moves(self, curPiece):
        validMoves = []
        for col in self.get_valid_drops():
            validMoves.append([col, 0])
        for col in self.get_valid_popouts(curPiece):
            validMoves.append([col, 1])
        return validMoves

    def no_moves(self, curPiece):
        if len(self.get_valid_moves(curPiece)) == 0:
            return True
        else: 
            return False

    def copy(self):
        return Board(self.rows, self.cols, self.state.copy())

    def __str__(self):
        curBoard = '\n'
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                curBoard += f' {int(self.state[i][j])}'
            curBoard += '\n'
        curBoard += '\n 0 1 2 3 4 5 6\n'
        return curBoard