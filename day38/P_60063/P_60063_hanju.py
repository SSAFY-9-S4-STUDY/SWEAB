from collections import deque

def solution(board):
    # 1. 변수 설정
    # 맵의 크기
    N = len(board)
    # dp를 위한 기록용 이차원 배열들
    # 가로, 새로 따로 분할
    hor = [[float("inf")] * (N-1) for _ in range(N)]
    ver = [[float("inf")] * (N) for _ in range(N-1)]
    # 가로, 세로별 행과 열의 최대 길이
    min_cost = {0:hor, 1:ver}

    # 2. 초기 세팅
    # 시작 지점 값 변경
    hor[0][0] = 0
    # hor에서 갈 수 없는 지점 기록
    for r in range(N):
        for c in range(N-1):
            if board[r][c] or board[r][c+1]:
                hor[r][c] = 0
    # ver에서 갈 수 없는 지점 기록
    for r in range(N-1):
        for c in range(N):
            if board[r][c] or board[r+1][c]:
                ver[r][c] = 0

    # 3. 함수 - dp 판단 후 이동 함수
    def move(hv, nr, nc, cost):
        if min_cost[hv][nr][nc] < cost: return
        min_cost[hv][nr][nc] = cost
        queue.append((nr, nc, hv))  

    # 3. dp 수행
    queue = deque([(0,0,0)])
    while queue:
        # 행, 열, 가로세로여부
        r, c, hv = queue.pop()
        # 비용
        cost = min_cost[hv][r][c] + 1
        # 회전 이동시 모양
        nhv = abs(hv - 1)
        # 현재 모양에서의 배열 크기
        n, m = (N-1, N) if hv else (N, N-1)
        # 4방향 이동
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # 이동 좌표
            nr, nc = r + x, c + y
            # board의 유효한 위치인지 더이상 cost를 줄일 수있는지 측정
            if nr < 0 or nr == n: continue
            if nc < 0 or nc == m: continue
            if not min_cost[hv][nr][nc]: continue
            # 모두 유효하면 위치 이동
            # 그대로 이동
            move(hv, nr, nc, cost)
            # 가로일 경우
            if not hv and not y:
                nx = (x - 1) // 2
                move(nhv, r + nx, c, cost)
                move(nhv, r + nx, c + 1, cost)
            # 세로일 경우
            if hv and not x:
                ny = (y - 1) // 2
                move(nhv, r, c + ny, cost)
                move(nhv, r + 1, c + ny, cost)
    
    vertical, horizantal = ver[-1][-1], hor[-1][-1]
    if not vertical: return horizantal
    if not horizantal: return vertical
    return min(vertical,horizantal)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))