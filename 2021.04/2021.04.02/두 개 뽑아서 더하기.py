""" 8 min """
from itertools import permutations
def solution(numbers):
    answer = set()
    for i in list(permutations(numbers,2)):
        answer.add(i[0] + i[1])
    return sorted(list(answer))
