
def solution(n, s, a, b, fares):
    graph = [[float('INF')]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for fare in fares:
        c, d, f = fare
        graph[c][d] = graph[d][c] = f

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    ans = float('INF')
    for i in range(1, n+1):
        ans = min(ans, graph[s][i] + graph[i][a] + graph[i][b])

    return ans