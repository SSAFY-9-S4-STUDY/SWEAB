from collections import deque

def DFS(V):
    visited_DFS[V] = 1
    print(V, end=' ')
    for next in range(1, N+1):
        if arr[V][next] == 1 and visited_DFS[next] == 0:
            DFS(next)


def BFS(V):
    visited_BFS[V] = 1
    queue = deque([V])
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next in range(1, N+1):
            if arr[now][next] == 1 and visited_BFS[next] == 0:
                queue.append(next)
                visited_BFS[next] = 1


N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    arr[node1][node2] = 1
    arr[node2][node1] = 1

visited_DFS = [0] * (N+1)
visited_BFS = [0] * (N+1)

DFS(V)
print()
BFS(V)
