def DFS(prev, node):
    visited[node] = 1
    for i in arr[node]:
        if i == prev:
            continue
        if visited[i]:
            return
        if not DFS(node, i):
            return
    return True

case = 0
while True:
    case += 1
    N, M = map(int, input().split())
    if not N and not M:
        break

    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    count = 0

    for _ in range(M):
        node1, node2 = map(int, input().split())
        arr[node1].append(node2)
        arr[node2].append(node1)

    for v in range(1, N+1):
        if not visited[v]:
            if DFS(0, v):
                count += 1

    if not count:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')