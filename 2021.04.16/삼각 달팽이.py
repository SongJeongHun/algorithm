""" 2h 12m """
import itertools
def solution(n):
    global answer
    answer = [[0] * i for i in range(1,n + 1)]
    depth = 0
    index = 0
    num = 1
    end = int(n * (n + 1) / 2)
    recursive(depth,index,num,n,end,1)
    return list(itertools.chain( * answer))
def recursive(depth,index,num,n,end,time):
    if num == end + 1:
        return
    for _ in range(n):
        answer[depth][index] = num
        depth += 1
        num += 1
    depth -= 1
    index += 1
    for _ in range(n - 1):
        answer[depth][index] = num
        index += 1
        num += 1
    depth -= 1
    for _ in range(n - 2):
        index = len(answer[depth]) - time
        answer[depth][index] = num
        depth -= 1
        num += 1
    return recursive(depth +2,index,num,n - 3,end,time + 1)
solution(10)
