from collections import deque

N = int(input())

houses = [list(map(int, input())) for _ in range(N)]

mark = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

visited = [[0 for _ in range(N)] for _ in range(N)]

queue = deque()
for j in range(N):
    for i in range(N):
        visited[j][i] = 1
        if houses[j][i] == 1:
            queue.append([j, i])
            cnt = 0
            while queue:
                now = queue.popleft()
                cnt += 1
                houses[now[0]][now[1]] = 0
                visited[now[0]][now[1]] = 1
                for k in range(4):
                    ny, nx = now[0] + dy[k], now[1] + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and [ny, nx] not in queue:
                        if houses[ny][nx] == 1:
                            queue.append([ny, nx])
                        else:
                            visited[ny][nx] = 1

            mark.append(cnt)
mark.sort()
print(len(mark))
print(*mark, sep='\n')