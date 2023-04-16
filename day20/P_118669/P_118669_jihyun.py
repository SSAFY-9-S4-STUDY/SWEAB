from collections import deque


def solution(n, paths, gates, summits):
    adjM = [[0] * (n+1) for _ in range(n + 1)]
    for i, j, w in paths:
        adjM[i][j] = w
        adjM[j][i] = w
    
    queue = deque()
    intensitys = [1e7] * (n + 1)
    
    for gate in gates:
        intensitys[gate] = 0
        queue.append((0, gate))
    
    while queue:
        inten, i = queue.popleft()
        if i in summits:
            continue
        if intensitys[i] < inten:
            continue

        for j, w in enumerate(adjM[i]):
            if j and i != j:
                intensitys[j] = min(intensitys[j], max(intensitys[i], w))
                queue.append((max(intensitys[i], w), j))
            
    answer = [n + 1, 1e7]
    
    for summit in summits.sort():
        if intensitys[summit] < answer[1]:
            answer[0] = summit
            answer[1] = intensitys[summit]
    
    return answer


