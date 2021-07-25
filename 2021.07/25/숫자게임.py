import heapq

def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while B:
        targetA = heapq.heappop(A)
        targetB = heapq.heappop(B)
        if targetA < targetB:
            answer += 1
        else:
            heapq.heappush(A,targetA)
    return answer
solution([5,1,3,7],[2,2,6,8])
