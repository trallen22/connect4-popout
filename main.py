from board import Board
from new_minimax import minimax
from mcts import mcts
from evaluate import winning_move

import math
import random
import os

# row and column count
ROWS = 6
COLS = 7

# turns
PLAYER_TURN = 0
AI_TURN = 1

# pieces represented as numbers
PLAYER_PIECE = 1
AI_PIECE = 2

play = 1
curBoard = Board(ROWS, COLS)

turn = random.choice([PLAYER_TURN, AI_TURN])

chooseAI = 1
while chooseAI:
    mindset = input('which algorithm to play: minimax(a) or mcts(b)  ')
    if mindset.lower() == 'minimax' or mindset.lower() == 'a':
        chooseAI = 0
    elif mindset.lower() == 'mcts' or mindset.lower() == 'b':
        chooseAI = 0
    else:
        print(f'{mindset} is an invalid algorithm')
        mindset = input('which algorithm to play: minimax(a) or mcts(b)  ')

os.system('clear')
print(curBoard)

while play:
    
    if turn == PLAYER_TURN: 
        makeMove = 1
        while makeMove:
            # TODO: catch exceptions with bad input d- or p$
            player_move = input("play move (d#) drop or (p#) pop: ")
            if player_move[0] == 'd' and curBoard.is_valid_drop(int(player_move[1])):
                curBoard.drop_piece(int(player_move[1]), PLAYER_PIECE)
                makeMove = 0
            elif player_move[0] == 'p' and curBoard.is_valid_popout(int(player_move[1]), PLAYER_PIECE):
                curBoard.popout_piece(int(player_move[1]))
                makeMove = 0
            elif player_move == 'quit' or player_move[0] == 'q':
                play = 0
                print('Player quit')
                break
            else:
                print('invalid move')
        os.system('clear')
        if not makeMove:
            print(curBoard)
            print(f'last move: action = {player_move[0]} col = {player_move[1]}')
            if winning_move(curBoard, PLAYER_PIECE):
                print("PLAYER WINS")
                play = 0
            elif winning_move(curBoard, AI_PIECE):
                print("COMPUTER WINS")
                play = 0
            else: 
                turn = AI_TURN

    # MINIMAX
    elif turn == AI_TURN and (mindset == 'minimax' or mindset == 'a'):
        col, value, action = minimax(
            curBoard, 4, -math.inf, math.inf, True)
        if action == 0: # drop 
            curBoard.drop_piece(col, AI_PIECE)
        elif action == 1: # pop
            curBoard.popout_piece(col)
        else:
            print('something went wrong')
        os.system('clear')
        print(curBoard)
        print(f'last move: action = {action} col = {col}')
        if winning_move(curBoard, AI_PIECE):
            print("CONGRATS COMPUTER")
            play = 0
        elif winning_move(curBoard, PLAYER_PIECE):
            print("CONGRATS PLAYER")
            play = 0
        else: 
            turn = PLAYER_TURN

    # MCTS 
    elif turn == AI_TURN and (mindset == 'mcts' or mindset == 'b'):
        nextMove = mcts(curBoard, AI_PIECE, PLAYER_PIECE)
        if nextMove[1] == 0: # drop 
            curBoard.drop_piece(nextMove[0], AI_PIECE)
        elif nextMove[1] == 1: # pop
            curBoard.popout_piece(nextMove[0])
        else:
            print('something went wrong')
        os.system('clear')
        print(curBoard)
        print(f'last move: action = {nextMove[1]} col = {nextMove[0]}')
        if winning_move(curBoard, AI_PIECE):
            print("COMPUTER WINS")
            play = 0
        elif winning_move(curBoard, PLAYER_PIECE):
            print("PLAYER WINS")
            play = 0
        else: 
            turn = PLAYER_TURN
