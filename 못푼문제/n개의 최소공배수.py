from itertools import combinations
import collections
def solution(arr):
    queue = collections.deque(sorted(arr,reverse = True))
    arr = list(map(str,arr))
    num = queue.popleft()
    for i in queue:
        target = num * i
        if ''.join(arr) in getDivisor(target):
            return target       
    return arr
def getDivisor(n):
    n = int(n)
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(str(i)) 
    return divisors
solution([1,2,4,5,5])
