from math import sqrt, log

class Node:
    def __init__(self, curBoard, curMove=None, parent=None):
        self.curBoard = curBoard
        self.curMove = curMove
        self.visits = 1
        self.wins = 0
        self.parent = parent
        self.children = []

    def __str__(self):
        state = self.curBoard.state
        curBoard = '\n'
        for i in range(len(state)):
            for j in range(len(state[0])):
                curBoard += f' {int(state[i][j])}'
            curBoard += '\n'
        curBoard += '\n'
        for i in range(len(state[0])):
            curBoard += f' {i}'
        curBoard += '\n'
        return curBoard 