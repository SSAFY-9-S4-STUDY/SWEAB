## 또 Googling

from collections import deque
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()
DIRECTION = ((-1,0),(1,0),(0,-1),(0,1))

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for dx, dy in DIRECTION:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]==0:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx,ny))

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)