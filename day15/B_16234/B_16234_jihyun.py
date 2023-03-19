def union():
    sum_popul = 0
    open = []

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0

for i in range(N):
    for j in range(N):
        for di, dj in direc:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and L <= abs(population[i][j]-population[ni][nj]) <= R:
                population

    if sum_popul == 0:
        break
    else:
        ans += 1
        new_p = sum_popul // len(open)
        for i, j in open:
            population[i][j] = new_p

print(ans)

