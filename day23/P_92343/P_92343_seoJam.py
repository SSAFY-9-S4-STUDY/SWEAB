from collections import defaultdict


def solution(info, edges):

    def dfs(node, sheeps, wolves, near):
        # [1] 양 최대값 갱신
        global answer, visited
        answer = max(answer, sheeps)
        # [2] 다음 노드로 넘어갈 수 있는지 판단
        if sheeps <= wolves or node not in tree:  # 늑대가 양보다 많거나 leaf 노드일 때
            return
        # [3] 다음 노드로 넘어가기
        near = list(set(near + tree[node]))
        print(near)
        for next in near:
            if not visited[next]:
                visited[next] = 1
                if info[node]:
                    dfs(next, sheeps, wolves + 1, near)
                else:
                    dfs(next, sheeps + 1, wolves, near)
                visited[next] = 0


    global answer, visited
    answer = 0
    visited = [0] * len(info)

    # 트리 정보 정리
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])

    dfs(0, 1, 0, [0])
    return answer



print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))

# def dfs(node, sheep, wolf, nodes, visited):
#     global result, is_wolf, adj
#     n_nodes = list(set(nodes + adj[node]))
#     if sheep <= wolf or not n_nodes:
#         return
#     for new_node in n_nodes:
#         if not visited[new_node]:
#             visited[new_node] = 1
#             if is_wolf[new_node] == 0:
#                 dfs(new_node, sheep+1, wolf, n_nodes, visited)
#             else:
#                 dfs(new_node, sheep, wolf+1, n_nodes, visited)
#             visited[new_node] = 0
#     result = max(result, sheep)
#
# def solution(info, edges):
#     global result, is_wolf, adj
#     is_wolf = info
#     result = 1
#     adj = [[] for _ in range(len(info))]
#     visited = [0 for _ in range(len(info))]
#     for i, j in edges:
#         adj[i].append(j)
#     visited[0] = 1
#     dfs(0, 1, 0, [0], visited)
#     return result