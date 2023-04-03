from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
vector = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1 ,-1)]

queue, cnt = deque(), 0
for r in range(N):
    for c in range(M):
        if arr[r][c]:
            queue.append((r, c))
            cnt += 1

ans = 0
while queue:
    tmp_cnt = 0
    for i in range(cnt):
        r, c = queue.popleft()
        for v in vector:
            nr, nc = r + v[0], c + v[1]
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
                queue.append((nr, nc))
                arr[nr][nc] = 1
                tmp_cnt += 1
    if tmp_cnt:
        ans += 1
        cnt = tmp_cnt

print(ans)