def find_union(lst, total, idx, n):
    while idx != n:
        x, y = lst[idx]
        for v in vector:
            nx, ny = x + v[0], y + v[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
              num_p1, num_p2 = countries[x][y], countries[nx][ny] 
              if L <= abs(num_p1 - num_p2) <= R:
                  lst.append((nx,ny))
                  visited[nx][ny] = 1
                  total += num_p2
                  n += 1
        idx += 1
    if n > 1:
        unions.append(lst)
        mean_p.append(total//n)


N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

vector = [(1, 0), (-1, 0), (0, 1), (0,-1)]
cnt = 0

while True:
    
    visited = [[0]*N for _ in range(N)]
    unions = []
    mean_p = []

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = 1
                find_union([(r,c)], countries[r][c], 0, 1)

    if not unions:
        break
    
    for union, num in zip(unions,mean_p):
        for x, y in union:
            countries[x][y] = num
    
    cnt += 1

print(cnt)

