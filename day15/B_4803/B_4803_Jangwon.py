## 뭔가 풀 수 있을 거 같아서 이거는 일단 중간과정만 올리고 다시 올릴게요

def dfs(end, start):
    global status
    if not visited[start]:
        visited[start] = end

    for node in range(1, N + 1):
        if arr[start][node]:
            if node == end:
                continue
            if visited[node]:
                status = False
                return
            if not visited[node]:
                dfs(start, node)

tc = 0
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


        ans = 0
        for i in range(1, N + 1):
            if not visited[i]:
                status = True
                dfs(i, i)
                if status:
                    ans += 1

        tc += 1
        if ans > 1:
            print(f'Case {tc}: A forest of {ans} trees.')
        elif ans == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: No trees.')