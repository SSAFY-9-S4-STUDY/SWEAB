import sys
sys.setrecursionlimit(10 ** 9)


def dfs(start):
    for next in arr[start]:
        if not visited[next]:
            visited[next] = start
            dfs(next)


N = int(sys.stdin.readline().rstrip())

arr = [[] for _ in range(N + 1)]

visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

dfs(1)

print(*visited[2:], sep='\n')