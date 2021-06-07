""" 31m """
def solution(brown, yellow):
    answer = getDivisor(brown + yellow)
    square = []
    for i in range(int(len(answer) / 2)):
        width = answer[ -(i + 1) ]
        height = answer[i]
        if height < 3:
            continue
        else:
            square.append([width,height])
    for i in square:
        if getYellow(i) == yellow:
            return i
def getDivisor(n):
    n = int(n)
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(i) 
    if len(divisors) % 2 == 1:
        mid = int(len(divisors) / 2)
        divisors.insert(mid,divisors[mid])
    return divisors
def getYellow(square):
    return int((square[0] - 2) * (square[1] - 2))
print(solution(10,2))
