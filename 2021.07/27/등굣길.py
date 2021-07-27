def solution(m, n, puddles):
    dp = [[1] * m for _ in range(n)]
    for i,j in puddles:
        dp[j - 1][i - 1] = 0
        if j == 1:
            for i in range(i,m):
                dp[0][i] = 0
        if i == 1:
            for i in range(j,n):
                dp[i][0] = 0
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] == 0:
                continue
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n - 1][m - 1] % 1000000007
print(solution(4,3,[[1,2],[2,1]]))
            
            
    
    
    

