from collections import deque

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

# 델타방향검색
dy = [0, 1, 0, -1]  # 우하좌상
dx = [1, 0, -1, 0]

queue = deque()

# 익은 토마토 찾기
for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            queue.append([j, i])
            visited[j][i] = 1

# 탐색시작
while queue:
    now = queue.popleft()
    days = visited[now[0]][now[1]]

    for k in range(4):
        ny, nx = now[0] + dy[k], now[1] + dx[k]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = days + 1
            if not arr[ny][nx]:
                arr[ny][nx] = 1
                queue.append([ny, nx])
            elif arr[ny][nx] == -1:
                visited[ny][nx] = 1

if sum(arr, []).count(0):
    ans = -1
else:
    ans = max(sum(visited, [])) - 1
print(ans)