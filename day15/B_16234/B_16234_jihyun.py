# 테케 하나 계속 틀리는데 일단 낼게요..
# 하 화난다..
# 몰라 내일의 내가 디버깅하겠지^^


def union(r, c, q):
    sum_popul = population[r][c]
    open = [[r, c]]
    while q:
        r, c = q.pop(0)
        visited[r][c] = 1
        sum_popul += population[r][c]
        open.append([r, c])
        for dr, dc in direc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not (visited[nr][nc]) and L <= abs(population[r][c] - population[nr][nc]) <= R:
                q.append([nr, nc])

    new_p = sum_popul // len(open)
    for r, c in open:
        population[r][c] = new_p

    return population


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0

while True:
    visited = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not(visited[i][j]):
                visited[i][j] = 1
                q = []
                for di, dj in direc:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and not(visited[ni][nj]) and L <= abs(population[i][j]-population[ni][nj]) <= R:
                        q.append([ni, nj])
                        visited[ni][nj] = 1
                if q:
                    population = union(i, j, q)
                    flag = True

    if flag:
        ans += 1
    else:
        break

print(ans)
