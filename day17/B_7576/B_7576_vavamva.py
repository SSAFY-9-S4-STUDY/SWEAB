# 토마토 문제

# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈칸
# "1"에 인접(상하좌우)한 "0" 들은 하루 뒤 "1"이 됨

import sys
from collections import deque
input = sys.stdin.readline
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start):
    queue = deque(start)
    while queue:
        now = queue.popleft()
        for d in directions:
            nx, ny = now[0] + d[0], now[1] + d[1]
            if 0 <= nx < col and 0 <= ny < row and box[ny][nx] == 0:
                box[ny][nx] = box[now[1]][now[0]] + 1
                queue.append((nx, ny))


col, row = map(int, input().split())
box = []
tomato = []
minus = 0
for y in range(row):
    box.append(list(map(int, input().split())))
    for x in range(col):
        if box[y][x] == 1:
            tomato.append((x, y))
        elif box[y][x] == -1:
            minus += 1

bfs(tomato)

flag = True
max_day = 0
for line in box:
    max_day = max(max(line), max_day)
    for elem in line:
        if elem == 0:
            flag = False
            break

if flag:
    print(max_day - 1)
else:
    print(-1)
