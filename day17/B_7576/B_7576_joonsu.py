from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
result = -2
temp = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < M\
                and arr[new_x][new_y] == 0:
            arr[new_x][new_y] = arr[x][y] + 1
            queue.append([new_x, new_y])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            temp = 1
        result = max(result, arr[i][j])

if temp == 1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)