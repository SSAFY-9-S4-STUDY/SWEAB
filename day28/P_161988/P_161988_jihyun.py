def solution(sequence):
    n = len(sequence)
    
    for even_idx in range(1, n, 2):
        sequence[even_idx] *= -1


    # 이거 왜 안되는지 알려줄 멋쟁이 찾아요
    # dp = [0] * n
    # dp[0] = sequence[0]
    
    # for i in range(1, n):
    #     num = sequence[i]
    #     if abs(num) > abs(num + dp[i-1]):
    #         dp[i] = num
    #     else:
    #         dp[i] = num + dp[i-1]
            
    # answer = abs(max(dp, key=abs))
    
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sequence[0]
    dp[1][0] = sequence[0]
    
    for i in range(1, n):
        num = sequence[i]
        dp[0][i] = min(num, num + dp[0][i-1])
        dp[1][i] = max(num, num + dp[1][i-1])
    
    mini = abs(min(dp[0]))
    maxi = max(dp[1])
    
    return max(mini, maxi)