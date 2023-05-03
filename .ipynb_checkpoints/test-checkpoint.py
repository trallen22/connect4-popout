from board import Board
from evaluate import score_board
import numpy as np
import random
from mctsBot import MctsBot
from randomBot import RandomBot
from minimaxBot import MiniMaxBot
from simulate import simGame
from tqdm import tqdm

MY_PIECE = 1
AI_PIECE = 2
NUMGAMES = 100
OUTPUTFILE = 'OUTPUTFILE.txt'

bot1 = MctsBot(AI_PIECE)
bot2 = RandomBot(MY_PIECE)
bot3 = MiniMaxBot(3)

# MCTS VS RANDOM
winnerDict = {str(bot1): 0, str(bot2): 0, 'draw': 0}

pbar = tqdm(desc='games played', total = NUMGAMES)
for i in range(NUMGAMES):
    winnerDict[str(simGame(bot1, bot2))] += 1
    pbar.update(1)
with open(OUTPUTFILE, 'a') as f:
    f.write(f'##### {bot1} vs {bot2}\n')
    for i in winnerDict:
        f.write(f'{i}: {winnerDict[i]}\n')

# MINIMAX VS RANDOM
winnerDict = {str(bot3): 0, str(bot2): 0, 'draw': 0}

pbar = tqdm(desc='games played', total = NUMGAMES)
for i in range(NUMGAMES):
    winnerDict[str(simGame(bot3, bot2))] += 1
    pbar.update(1)
with open(OUTPUTFILE, 'a') as f:
    f.write(f'##### {bot3} vs {bot2}\n')
    for i in winnerDict:
        f.write(f'{i}: {winnerDict[i]}\n')
        
# MCTS VS MINIMAX
winnerDict = {str(bot1): 0, str(bot3): 0, 'draw': 0}

pbar = tqdm(desc='games played', total = NUMGAMES)
for i in range(NUMGAMES):
    winnerDict[str(simGame(bot1, bot3))] += 1
    pbar.update(1)
with open(OUTPUTFILE, 'a') as f:
    f.write(f'##### {bot1} vs {bot3}\n')
    for i in winnerDict:
        f.write(f'{i}: {winnerDict[i]}\n')