import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n > 0:
        target = heapq.heappop(works) + 1
        heapq.heappush(works,target)
        n -= 1
    for i in works:
        answer += i ** 2
    return answer
solution(4,[4,3,3])
solution(99,[2, 15, 22, 55, 55])
    
