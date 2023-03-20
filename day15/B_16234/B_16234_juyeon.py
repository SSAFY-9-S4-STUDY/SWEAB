def BFS(x, y):
    global cnt, visited, peoples, flag
    dif = [(0,1), (1,0), (-1,0), (0,-1)]

    q = [(x, y)]
    res = [(x, y)]
    while q:
        x, y = q.pop(0)        
        visited[x][y] = 1
        num = peoples[x][y]
        for di in dif:
            nx = x + di[0]
            ny = y + di[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(peoples[nx][ny] - num) <= R:
                    visited[nx][ny] = 1
                    flag = False
                    res.append((nx, ny))
                    q.append((nx, ny))

    k = 0
    for i, j in res:
        k += peoples[i][j]
    k //= len(res)
    for i, j in res:
        peoples[i][j] = k

N, L, R = map(int,input().split())
peoples = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)
    if flag:
        break
    cnt += 1

print(cnt)