import sys
input = sys.stdin.readline
from collections import deque

def bfs(V, E, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    q = deque([R])
    visited[R] = 1  # 시작 정점 R을 방문 했다고 표시한다.
    count = 2

    while q:
        q.popleft()  # 큐 맨 앞쪽의 요소를 삭제한다.
        for i in E[R]:  # E(u) : 정점 u의 인접 정점 집합
            if not visited[i]:
                visited[i] = count  # 정점 v를 방문 했다고 표시한다.
                q.append(i)  # 큐 맨 뒤에 정점 v를 추가한다.
                count += 1


N, M, R = map(int, input().split())
visited = [0] * (N + 1)
E = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(N + 1):
    E[i].sort()

bfs(N, E, R)
for i in visited[1::]:
    print(i)
