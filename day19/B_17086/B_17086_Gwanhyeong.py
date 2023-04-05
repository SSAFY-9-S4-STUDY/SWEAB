from collections import deque

DIRECTION = [(1,0), (1,-1), (0,-1),(-1,-1),
             (-1,0), (-1, 1), (0, 1), (1,1)]


def bfs():
    while q:
        current_x, current_y = q.popleft()
        current_visit = visited[current_x][current_y]
        for dx, dy in DIRECTION:
            nx = current_x + dx
            ny = current_y + dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = current_visit + 1
                q.append((nx,ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            q.append((i,j))
            visited[i][j] = 1
bfs()
print(max(map(max,visited))-1)