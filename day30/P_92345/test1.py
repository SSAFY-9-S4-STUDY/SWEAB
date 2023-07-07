def solution(board, aloc, bloc):
    # 탐색 함수
    def play(board, order, n):
        nonlocal ans
        # 종료 조건 1. 현재 기록된 최적값보다 n이 크면 탐색 중지
        if n >= ans:
            lst.append((order, n))
            return
        # 움직일 사람의 위치
        row, col = locs[order]
        # 종료 조건 2. 플레이어 위치에 발판이 없다면 패배
        if not board[row][col]:
            ans = min(n, ans)
            lst.append((order, n))
            return 
        # 현재 순번 플레이어 이동
        end = True  # 이동할 곳이 있는지 판단할 함수
        for r,c in [(1,0), (-1,0), (0,1), (0,-1)]:
            n_row, n_col = row + r, col + c
            if 0 <= n_row < R and 0 <= n_col < C and board[n_row][n_col]:
                end = False  # 종료 조건 철회
                # 상태값을 변화시키고 dfs
                board[row][col], locs[order] = 0, (n_row, n_col)
                play(board, abs(order-1), n+1)
                board[row][col], locs[order] = 1, (row, col)
        # 종료 조건3. 현재 플레이어가 이동할 곳이 없다면 패배
        if end:
            ans = min(n, ans)
            lst.append((order, n))
            return

    R, C = len(board), len(board[0])
    ans, locs = 5 * 5, [tuple(aloc), tuple(bloc)]
    lst = []
    play(board, 0, 0)

    return lst

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [0,0], [2,2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1,0], [1,2]))
# print(solution([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], [0,0], [4,4]))