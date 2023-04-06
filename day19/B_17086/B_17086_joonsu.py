from collections import deque

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            queue.append((i,j))

while queue:
    y, x = queue.popleft()
    for k in range(8):
        new_y = y + dy[k]
        new_x = x + dx[k]
        if 0 <= new_y < N and 0 <= new_x < M\
                and arr[new_y][new_x] == 0:
            queue.append((new_y, new_x))
            arr[new_y][new_x] = arr[y][x] + 1

for i in range(N):
    result = max(result, max(arr[i]))

print(result-1)
