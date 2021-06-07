"""41 min"""
def solution(board, moves):
    answer = 0
    n = len(board)
    stack_board = []
    bucket = []
    for i in range(n):
        stack = []
        for j in range(n):
            if board[j][i] != 0:
                stack.append(board[j][i])
        stack_board.append(stack)    
    for i in moves:
        if stack_board[i - 1]:
            friend = stack_board[i - 1].pop(0) 
            bucket.append(friend)
        if boom(bucket):
            answer += 2
    return answer
def boom(bucket):
    for i in range(len(bucket) - 1):
        if bucket[i] == bucket[i + 1]:
            bucket.pop(i)
            bucket.pop(i)
            return True
    return False
solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
