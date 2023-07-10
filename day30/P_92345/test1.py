def solution(board, aloc, bloc):
    # 탐색 함수
    def play(board, order, n):
        # 움직일 사람의 위치
        row, col = locs[order]
        # 플레이어 위치에 발판이 없다면 패배
        if not board[row][col]:
            rst_lst.append((n//2+order,n//2))
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
        # 현재 플레이어가 이동할 곳이 없다면 패배
        if end:
            rst_lst.append((n//2+order,n//2))
            return

    R, C = len(board), len(board[0])
    locs, rst_lst = [tuple(aloc), tuple(bloc)], []
    play(board, 0, 0)

    ans = 1000
    # for i in rst_lst:
    return sorted(rst_lst)

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [0,0], [2,2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1,0], [1,2]))
print(solution([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], [0,0], [4,4]))