import sys

N, M, start = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

route = [start]
cnt = 1
order = [0]*N

while route:
    tmp = route.pop()
    if not order[tmp-1]:
        order[tmp-1] = cnt
        cnt += 1
        route.extend(sorted(graph[tmp], reverse=True))

for i in range(N):
    print(order[i])