from queue import deque

MAX_VALUE = 1e5
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동서남북


def solution(board):
    n = len(board)
    dp = [[MAX_VALUE for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    q = deque([(0, 0, 0), (0, 0, 2)])  # (row, column, dir)

    while q:
        cr, cc, prev = q.popleft()

        for idx in range(4):
            dr, dc = DIRS[idx]
            nr, nc = cr + dr, cc + dc

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue

            if board[nr][nc]:
                continue

            new_value = dp[cr][cc] + 100 if prev == idx else dp[cr][cc] + 600

            if dp[nr][nc] >= new_value:
                dp[nr][nc] = new_value
                q.append((nr, nc, idx))

    # print(dp)
    return dp[n - 1][n - 1]


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
