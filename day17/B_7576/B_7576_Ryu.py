import sys
input = sys.stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(N)]
already = set()
new = set()
total = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            new.add((i, j))
            total += 1
        elif lst[i][j] == 0:
            total += 1

rlt = 0
while True:
    already |= new
    temp = set()
    for i, j in new:
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in already and lst[ni][nj] == 0:
                temp.add((ni, nj))

    if not temp:
        break
    else:
        rlt += 1
        new = temp

if len(already) != total:
    rlt = -1

print(rlt)