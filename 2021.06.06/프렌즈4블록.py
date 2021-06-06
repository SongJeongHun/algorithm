def solution(m, n, board):
    answer = 0
    isBoom = True
    stack_board = []
    for i in range(n):
        stack = []
        for j in range(m):
            stack.append(board[j][i])
        stack_board.append(stack[::-1])
    while(isBoom):
        stack_board,isBoom,answer = boom(stack_board,answer)
    return answer
def boom(board,count):
    isBoom = False
    for i in range(len(board) - 1):
        if len(board[i]) < len(board[i + 1]):
            target = len(board[i])
        else:
            target = len(board[i + 1])
        for j in range(target - 1):
            if board[i][j].upper() == board[i][j + 1].upper() and board[i][j].upper() == board[i + 1][j].upper() and board[i][j].upper() == board[i + 1][j + 1].upper():
                board[i][j] = board[i][j].lower()
                board[i + 1][j] = board[i + 1][j].lower()
                board[i][j + 1] = board[i][j + 1].lower()
                board[i + 1][j + 1] = board[i + 1][j + 1].lower()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].islower():
                board[i][j] = ''
                count += 1
                isBoom = True
    for i in range(len(board)):
        board[i] = list(''.join(board[i]))
    return board,isBoom,count    
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
