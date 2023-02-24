import sys

N, M, R= map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
nodes = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

stk = [0] * M
top = 0
stk[top] = R
num = 1
while top != -1:
    cur = stk[top]
    top -= 1
    if visited[cur] == 0:
        visited[cur] = num
        num += 1

        for i in sorted(nodes[cur], reverse = 1):
            if visited[i] == 0:
                top += 1
                stk[top] = i

for i in range(1, N + 1):
    print(visited[i])