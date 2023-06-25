from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    arr = [[] for _ in range(n + 1)]
    cost = [-1 for _ in range(n + 1)]
    cost[destination] = 0

    for s, e in roads:
        arr[s].append(e)
        arr[e].append(s)
    queue = deque([destination])

    while queue:
        x = queue.popleft()
        for node in arr[x]:
            if cost[node] == -1:
                queue.append(node)
                cost[node] = cost[x] + 1

    for source in sources:
        answer.append(cost[source])

    return answer