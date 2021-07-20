def solution(n, k):
    table = [i for i in range(1,n + 1)]
    answer = []
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    if n == 1:
        return [1]
    if n == 2:
        if k == 1:
            return [1,2]
        else:
            return [2,1]
    for i in range(2,n):
        dp[i] = dp[i - 1] * (i + 1)
    while (n != 0):
        tmp = dp[n - 1] // n
        index = k // tmp
        k = k % tmp
        if k == 0:
            answer.append(table.pop(index - 1))
        else :
            answer.append(table.pop(index))
        n -= 1
    return answer
print(solution(3,5))
