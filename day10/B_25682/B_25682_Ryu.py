import sys

N, M, K = map(int, sys.stdin.readline().split())
sr = [[0 for _ in range(M + 1)] for _ in range(N+1)]
ans = K ** 2

for i in range(N):
    a = sys.stdin.readline().rstrip()
    for j in range(M):
        sr[i + 1][j + 1] = (((i + j) % 2 == 0) ^ (a[j] == 'W')) + sr[i][j + 1] + sr[i + 1][j] - sr[i][j]

ans = []
for i in range(K - 1, N):
    for j in range(K - 1, M):
        ans.append(sr[i + 1][j + 1] - sr[i + 1][j - K + 1] - sr[i - K + 1][j + 1] + sr[i - K + 1][j - K + 1])

print(min(K ** 2 -max(ans), min(ans)))

# 주어진 나무 판자를 lst에 받아오려고 했으나