def solution(number, k):
    result = []
    for i in number:
        while result and result[-1] < i:
            if k > 0:
                result.pop()
                k -= 1
            else:
                break
        result.append(i)
    if k > 0:
        for _ in range(k):
            result.pop()
    return ''.join(result)
print(solution('123123',5))
