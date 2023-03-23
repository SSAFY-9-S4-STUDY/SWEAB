def DFS(i):
    global dfs_res, visited_d 
    if not visited_d[i]:
        dfs_res.append(i)
        visited_d[i] = 1
    else:
        return 
    for node in nodes[i]:
        DFS(node)

def BFS(i):
    global bfs_res, visited_b
    q=[i]
    while q:
        x = q.pop(0)
        if not visited_b[x]:
            bfs_res.append(x)
            visited_b[x] = 1
        for node in nodes[x]:
            if not visited_b[node]:
                q.append(node)

N, M, V = map(int,input().split())
nodes = [[] for _ in range(N+1)]  # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for _ in range(M):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for node in nodes:
    node.sort()

dfs_res = []
visited_d = [0]*(N+1)
DFS(V)

visited_b = [0]*(N+1)
bfs_res = []
BFS(V)

print(*dfs_res)
print(*bfs_res)