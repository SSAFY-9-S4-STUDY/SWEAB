# 구글링의 힘을 받았습니당#

import sys

(N, K) = map(int, sys.stdin.readline().split())
item = [[0, 0]]
for i in range(1, N + 1):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])


# 시간초과 메모리초과 계속된 코드....#
# import sys
# sys.setrecursionlimit(10 ** 5)
#
# def dfs(weight, value, depth):
#     global ans
#
#     if weight > K:
#         return
#
#     if ans < value:
#         ans = value
#
#     if depth == N:
#         return
#
#     dfs(weight + items[depth][0], value + items[depth][1], depth + 1)
#     dfs(weight, value, depth + 1)
#
#
# N, K = map(int, input().split())
#
# items = []
# for _ in range(N):
#     W, V = map(int, input().split())
#     items.append([W, V])
#
# ans = 0
# dfs(0, 0, 0)
#
# print(ans)