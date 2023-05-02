from collections import deque

def solution(m, n, puddles):
    # dists 최단 거리를 기록할 이중배열
    dists = [[10000] * m for _ in range(n)]
    for c, r in puddles + [[1,1]]:
        dists[r-1][c-1] = 0
    # cnts 최단 거리로 올 수 있는 루트 수를 기록할 이중 배열
    cnts = [[0] * m for _ in range(n)]
    cnts[0][0] = 1
    # 최단 거리를 가지는 경로 개수 세기
    vector = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        for v in vector:
            nr, nc = r + v[0], c + v[1]
            d, cnt = dists[r][c] + 1, cnts[r][c]
            # 배열 인덱스를 넘어가거나, 기록된 최단 거리를 넘어서면 종료
            if nr < 0 or nr >= n or nc < 0 or nc >= m or d > dists[nr][nc]:
                continue
            if d < dists[nr][nc]:
                dists[nr][nc] = d
                queue.append((nr, nc))
            cnts[nr][nc] += cnt

    return cnts[n-1][m-1] % 1000000007

m, n = 4, 3
puddles = 	[[2, 2]]
print(solution(m,n,puddles))

