from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1
    return visited
    

def solution(n, roads, sources, destination):
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)  
    
    visited = bfs(graph, destination, visited)

    ans = []
    for i in sources:
        ans.append(visited[i])
    
    return ans