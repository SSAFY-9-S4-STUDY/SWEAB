def dfs(node):
    stack = [node]
    visited = [0] * (vertex + 1)
    result = []
    while stack:
        now = stack.pop()
        # print(f' now: {now} ')
        if graph.get(now) and visited[now] == 0:
            visited[now] = 1
            for key in sorted(graph[now], reverse=True):
                if visited[key] == 0:
                    # print(key)
                    stack.append(key)
            result.append(now)

    return result


def bfs(node):
    queue = [node]
    visited = [0] * (vertex + 1)
    visited[queue[0]] = 1
    result = []
    while queue:
        now = queue.pop(0)
        result.append(now)
        if graph.get(now):
            for key in sorted(graph[now]):
                if visited[key] == 0:
                    queue.append(key)
                    visited[key] = 1
    return result


vertex, edges, start = map(int, input().split())

graph = dict()
for _ in range(edges):
    parent, child = map(int, input().split())
    if graph.get(parent):
        graph[parent].append(child)
    else:
        graph[parent] = [child]
    if graph.get(child):
        graph[child].append(parent)
    else:
        graph[child] = [parent]

if dfs(start):  # bfs와는 다르게 result에 elem이 추가될 때 조건이 필요함.
    print(*dfs(start))
else:
    print(start)

print(*bfs(start))