def next_house(row, col):
    global houses
    stack, cnt = [(row, col)], 0
    while stack:
        x, y = stack.pop()
        cnt += 1
        for v in vector:
            nx, ny = x + v[0], y + v[1]
            if 0 <= nx < N and 0 <= ny < N and houses[nx][ny] == 1:
                stack.append((nx, ny))
                houses[nx][ny] = 0
    return cnt

N = int(input())
houses = [list(map(int, input())) for _ in range(N)]

vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = []
for r in range(N):
    for c in range(N):
        if houses[r][c] == 1:
            houses[r][c] = 0
            ans.append(next_house(r,c))

print(len(ans))
for i in sorted(ans):
    print(i)