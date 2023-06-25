from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    visited = [-1 for _ in range(n+1)]
    print(visited)
    q = deque([destination])
    visited[destination] = 0
    while q:
        now = q.popleft()
        distance = visited[now]
        for next in graph[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = distance + 1

    answer = []
    for i in sources:
        answer.append(visited[i])
    return answer
print(solution(3,[[1, 2], [2, 3]], [2,3], 1))