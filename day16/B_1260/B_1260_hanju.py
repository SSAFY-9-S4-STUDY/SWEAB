import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

g = [[] for i in range(N+1)]

for _ in range(M):
    e1, e2 = map(int, sys.stdin.readline().split())
    g[e1].append(e2)
    g[e2].append(e1)

visited_dfs = [0 for i in range(N+1)]
visited_bfs = [0 for i in range(N+1)]
stack, queue = [V], deque([V])

ans_dfs = []
while stack:
    tmp = stack.pop()
    if not visited_dfs[tmp]:
        ans_dfs.append(tmp)
        visited_dfs[tmp] = 1
        for i in sorted(g[tmp], reverse=True):
            stack.append(i)

ans_bfs = []
while queue:
    tmp = queue.popleft()
    if not visited_bfs[tmp]:
        ans_bfs.append(tmp)
        visited_bfs[tmp] = 1
        for i in sorted(g[tmp]):
            queue.append(i)

print(*ans_dfs)
print(*ans_bfs)