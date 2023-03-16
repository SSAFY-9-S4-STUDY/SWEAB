delta = [(1, 0), (-1, 0 ), (0, 1), (0, -1)]

n = int(input())

table = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

# 순회로 visited는 0이면서 table은 1인 좌표를 찾아내고, visited에 표시 및 dfs 전개.

count = 1

for y in range(n):
    for x in range(n):
        if table[y][x] == '1' and visited[y][x] == 0:
            visited[y][x] = count
            stack = [(x, y)]
            while stack:
                now = stack.pop()
                for d in delta:
                    nx, ny = now[0] + d[0], now[1] + d[1]
                    if 0 <= nx < n and 0 <= ny < n and table[ny][nx] == '1' and visited[ny][nx] == 0:
                        visited[ny][nx] = count
                        stack.append((nx, ny))
            count += 1

house = []
for i in range(1, count):  # count 가 +1 되어있음
    cnt = 0
    for y in range(n):
        for x in range(n):
            if i == visited[y][x]:
                cnt += 1
    house.append(cnt)
house.sort()

print(count - 1)
for i in range(count - 1):
    print(house[i])