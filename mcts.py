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
        copyBoard = board.copyBoard()
        if move[1] == 0:
            copyBoard.drop_piece(move[0], myPiece)
            nextNode = Node(copyBoard, move, root)
        elif move[1] == 1:
            copyBoard.popout_piece(move[0])
            nextNode = Node(copyBoard, move, root)
        root.children.append(nextNode)
    for i in range(2000):
        nextMove = selection(root, myPiece, oppPiece)
        expansion(nextMove, myPiece)
        sim_val = simulation(random.choice(nextMove.children), myPiece, oppPiece, 0)
        backpropagation(nextMove, sim_val)
    bestWinRate = -1
    bestNode = root
    for i in range(len(root.children)):
        curWinRate = root.children[i].wins / root.children[i].visits
        if curWinRate > bestWinRate:
            bestNode = root.children[i]
            bestWinRate = curWinRate
    return bestNode.curMove

def selection(rootNode, myPiece, oppPiece):
    bestNode = rootNode
    value = -1
    for n in rootNode.children:
        curVal = ucb(n)
        if curVal > value:
            bestNode = n
            value = curVal
    # recursively search for best node by ucb   
    if len(bestNode.children) != 0:
        bestNode = selection(bestNode, myPiece, oppPiece)
    return bestNode

def expansion(curNode, curPiece):
    validMoves = curNode.curBoard.get_valid_moves(curPiece)
    for move in validMoves:
        copyBoard = curNode.curBoard.copyBoard()
        if move[1] == 0:
            copyBoard.drop_piece(move[0], curPiece)
            nextNode = Node(copyBoard, move, curNode)
        elif move[1] == 1:
            copyBoard.popout_piece(move[0])
            nextNode = Node(copyBoard, move, curNode)
        curNode.children.append(nextNode)

def simulation(curNode, myPiece, oppPiece, curTurn):
    # check who's turn 
    if curTurn == 0:
        curPiece = myPiece
        otherPiece = oppPiece
        nextTurn = 1
    else:
        curPiece = oppPiece
        otherPiece = myPiece
        nextTurn = 0
    copyBoard = curNode.curBoard.copyBoard()
    validMoves = copyBoard.get_valid_moves(curPiece)
    if len(validMoves) == 0:
        winVal = 0
    else:
        nextMove = random.choice(validMoves)
        if nextMove[1] == 0:
            copyBoard.drop_piece(nextMove[0], curPiece)
        elif nextMove[1] == 1:
            copyBoard.popout_piece(nextMove[0])
        # check if terminal node 
        if winning_move(copyBoard, myPiece):
            winVal = 1
        elif winning_move(copyBoard, oppPiece):
            winVal = 0
        else:
            winVal = simulation(Node(copyBoard), myPiece, oppPiece, nextTurn)
        curNode.wins += winVal
    return winVal

def backpropagation(curNode, winVal):
    curNode.visits += 1
    curNode.wins += winVal
    if curNode.parent != None:
        backpropagation(curNode.parent, winVal)

def ucb(curNode):
    EXPLORE_PARAM = sqrt(2)
    averageWins = curNode.wins / curNode.visits
    underRoot = sqrt(log(curNode.parent.visits) / curNode.visits)
    return averageWins + EXPLORE_PARAM * underRoot