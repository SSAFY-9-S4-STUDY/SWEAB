import sys
from collections import deque
# 이건 시간초과...
N, M, R = map(int, sys.stdin.readline().split())

adjacent_list = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int,sys.stdin.readline().split())
    adjacent_list[n1].append(n2)
    adjacent_list[n2].append(n1)
for i in range(N+1):
    adjacent_list[i].sort(reverse=True)
q = deque([R])
visited = [0] * (N+1)
visited[R] = 1
stack = []
while q:
    current_node = q.pop()
    stack.append(current_node)
    for next in adjacent_list[current_node]:
        if visited[next]==0:
            q.append(next)
            visited[next] = 1

for i in range(1,N+1):
    if i in stack:
        print(stack.index(i)+1)
    else:
        print(0)

