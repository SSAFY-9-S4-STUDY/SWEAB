## 뭔가 풀 수 있을 거 같아서 이거는 일단 중간과정만 올리고 다시 올릴게요....ㅜ

def dfs(start, cnt):
    if not visited[start]:
        visited[start] = cnt

    for node in range(1, N + 1):
        if arr[start][node]:
            if visited[node]:
                return
            else:
                dfs(node, cnt + 1)

while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break
    # m만큼 간선을 나타내는 두 개의 정수가 주어진다.
    else:
        arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        visited = [0 for _ in range(N + 1)]  # 같은 트리인지 판별할 곳.

        for _ in range(M):
            s, e = map(int, input().split())
            arr[s][e] = arr[e][s] = 1
