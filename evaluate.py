from board import Board

def evaluate(board):
    return

def score_four(a, b, c, d, myPiece, oppPiece):
    curScore = 0
    if a == myPiece and b == myPiece and c == myPiece and d == myPiece:
        return 1000
    elif a == oppPiece and b == oppPiece and c == oppPiece and d == oppPiece:
        return -1000
    if a == myPiece:
        curScore += 2
    elif a == oppPiece:
        curScore -= 2
    if b == myPiece:
        curScore += 3
    elif b == oppPiece:
        curScore -= 3
    if c == myPiece:
        curScore += 3
    elif c == oppPiece:
        curScore -= 3
    if d == myPiece:
        curScore += 2
    elif d == oppPiece:
        curScore -= 2

    if curScore < 0:
        return -(curScore ** 2)
    else:
        return curScore ** 2

def score_board(curBoard, myPiece, oppPiece):
    # checking horizontal 'windows' of 4 for win and positively sloped diagonals
    curScore = 0
    winner = 0
    midBoard = curBoard.cols//2
    for c in range(curBoard.cols):
        r = 0
        while r < curBoard.rows:
            if c < curBoard.cols - 3:
                curScore += (4 - abs(c+1 - midBoard))**2 * score_four(
                    curBoard.state[r][c], curBoard.state[r][c+1], curBoard.state[r][c+2], curBoard.state[r][c+3], myPiece, oppPiece)
                if r >= 3:
                    curScore += (4 - abs(c+1 - midBoard))**2 * score_four(
                        curBoard.state[r][c], curBoard.state[r-1][c+1], curBoard.state[r-2][c+2], curBoard.state[r-3][c+3], myPiece, oppPiece)
            # checking vertical 'windows' of 4 for win
            if r < curBoard.rows - 3:
                curScore += (4 - abs(c - midBoard))**2 * score_four(
                    curBoard.state[r][c], curBoard.state[r+1][c], curBoard.state[r+2][c], curBoard.state[r+3][c], myPiece, oppPiece)
            # checking negative sloped diagonal
            if c >= 3 and r >= 3 and r < curBoard.rows:
                curScore += (4 - abs(c - midBoard))**2 * score_four(
                    curBoard.state[r][c], curBoard.state[r-1][c-1], curBoard.state[r-2][c-2], curBoard.state[r-3][c-3], myPiece, oppPiece)
            r += 1
            if winner == 1:
                return 10000000
            elif winner == 2:
                return -10000000
    return curScore

def winning_move(curBoard, curPiece):

    # checking horizontal 'windows' of 4 for win and positively sloped diagonals

    for c in range(curBoard.cols):
        r = 0
        while r < curBoard.rows:
            if c < curBoard.cols - 3:
                if curBoard.state[r][c] == curPiece and curBoard.state[r][c+1] == curPiece and \
                    curBoard.state[r][c+2] == curPiece and curBoard.state[r][c+3] == curPiece:
                    return True 
                if r >= 3:
                    if curBoard.state[r][c] == curPiece and curBoard.state[r-1][c+1] == curPiece and \
                        curBoard.state[r-2][c+2] == curPiece and curBoard.state[r-3][c+3] == curPiece:
                        return True
            # checking vertical 'windows' of 4 for win
            if r < curBoard.rows - 3:
                if curBoard.state[r][c] == curPiece and curBoard.state[r+1][c] == curPiece and \
                    curBoard.state[r+2][c] == curPiece and curBoard.state[r+3][c] == curPiece:
                    return True
            # checking negative sloped diagonal
            if c >= 3 and r >= 3 and r < curBoard.rows:
                if curBoard.state[r][c] == curPiece and curBoard.state[r-1][c-1] and \
                    curBoard.state[r-2][c-2] == curPiece and curBoard.state[r-3][c-3] == curPiece:
                    return True
            r += 1
    return False