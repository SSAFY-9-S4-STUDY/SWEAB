from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    union = [(x, y)]
    united = [pop[x][y]]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()
        for i in range(4):
            new_x = a + dx[i]
            new_y = b + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if L <= abs(pop[new_x][new_y] - pop[a][b]) <= R and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
                    union.append((new_x, new_y))
                    united.append(pop[new_x][new_y])
    if len(union) == 1:
        return 0

    cnt = 0
    for i in range(len(united)):
        cnt += united[i]

    average = cnt // len(union)
    for x, y in union:
        pop[x][y] = average

    return 1


N, L, R = map(int, input().split())
pop = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    visited = [[0] * N for _ in range(N)]

    move = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                move += bfs(i, j)

    if move == 0:
        break

    ans += 1

print(ans)