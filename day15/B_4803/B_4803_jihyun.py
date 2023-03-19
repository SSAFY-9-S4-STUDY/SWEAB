def dfs(node, directly):
    for connect_node in adjL[node]:
        if directly == connect_node:
            continue
        if visited[connect_node]:
            return 0

        visited[connect_node] = 1
        if dfs(connect_node, node) == 0:
            return 0
    return 1


tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    adjL = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    tree_num = 0
    for node in range(1, n+1):
        if not visited[node]:
            visited[node] = 1
            tree_num += dfs(node, 0)

    if tree_num == 0:
        ans = 'No trees.'
    elif tree_num == 1:
        ans = 'There is one tree.'
    else:
        ans = f'A forest of {tree_num} trees.'

    print(f'Case {tc}: {ans}')
    tc += 1
