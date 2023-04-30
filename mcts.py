from board import Board
from node import Node
from evaluate import winning_move
import random
from math import sqrt, log

def mcts(board, myPiece, oppPiece):
    root = Node(board)
    validMoves = board.get_valid_moves(myPiece)
    # creats root node children 
    for move in validMoves:
        copyBoard = board.copy()
        if move[1] == 0:
            copyBoard.drop_piece(move[0], myPiece)
            nextNode = Node(copyBoard, root)
        elif move[1] == 1:
            copyBoard.popout_piece(move[0])
            nextNode = Node(copyBoard, root)
        root.children.append(nextNode)
    for i in range(100):
        nextMove = selection(root, myPiece, oppPiece)
        expanded = expansion(nextMove, myPiece)
        sim_val = simulation(nextMove, expanded, myPiece, oppPiece, 0)
        root.wins += sim_val
        root.visits += 1

    return nextMove

def selection(rootNode, myPiece, oppPiece):
    bestNode = rootNode
    value = -1
    for n in rootNode.children:
        curVal = ucb(n)
        if curVal > value:
            bestNode = n
            value = curVal
    bestNode.visits += 1
    # recursively search for best node by ucb 
    if len(bestNode.children) != 0:
        bestNode = selection(bestNode.curBoard, myPiece, oppPiece)

    return bestNode

def expansion(curNode, curPiece):
    curNode.visits += 1
    return curNode.curBoard.get_valid_moves(curPiece)

def simulation(curNode, listNextMoves, myPiece, oppPiece, curTurn):
    # check who's turn 
    if curTurn == 0:
        curPiece = myPiece
        otherPiece = oppPiece
        nextTurn = 1
    else:
        curPiece = oppPiece
        otherPiece = myPiece
        nextTurn = 0
    nextMove = random.choice(listNextMoves)
    copyBoard = curNode.curBoard.copy()
    if nextMove[1] == 0:
        copyBoard.drop_piece(nextMove[0], curPiece)
    elif nextMove[1] == 1:
        copyBoard.popout_piece(nextMove[0])
    if len(copyBoard.get_valid_moves(curPiece)) == 0:
        winVal = 0
    elif winning_move(copyBoard, curPiece):
        winVal = 1
    elif winning_move(copyBoard, otherPiece):
        winVal = 0
    else:
        # TODO: update wins and visits
        winVal = simulation(Node(copyBoard), copyBoard.get_valid_moves(curPiece), myPiece, oppPiece, nextTurn)
    curNode.wins += winVal
    return winVal

def ucb(curNode):
    EXPLORE_PARAM = 2
    averageWins = curNode.wins / curNode.visits
    underRoot = sqrt(log(curNode.parent.visits) / curNode.visits)
    return averageWins + EXPLORE_PARAM * underRoot