import heapq
def solution(scoville, K):
    queue = []
    count = 0
    for i in scoville:
        heapq.heappush(queue,i)
    while queue[0] < K:
        new = heapq.heappop(queue) + heapq.heappop(queue) * 2
        heapq.heappush(queue,new)
        count += 1
        if len(queue) == 1 and queue[0] < K:
            return - 1 
    return count
