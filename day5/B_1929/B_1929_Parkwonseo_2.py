# 현직자가 짠 코드입니다.

from math import sqrt

small, large = map(int, input().split())

maximum_value = int(sqrt(large) + 1)
dp = [0 for _ in range(large + 1)]

for i in range(2, maximum_value):
    if dp[i] == 1:
        continue
    # n = max(small // i, 2) * i
    # while n <= large:
    #     dp[n] = 1
    #     n += i
    for j in range(max(small // i, 2) * i, large + 1, i):
        dp[j] = 1

for i in range(max(small, 2), large + 1):
    if dp[i] == 0:
        print(i)
