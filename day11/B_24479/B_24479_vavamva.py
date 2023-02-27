"""
1. 무방향 그래프.
2. 모든 간선의 가중치는 같다.
3. 깊이 우선 탐색(dfs)를 이용하여 노드를 방문한다.
4. 대신 2와 3 에서 인접 정점을 오름차순으로 방문한다.
그 방문 순서를 출력하라.
"""

vertex, edge, start = map(int, input().split())

# 양방향 간선임을 잊지 말자
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

stack = [start]
visited = [0] * (vertex + 1)
count = 0
while stack:
    now = stack.pop()
    if not visited[now]:
        count += 1
        visited[now] = count
    for next_v in sorted(graph[now], reverse= True):
        if not visited[next_v]:
            stack.append(next_v)

for i in range(1, vertex + 1):
    print(visited[i])
