def solution(m, n, puddles):
    dp = [[-1]*(m+1) for _ in range(n+1)]
    
    for col, row in puddles:
        dp[row][col] = 0
        
    for row in range(1, n+1):
        if dp[row][1] == 0:
            for rest in range(row, n+1):
                dp[rest][1] = 0
            break
        dp[row][1] = 1
        
    for col in range(1, m+1):
        if dp[1][col] == 0:
            for rest in range(col, m+1):
                dp[1][rest] = 0
            break
        dp[1][col] = 1
    
    for row in range(2, n+1):
        for col in range(2, m+1):
            if dp[row][col] == 0:
                continue
            dp[row][col] = dp[row-1][col] + dp[row][col-1]

    answer = dp[n][m] % 1000000007
    return answer