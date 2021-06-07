import sys
import collections
sys.setrecursionlimit(50000)
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    return recursive(collections.deque(people),limit,0)
def recursive(people,limit,count):
    if len(people) == 0:
        return count
    if len(people) == 1:
        return count + 1
    first = people.popleft()
    if first + people[-1] <= limit:
        people.pop()
        return recursive(people,limit,count + 1)
    else:
        return recursive(people,limit,count + 1)
print(solution([20, 50, 50, 80,200],200))
print(solution([20, 50, 50, 80,40,50,45,45,100],100))
print(solution([20, 50, 50, 100,150,110,200],250))
print(solution([40, 40, 40],100))
print(solution([40, 40, 40,99,98,100],100))
