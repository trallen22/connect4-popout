from board import Board
from new_minimax import minimax
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

turn = random.choice([0, 1])

turn = 0

os.system('clear')
print(curBoard)

while play:
    
    if turn == PLAYER_TURN: 
        player_move = input("play move (d#) drop or (p#) pop: ")
        if player_move[0] == 'd':
            curBoard.drop_piece(int(player_move[1]), PLAYER_PIECE)
        elif player_move[0] == 'p':
            curBoard.popout_piece(int(player_move[1]))
        elif player_move == 'quit':
            play = 0
        os.system('clear')
        print(curBoard)
        if winning_move(curBoard, PLAYER_PIECE):
            print("CONGRATS PLAYER")
            play = 0
        else: 
            turn = AI_TURN

    elif turn == AI_TURN:
        col, value, action = minimax(
            curBoard, 5, -math.inf, math.inf, True)
        if action == 0: # drop 
            curBoard.drop_piece(col, AI_PIECE)
        elif action == 1: # pop
            curBoard.popout_piece(col)
        else:
            print('something went wrong')
        os.system('clear')
        print(curBoard)
        if winning_move(curBoard, AI_PIECE):
            print("CONGRATS COMPUTER")
            play = 0
        else: 
            turn = PLAYER_TURN

    