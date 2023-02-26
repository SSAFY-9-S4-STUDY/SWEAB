import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def DFS(r):
    global count
    visited[r] = count
    arr[r].sort()
    for i in arr[r]:
        if visited[i] == 0:
            count += 1
            DFS(i)


N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

count = 1
DFS(R)

temp = visited[1:]
for i in temp:
    print(i)