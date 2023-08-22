def solution(temperature, t1, t2, a, b, onboard):
    # 범위가 -10~40 이므로 0이상의 정수로 바꾸자
    temperature += 10
    t1 += 10
    t2 += 10
    start, end = min(t1, temperature), max(t2, temperature)
    time = len(onboard)
    MAX_ENERGY = 100 * time
    # dp[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    dp = [[MAX_ENERGY for _ in range(51)] for _ in range(time)]
    dp[0][temperature] = 0
    flag = 1
    if temperature > t2:
        flag = -1
    
    for i in range(1, time):
        for j in range(51):
            arr = [MAX_ENERGY]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                if 0 <= j + flag <= 50:
                    arr.append(dp[i-1][j+flag])
                if j==temperature:
                    arr.append(dp[i-1][j])
                if 0<= j-flag<=50:
                    arr.append(dp[i-1][j-flag] + a)
                if t1 <= j <= t2:
                    arr.append(dp[i-1][j] + b)
                dp[i][j] = min(arr)
    
    answer = min(dp[len(onboard)-1])
    return answer