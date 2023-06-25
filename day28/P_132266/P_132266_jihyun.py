from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distances = {i: 500000 for i in range(1, n+1)}
    distances[destination] = 0

    queue = deque([destination])
    while queue:
        temp = queue.popleft()
        for connect in graph[temp]:
            if distances[connect] == 500000:
                distances[connect] = distances[temp] + 1
                queue.append(connect)

    answer = []
    for source in sources:
        if distances[source] == 500000:
            answer.append(-1)
        else:
            answer.append(distances[source])

    return answer