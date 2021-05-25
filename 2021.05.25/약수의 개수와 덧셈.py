def solution(left, right):
    answer = ""
    for i in range(left,right + 1):
        answer += getDivisor(i) + str(i)
    return eval(answer)
def getDivisor(n):
    n = int(n)
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(i) 
    if len(divisors) % 2 == 1:
        return '-'
    else:
        return '+'
