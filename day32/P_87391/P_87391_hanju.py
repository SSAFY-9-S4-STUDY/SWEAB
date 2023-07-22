def solution(N, M, x, y, queries):
    xs, xe, ys, ye = x, x, y, y
    for q, d in queries[::-1]:
        # x, y에 도착할 수 있는 경우가 없음
        if xs > xe or ys > ye:
            return 0
        # x, y 가 존재할 수 있는 범위를 queires를 반대로 돌면서 추측
        if q == 0:
            ys = ys if not ys else ys + d
            ye = min(M-1, ye + d)
        elif q == 1:
            ys = max(0, ys - d)
            ye = ye if ye == M - 1 else ye - d
        elif q == 2:
            xs = xs if not xs else xs + d
            xe = min(N-1, xe + d)
        elif q == 3:
            xs = max(0, xs - d)
            xe = xe if xe == N - 1 else xe - d

    return (xe - xs + 1) * (ye - ys + 1)

print(solution(2,2,0,0,	[[2,1],[0,1],[1,1],[0,1],[2,1]]))