import sys
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, sys.stdin.readline().rstrip().split())

arr = [[] for _ in range(N + 1)]

visited = [0 for _ in range(N + 1)]
ans = 1

for i in range(1, N + 1):
    arr[i].sort()

def dfs(start):
    global ans
    visited[start] = ans

    for next in arr[start]:
        if not visited[next]:
            ans += 1
            dfs(next)


for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    arr[n1] = n2
    arr[n2] = n1

dfs(R)

print(*visited[1:], sep='\n')