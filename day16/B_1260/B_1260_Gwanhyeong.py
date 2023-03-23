def dfs(n):
    visited[n] = 1
    dfs_list.append(n)
    for i in node[n]:
        if visited[i] == 0:
            dfs(i)


def bfs(n):
    visited[n] = 1
    bfs_list.append(n)
    q = [n]
    while q:
        for i in node[q.pop(0)]:
            if visited[i] == 0:
                visited[i] = 1
                bfs_list.append(i)
                q.append(i)
    

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dfs_list = []
bfs_list = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    node[n1].append(n2)
    node[n2].append(n1)

for i in range(N+1):
    node[i].sort()

dfs(V)
for i in range(N+1):
    visited[i] = 0

bfs(V)

for i in dfs_list:
    print(i, end=" ")
print()
for j in bfs_list:
    print(j, end=" ")