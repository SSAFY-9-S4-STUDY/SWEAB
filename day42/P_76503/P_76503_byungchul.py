from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, a, graph, visited):
    visited[node] = True
    num_of_operations = 0

    for next_node in graph[node]:
        if not visited[next_node]:
            # 재귀적으로 리프 노드까지 탐색하고, 탐색하며 가중치 조정 횟수 누적
            operations = dfs(next_node, a, graph, visited)
            a[node] += a[next_node]
            num_of_operations += abs(a[next_node]) + operations

    return num_of_operations

def solution(a, edges):
    if sum(a) != 0:  # 모든 노드의 가중치 합이 0이 아니면 해결 불가
        return -1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # DFS
    visited = [False] * len(a)

    # DFS 실행 및 연산 횟수 계산
    num_of_operations = dfs(0, a, graph, visited)

    return num_of_operations

