from collections import deque

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

num = int(input())

lst = [list(map(int, list(input()))) for _ in range(num)]

visited = [[0 for _ in range(num)] for __ in range(num)]
rlt = []

for i in range(num):
    for j in range(num):
        if visited[i][j] == 0 and lst[i][j] == 1:
            visited[i][j] = 1
            temp = 0
            q = deque([(i, j)])
            while q:
                cur = q.popleft()
                temp += 1
                for di, dj in direction:
                    ni, nj = cur[0] + di, cur[1] + dj
                    if 0 <= ni < num and 0 <= nj < num and visited[ni][nj] == 0 and lst[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
            rlt.append(temp)
        visited[i][j] = 1


rlt.sort()
print(len(rlt), *rlt)