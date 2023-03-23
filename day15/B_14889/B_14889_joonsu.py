import sys
import math
sys.setrecursionlimit(100000)

def DFS(idx, count):
    global result
    if count == N//2:
        st = li = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    st += arr[i][j]
                elif not visited[i]+visited[j]:
                    li += arr[i][j]
        result = min(result, abs(st-li))

    for k in range(idx, N):
        if visited[k]:
            continue
        visited[k] = 1
        DFS(k+1, count+1)
        visited[k] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = math.inf
DFS(0, 0)
print(result)