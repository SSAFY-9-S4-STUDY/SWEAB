import sys
from collections import deque

vertex, edge, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

queue = deque([start])
visited = [0] * (vertex + 1)
count = 1
visited[start] = count

while queue:
    now = queue.popleft()
    for next_v in sorted(graph[now]):
        if not visited[next_v]:
            queue.append(next_v)
            count += 1
            visited[next_v] = count

for idx in range(1, vertex + 1):
    print(visited[idx])