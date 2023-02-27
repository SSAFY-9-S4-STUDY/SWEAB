import sys
from collections import deque
# input -> sys.stdin.readline 이걸로 시간초과 해결...
N, M, R = map(int, sys.stdin.readline().split())

adjacent_list = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    adjacent_list[n1].append(n2)
    adjacent_list[n2].append(n1)
for i in range(N+1):
    adjacent_list[i].sort()


queue=deque([R])
visited = [0]*(N+1)
visited[R] = 1
current_visited = 1
while queue:
    current_node = queue.popleft()
    for node in adjacent_list[current_node]:
        if visited[node]==0:
            queue.append(node)
            visited[node] = current_visited + 1
            current_visited = visited[node]

for i in range(1,N+1):
    print(visited[i])
