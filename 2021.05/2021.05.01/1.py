def solution(inputString):
    answer = ['(',')','{','}','[',']','<','>']
    a = dict()
    result = dict()
    left = []
    right = []
    for i in range(len(inputString)):
        for j in answer:
            if inputString[i] == j:
                result[j] = i
    mid = int(len(result.keys()) / 2)
    if mid > 2 and mid % 2 != 0:
        mid += 1
    left = list(result.keys())[:mid]
    right = list(result.keys())[mid:]
    if len(left) != 0:
        if left[0] == ')' or left[0] == '}' or left[0] == ']' or left[0] == '>':
            return 0
    for i in range(len(left)):
        if len(right) <= i:
            return -len(inputString) + 1
        if left[len(left) - i - 1] == '(':
            if left[len(left) - i - 1] != chr(ord(right[i]) - 1):
                return -result[right[i]]
        else:
            if left[len(left) - i - 1] != chr(ord(right[i]) - 2):
                return -result[right[i]]     
    return len(left)
print(solution("x * (y + z) ^ 2 = ?"))
