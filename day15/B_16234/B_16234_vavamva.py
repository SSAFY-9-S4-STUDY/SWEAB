# 인구이동
# import pprint
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

delta = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def dfs(x, y):
    stack = [(x, y)]
    population = 0
    country = 0
    union = []
    # print(f"dfs 시작: {x, y}")
    while stack:
        now = stack.pop()
        union.append(now)
        population += land[now[1]][now[0]]
        country += 1
        for d in delta:
            nx, ny = now[0] + 2 * d[0], now[1] + 2 * d[1]
            # print(nx, ny)
            if 0 <= nx < 2 * n and 0 <= ny < 2 * n:
                # print(land[ny - d[1]][nx - d[0]], visited[ny][nx])
                if land[ny - d[1]][nx - d[0]] and visited[ny][nx] == 0:
                    stack.append((nx, ny))
                    visited[ny][nx] = 1

    # print(f"dfs 끝: {union}")
    for ux, uy in union:
        land[uy][ux] = population // country


n, low_limit, high_limit = map(int, input().split())

# 각 통로를 표시하는 배열을 새로 만들어보자

land = [[False] * ((2 * n) - 1) for _ in range((2 * n) - 1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        land[2 * i][2 * j] = tmp[j]

count = 0
while True:
    flag = True
    for y in range(n):
        for x in range(n):
            if 2 * (y + 1) < 2 * n - 1 and low_limit <= abs(land[2 * y][2 * x] - land[2 * (y + 1)][2 * x]) <= high_limit:
                flag = False
                land[2 * y + 1][2 * x] = True
            if 2 * (x + 1) < 2 * n - 1 and low_limit <= abs(land[2 * y][2 * x] - land[2 * y][2 * (x + 1)]) <= high_limit:
                flag = False
                land[2 * y][2 * x + 1] = True
    # pprint.pprint(land)

    if flag:
        break

    # pprint.pprint(land)

    # 인구 이동 시작
    visited = [[0] * (2 * n - 1) for _ in range(2 * n - 1)]
    for i in range(n):
        for j in range(n):
            if visited[2 * i][2 * j] == 0:
                visited[2 * i][2 * j] = 1
                dfs(2 * j, 2 * i)

    # 인구 이동 끝
    count += 1
    # pprint.pprint(visited)

    for y in range(2 * n - 1):
        if y % 2:
            for x in range(2 * n - 1):
                land[y][x] = False
        else:
            for x in range(1, 2 * n - 1, 2):
                land[y][x] = False

# pprint.pprint(land)
print(count)
