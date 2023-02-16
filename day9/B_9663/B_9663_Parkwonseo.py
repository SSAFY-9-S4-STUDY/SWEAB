def queen(arr, x, y, num):  # 퀸의 방향대로 1 입력

    i = 0
    # x 양방향, 음방향 / y 양방향, 음방향 / xy
    while x + i < num:
        arr[y][x + i] = 1
        if y + i < num:
            arr[y + i][x + i] = 1
        if y - i > 0:
            arr[y - i][x + i] = 1
        i += 1
    i = 0
    while x - i >= 0:
        arr[y][x - i] = 1
        if y + i < num:
            arr[y + i][x - i] = 1
        if y - i > 0:
            arr[y - i][x - i] = 1
        i += 1
    i = 0
    while y + i < num:
        arr[y + i][x] = 1
        i += 1
    i = 0
    while y - i >= 0:
        arr[y - i][x] = 1
        i += 1


n = int(input())
table = [[0] * n for _ in range(n)]
ans = 0

for v in range(n):
    n_queen = 1
    visited = [[] for _ in range(n)]
    queen(table, v, 0, n)
    for i in range(1, n):
        for j in range(n):
            if (i, j) not in visited[v] and table[i][j] == 0:
                visited[v].append((i, j))
                queen(table, j, i, n)
                break
    table = [[0] * n for _ in range(n)]
    if n_queen == n:
        ans += 1

print(ans)
