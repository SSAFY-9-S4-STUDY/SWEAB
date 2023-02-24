import sys

N, M, R= map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
nodes = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

q = [0] * (M + 1)
front = -1
rear = -1

rear += 1
q[rear] = R

num = 1
while front != rear:
    front += 1
    cur = q[front]

    if visited[cur] == 0:
        visited[cur] = num
        num += 1

        for i in sorted(nodes[cur]):
            if visited[i] == 0:
                rear += 1
                q[rear] = i

for i in range(1, N + 1):
    print(visited[i])