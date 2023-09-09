from collections import deque


def solution(board):
    N = len(board)
    TARGET = (N - 1, N - 1)
    queue = deque([((0, 0), (0, 1), 0)])
    visited = set([((0, 0), (0, 1))])
    r, c = 0, 1

    while queue:
        rob1, rob2, cnt = queue.popleft()

        if rob1 == TARGET or rob2 == TARGET:
            return cnt

        # 가로 방향일때
        if rob1[r] == rob2[r]:
            for nr, nc in [
                (rob1[r] - 1, rob1[c]),
                (rob2[r] - 1, rob2[c]),
                (rob1[r], rob1[c] - 1),
                (rob2[r], rob2[c] + 1),
                (rob1[r] + 1, rob1[c]),
                (rob2[r] + 1, rob2[c]),
            ]:
                if nr < 0 or nc < 0 or N <= nr or N <= nc:
                    continue
                if board[nr][nc] == 1:
                    continue
                
        # 세로 방향일때
        elif rob1[c] == rob2[c]:
            for nr, nc in [
                (rob1[r] - 1, rob1[c]),
                (rob1[r], rob1[c] - 1),
                (rob1[r], rob1[c] + 1),
                (rob2[r], rob2[c] - 1),
                (rob2[r], rob2[c] + 1),
                (rob2[r] + 1, rob2[c]),
            ]:
                pass


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
