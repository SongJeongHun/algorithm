def solution(rows, columns, queries):
    board = [(columns * i) + j + 1 for i in range(rows) for j in range(columns)]
    queue = []
    index_queue = []
    answer = []
    for i in queries:
        tl = columns * (i[0] - 1) + (i[1] - 1)
        tr = columns * (i[0] - 1) + (i[3] - 1)
        bl = columns * (i[2] - 1) + (i[1] - 1)
        br = columns * (i[2] - 1) + (i[3] - 1)
        for j in range(tl,tr):
            queue.append(board[j])
            index_queue.append(j)
        for _ in range(i[2] - i[0]):
            queue.append(board[tr])
            index_queue.append(tr)
            tr += columns
        for j in range(br,bl,-1):
            queue.append(board[j])
            index_queue.append(j)
        for _ in range(i[2] - i[0]):
            queue.append(board[bl])
            index_queue.append(bl)
            bl -= columns
        answer.append(min(queue))
        queue = [queue[-1]] + queue[:-1]
        for j in range(len(index_queue)):
            board[index_queue[j]] = queue[j]
        queue = []
        index_queue = []
    return answer
print(solution(97,100,[[1,1,97,100]]))
