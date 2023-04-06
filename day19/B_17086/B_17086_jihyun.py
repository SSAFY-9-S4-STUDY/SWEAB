N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

locations = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            locations.append([i, j])

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            continue
        safe_distance = N + M
        for shark in locations:
            diff_x = abs(shark[0] - i)
            diff_y = abs(shark[1] - j)
            safe_distance = min(safe_distance, max(diff_x, diff_y))
        else:
            ans = max(ans, safe_distance)

print(ans)