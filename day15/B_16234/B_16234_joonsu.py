from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    visited = [[0]*N for _ in range(N)]
    flag = True

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue = deque([(i, j)])
                visited[i][j] = 1

                tmp = [(i, j)]
                while queue:
                    x, y = queue.pop()
                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]
                        if 0 <= new_x < N and 0 <= new_y < N\
                            and visited[new_x][new_y] == 0:
                            if L <= abs(arr[x][y] - arr[new_x][new_y]) <= R:
                                queue.appendleft((new_x,new_y))
                                visited[new_x][new_y] = 1
                                tmp.append((new_x, new_y))

                if len(tmp) > 1:
                    flag = False
                    avg = sum([arr[m][n] for m, n in tmp]) // len(tmp)
                    for m, n in tmp:
                        arr[m][n] = avg
    if flag:
        break
    result += 1

print(result)