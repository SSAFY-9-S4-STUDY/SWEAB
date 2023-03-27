import sys
from collections import deque
input = sys.stdin.readline

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
arr = [list(map(int,  input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()
    if not q:
        ans = arr[i][j]
    for di, dj in direc:
        ni, nj = i + di, j + dj
        if 0 <= ni < N  and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j] + 1
            q.append((ni, nj))

for lst in arr:
    if 0 in lst:
        ans = -1
        break
else:
    ans -= 1

print(ans)