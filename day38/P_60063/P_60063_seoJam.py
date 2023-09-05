from collections import deque


def solution(board):
    MAX_VALUE = 1e9
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    N = len(board)

    # board 주변을 1로 패딩
    new_board = [[1 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            new_board[i][j] = board[i - 1][j - 1]

    dp = [[MAX_VALUE for _ in range(N + 1)] for _ in range(N + 1)]
    dp[1][1] = dp[1][2] = 0
    queue = deque([(1, 1), (1, 2)])

    while queue:
        cr, cc = queue.popleft()

        for dr, dc in DIRS:
            nr, nc = cr + dr, cc + dc
            # 범위 확인
            if nr < 1 or nc < 1 or N < nr or N < nc:
                continue
            # 벽 확인
            if new_board[nr][nc]:
                continue
            # 90도 회전 가능 확인
            if (not dc and new_board[nr][nc - 1] and new_board[nr][nc + 1]) or (
                not dr and new_board[nr - 1][nc] and new_board[nr + 1][nc]
            ):
                continue
            
            new_value = dp[cr][cc] + 1

            if dp[nr][nc] > new_value:
                dp[nr][nc] = new_value
                queue.append((nr, nc))
    print(dp)
    answer = dp[N][N]

    return answer


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
