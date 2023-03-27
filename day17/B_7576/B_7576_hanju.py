import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = N * M

# 익은 토마토 위치와 개수 찾기
q, cnt = deque(), 0
for r in range(N):
    for c in range(M):
        if tomatoes[r][c] == 1:
            q.append((r,c))
            cnt += 1

# bfs로 최소 탐색 주기 찾기
vector, ans = [(1,0), (-1,0), (0,1), (0,-1)], 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        for v in vector:
            nr, nc = r + v[0], c + v[1]
            if 0 <= nr < N and 0 <= nc < M and not tomatoes[nr][nc]:
                q.append((nr, nc))
                tomatoes[nr][nc] = 1
    ans += 1

print(-1 if 0 in sum(tomatoes,[]) else ans-1)
                