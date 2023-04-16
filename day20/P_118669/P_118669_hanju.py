from collections import deque

def solution(N, paths, gates, summits):

    graph = [[] for _ in range(N+1)]
    for p in paths:
        graph[p[0]].append((p[1],p[2]))
        graph[p[1]].append((p[0],p[2]))

    intensities, queue = [0]*(N+1), deque()
    for i in gates:
        intensities[i] = -1
        queue.append((i,0))
    for i in summits:
        intensities[i] = 't'

    min_d, summit = 10000000, 50000
    while queue:
        e, d = queue.popleft()
        for ne, nd in graph[e]:
            nd = max(nd, d)
            if intensities[ne] == 't':
                if nd < min_d:
                    min_d, summit = nd, ne
                elif nd == min_d:
                    summit = min(summit, ne)
            elif not intensities[ne] or nd < intensities[ne]:
                intensities[ne] = nd
                queue.append((ne, nd))

    return [summit, min_d]
