import heapq
def solution(n, s, a, b, fares):

    def dikstra(start):
        result = [float('INF') for _ in range(n+1)]
        result[start] = 0
        q = []
        heapq.heappush(q, (result[start], start))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                if result[fu] > result_x + fw:
                    result[fu] = result_x + fw
                    heapq.heappush(q, ([result[fu], fu]))
        return result
    
    answer = 200000001
    graph = [[] for _ in range(n+1)]
    for n1, n2, fee in fares:
        graph[n1].append((n2, fee))
        graph[n2].append((n1, fee))

    # 각 노드에서 다른 노드까지의 최단거리를 구한 dikstra(i)
    distance = [[]]
    for i in range(1, n+1):
        distance.append(dikstra(i))
    
    # 이를 이용해서 임의의 중간노드 i에 대해 금액(s~i)+금액(i~a)+금액(i~b) 의 최소값을 도출
    for i in range(1, n+1):
        answer = min(answer, distance[s][i] + distance[i][a]+ distance[i][b])
    return answer