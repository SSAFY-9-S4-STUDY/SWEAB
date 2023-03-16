def find_apar():
    q = [[i, j]]
    cnt = 1
    arr[i][j] = 0
    while q:
        r, c = q.pop(0)
        for di, dj in direc:
            ni, nj = r + di, c + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                cnt += 1
                q.append([ni, nj])
                arr[ni][nj] = 0
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            ans.append(find_apar())

ans.sort()
print(len(ans), *ans, sep='\n')