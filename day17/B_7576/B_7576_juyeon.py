from collections import deque
def BFS():
    global q, basket, max_dis
    dif = [(0,1),(1,0),(0,-1),(-1,0),]
    
    while q:
        x, y = q.popleft()
        for di in dif:
            nx = x + di[0]
            ny = y + di[1]
            if 0 <= nx < N and 0 <= ny < M and basket[nx][ny] == 0:
                q.append((nx, ny))
                basket[nx][ny] = basket[x][y] + 1
                idx = 1


M, N = map(int,input().split())
basket = [list(map(int,input().split())) for _ in range(N)]

q = deque([])
for i in range(N):
    for j in range(M):
        if basket[i][j] == 1:
            q.append((i,j))

BFS()


max_dis = 0
for i in range(N):
    for j in range(M):
        if basket[i][j] == 0:
            print(-1)
            exit()
        if basket[i][j] > max_dis:
            max_dis = basket[i][j]

print(max_dis-1)