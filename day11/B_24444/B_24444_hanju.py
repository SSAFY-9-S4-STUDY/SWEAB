import sys
from collections import deque

N, M, start = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

route = deque([start])
cnt = 1
order = [0]*N

while route:
    tmp = route.popleft()
    if not order[tmp-1]:
        order[tmp-1] = cnt
        cnt += 1
        route.extend(sorted(graph[tmp]))

for i in order:
    print(i)
