from collections import deque

def dfs(start):
    if not nodes[start]:
        return
    else:
        for i in range(len(nodes[start])):
            if nodes[start][i] not in visited_dfs:
                visited_dfs.append(nodes[start][i])
                dfs(nodes[start][i])


def bfs(start):
    while queue:
        now = queue.popleft()
        if nodes[now]:
            for i in range(len(nodes[now])):
                if nodes[now][i] not in visited_bfs:
                    visited_bfs.append(nodes[now][i])
                    queue.append(nodes[now][i])

N, M, V = map(int, input().split())

# index로 찾아갈거야
nodes = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
    nodes[s].sort()
    nodes[e].sort()

queue = deque()

visited_dfs = [V]
visited_bfs = [V]
queue.append(V)

dfs(V)
bfs(V)
print(*visited_dfs)
print(*visited_bfs)