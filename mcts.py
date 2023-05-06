from board import Board
from node import Node
from evaluate import winning_move
import random
from math import sqrt, log

def mcts(board, myPiece, oppPiece, rootNode=None):
    if rootNode == None:
        root = Node(board,curTurn=0)
        validMoves = board.get_valid_moves(myPiece)
        # creates root node children 
        for move in validMoves:
            copyBoard = board.copyBoard()
            if move[1] == 0:
                copyBoard.drop_piece(move[0], myPiece)
                nextNode = Node(copyBoard, move, root, 1)
            elif move[1] == 1:
                copyBoard.popout_piece(move[0])
                nextNode = Node(copyBoard, move, root, 1)
            root.children.append(nextNode)        
    else:
        root = rootNode
    while root.visits <= 4000:
        nextMove = selection(root, myPiece, oppPiece)
        expansion(nextMove, myPiece, oppPiece, nextMove.curTurn)
        sim_val = simulation(random.choice(nextMove.children), myPiece, oppPiece, 0)
        backpropagation(nextMove, sim_val)
    bestWinRate = -1
    bestNode = root
    for i in range(len(root.children)):
        curWinRate = root.children[i].wins / root.children[i].visits
        # print(f'col {i}: visits {root.children[i].visits}, wins {root.children[i].wins} rate {curWinRate}')
        if curWinRate > bestWinRate:
            bestNode = root.children[i]
            bestWinRate = curWinRate
    return bestNode.curMove, bestNode

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

def expansion(curNode, curPiece, oppPiece, curTurn):
    if curTurn == 0:
        nextTurn = 1
        piece = curPiece
    else:
        nextTurn = 0
        piece = oppPiece
    validMoves = curNode.curBoard.get_valid_moves(piece)
    for move in validMoves:
        copyBoard = curNode.curBoard.copyBoard()
        if move[1] == 0:
            copyBoard.drop_piece(move[0], piece)
            nextNode = Node(copyBoard, move, curNode, nextTurn)
        elif move[1] == 1:
            copyBoard.popout_piece(move[0])
            nextNode = Node(copyBoard, move, curNode, nextTurn)
        curNode.children.append(nextNode)

def simulation(curNode, myPiece, oppPiece, curTurn):
    # check who's turn 
    copyBoard = curNode.curBoard.copyBoard()
    if curTurn == 0: # my turn
        validMoves = copyBoard.get_valid_moves(myPiece)
        if len(validMoves) == 0:
            return 0
        for move in validMoves:
            b_copy = curNode.curBoard.copyBoard()
            if move[1] == 0:
                b_copy.drop_piece(move[0], myPiece)
            elif move[1] == 1:
                b_copy.popout_piece(move[0])
            if winning_move(b_copy, myPiece):
                # curNode.wins += 1
                return 1
            elif winning_move(b_copy, oppPiece):
                # curNode.wins += -1
                return -1
        nextMove = random.choice(validMoves)
        if nextMove[1] == 0:
            copyBoard.drop_piece(nextMove[0], myPiece)
        elif nextMove[1] == 1:
            copyBoard.popout_piece(nextMove[0])
        # check if terminal node 
        if winning_move(copyBoard, myPiece):
            winVal = 1
        elif winning_move(copyBoard, oppPiece):
            winVal = -1
        else:
            winVal = simulation(Node(copyBoard), myPiece, oppPiece, 1)
        curNode.wins += winVal
    else:
        validMoves = copyBoard.get_valid_moves(oppPiece)
        if len(validMoves) == 0:
            return 0
        for move in validMoves:
            b_copy = curNode.curBoard.copyBoard()
            if move[1] == 0:
                b_copy.drop_piece(move[0], oppPiece)
            elif move[1] == 1:
                b_copy.popout_piece(move[0])
            if winning_move(b_copy, oppPiece):
                # curNode.wins += -1
                return -1
            elif winning_move(b_copy, myPiece):
                # curNode.wins += 1
                return 1
        nextMove = random.choice(validMoves)
        if nextMove[1] == 0:
            copyBoard.drop_piece(nextMove[0], oppPiece)
        elif nextMove[1] == 1:
            copyBoard.popout_piece(nextMove[0])
        # check if terminal node 
        if winning_move(copyBoard, oppPiece):
            winVal = -1
        elif winning_move(copyBoard, myPiece):
            winVal = 1
        else:
            winVal = simulation(Node(copyBoard), myPiece, oppPiece, 0)
        # curNode.wins += winVal

    return winVal

def backpropagation(curNode, winVal):
    curNode.visits += 1
    curNode.wins += winVal
    if curNode.parent != None:
        backpropagation(curNode.parent, winVal)

def ucb(curNode):
    EXPLORE_PARAM = sqrt(4)
    averageWins = curNode.wins / curNode.visits
    underRoot = sqrt(log(curNode.parent.visits) / curNode.visits)
    return averageWins + EXPLORE_PARAM * underRoot