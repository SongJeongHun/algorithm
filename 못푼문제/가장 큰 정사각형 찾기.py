def solution(board):
    if len(board) == 1:
        return 1
    for i in range(len(board) - 1,0,-1):
        for j in range(len(board)):
            target = board[j]
            for k in range(len(target)):
                if search(board,i,[j,k]):
                    return (i + 1) * (i + 1)
def search(square,width,start):
    if start[0] + width >= len(square) or start[1] + width >= len(square[0]):
        return False
    for i in range(start[0],start[0] + width + 1):
        target = square[i]
        for j in range(start[1],start[1] + width + 1):
            if target[j] == 0:
                return False
    return True
print(solution([[1, 0], [0, 0]]))

            
            
            
    
