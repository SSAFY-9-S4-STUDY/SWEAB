# import sys
# sys.stdin = open("input.txt")
from collections import deque


def bfs(graph, start):
    q = deque([start])
    visited = []
    while q:
        i = q.popleft()
        if i not in visited:
            visited.append(i)
            q += graph[i]
    return visited

def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        i = stack.pop()
        if i not in visited:
            visited.append(i)
            stack += reversed(graph[i])
    return visited


graph = {}
n, m, start = map(int, input().split())
for i in range(1, n+1):
    graph[i] = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

d = dfs(graph, start)
b = bfs(graph, start)

print(' '.join(map(str, d)))
print(' '.join(map(str, b)))