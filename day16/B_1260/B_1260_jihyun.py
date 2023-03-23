def dfs(st):
    visited[st] = 1
    print(st, end=' ')
    if adjL[st]:
        for next in adjL[st]:
            if visited[next]:
                continue
            else:
                dfs(next)
    else:
        return


def bfs(st):
    # dfs 함수 먼저 실행하면서 방문한 곳은 1, 방문하지 않은 곳은 0으로 값이 매핑되어 있음
    # visited 초기화를 안시킬 거기 때문에 1이 방문하지 않은 곳이고 방문하면 0으로 바꿔줄거임
    visited[st] = 0
    q = [st]
    while q:
        node = q.pop(0)
        print(node, end=' ')
        for next in adjL[node]:
            if visited[next]:
                q.append(next)
                visited[next] = 0
    return


N, M, V = map(int, input().split())
adjL = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    adjL[n1].append(n2)
    adjL[n2].append(n1)

# 숫자가 작은 곳부터 방문하기 위해 연결된 node가 2개 이상이면 sort()
for connect_nodes in adjL:
    if len(connect_nodes) > 1:
        connect_nodes.sort()

visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)
