from randomBot import RandomBot
from minimaxBot import MiniMaxBot
from mctsBot import MctsBot
from board import Board
from evaluate import winning_move
from random import choice
from os import system


def simGame(bot1, bot2):
    curBoard = Board(6, 7)
    BOT1TURN = 1
    BOT2TURN = 2
    SHOWBOARD = 0

    turn = choice([1, 2])
    play = 1
    curMove = 0

    if SHOWBOARD:
        system('clear')
        print(curBoard)

    while play:
        if turn == BOT1TURN:
            if len(curBoard.get_valid_moves(bot1.piece)) == 0:
                return 'draw'
            bot1.playMove(curBoard, bot1.piece, bot2.piece)
            if SHOWBOARD:
                system('clear')
                print(curBoard)
            if winning_move(curBoard, bot1.piece):
                return str(bot1)
            elif winning_move(curBoard, bot2.piece):
                return str(bot2)
            else:
                turn = BOT2TURN
        elif turn == BOT2TURN:
            bot2.playMove(curBoard, bot2.piece, bot1.piece)
            if SHOWBOARD:
                system('clear')
                print(curBoard)
            if winning_move(curBoard, bot2.piece):
                return str(bot2)
            elif winning_move(curBoard, bot1.piece):
                return str(bot1)
            else:
                turn = BOT1TURN
        else:
            return 'error'
