from collections import defaultdict
import heapq


def dijkstra(n, destination, adjN):
    adjM = [n] * (n + 1)
    adjM[destination] = 0
    queue = []
    heapq.heappush(queue, (adjM[destination], destination))

    while queue:
        nowM, nowN = heapq.heappop(queue)

        if adjM[nowN] < nowM:
            continue

        for nearN in adjN[nowN]:
            if adjM[nearN] > adjM[nowN]+1:
                adjM[nearN] = adjM[nowN]+1
                heapq.heappush(queue, (adjM[nearN], nearN))

    for i in range(n+1):
        if adjM[i] == n:
            adjM[i] = -1

    return adjM


def solution(n, roads, sources, destination):

    # [1] 연결정보 저장
    adjN = defaultdict(list)
    for n1, n2 in roads:
        adjN[n1].append(n2)
        adjN[n2].append(n1)

    # [2] 도착지로부터 각 노드까지의 거리 저장 후 반환
    adjM = dijkstra(n, destination, adjN)
    answer = list(map(lambda x: adjM[x], sources))

    return answer

