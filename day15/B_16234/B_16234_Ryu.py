from collections import deque

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[0 for __ in range(N)] for _ in range(N)]
rlt = 0
while True:
    swi = 0
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and L <= abs(lst[i][j] - lst[ni][nj]) <= R and visited[ni][nj] == 0:
                        q = deque([(i, j)])
                        visited[i][j] = 1
                        change_lst = [(i, j)]
                        popul = lst[i][j]
                        while q:
                            cur = q.popleft()
                            for di, dj in direction:
                                ni, nj = cur[0] + di, cur[1] + dj
                                if 0 <= ni < N and 0 <= nj < N and L <= abs(lst[cur[0]][cur[1]] - lst[ni][nj]) <= R and visited[ni][nj] == 0:
                                    visited[ni][nj] = 1
                                    q.append((ni,nj))
                                    change_lst.append((ni, nj))
                                    popul += lst[ni][nj]

                        for ci, cj in change_lst:
                            lst[ci][cj] = popul // len(change_lst)

                        swi = 1
                        visited[i][j] = 1
                        break
    if swi == 0:
        break
    else:
        rlt += 1

print(rlt)
