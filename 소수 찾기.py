from itertools import permutations
def solution(numbers):
    num = set()
    answer = 0
    for i in range(1,len(numbers) + 1):
        for e in list(permutations(numbers,i)):
            n = int(''.join(e))
            if n != 0:
                num.add(n)
    for j in num:
         if prime(j):
            answer += 1
    return answer
def prime(num):
    if num != 1:
        for i in range(2,num):
            if num % i == 0:
                return False
    else:
        return False
    return True
