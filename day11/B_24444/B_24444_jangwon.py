import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().rstrip().split())

arr = [[] for _ in range(N+1)]

visited = [0 for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

queue = deque([R])
visited[R] = 1
cnt = 1

for i in range(1, N + 1):
    arr[i].sort()

while queue:
    now = queue.popleft()

    for next in arr[now]:
        if not visited[next]:
            queue.append(next)
            cnt += 1
            visited[next] = cnt

print(*visited[1:], sep='\n')