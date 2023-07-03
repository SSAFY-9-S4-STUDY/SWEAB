import sys
sys.setrecursionlimit(1000000)

def solution(n, roads, sources, destination):
    # 그래프 순회를 위한 bfs 함수
    def find_shortest(queue, distance):
        tmp = []
        for q in queue:
            for nod in edges[q]:
                if shortest_distance[nod] < 0:
                    tmp.append(nod)
                    shortest_distance[nod] = distance
        if tmp:
            find_shortest(tmp, distance + 1)

    # roads를 통해 그래프 표시하기
    edges = {i:[] for i in range(1, n+1)}
    for nod1, nod2 in roads:
        edges[nod1].append(nod2)
        edges[nod2].append(nod1)

    # bfs로 그래프를 순회하며 destination과의 노드별로 최단거리 측정
    shortest_distance = [-1]*(n+1)
    shortest_distance[destination] = 0
    find_shortest([destination], 1)

    return [shortest_distance[i] for i in sources]


print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
