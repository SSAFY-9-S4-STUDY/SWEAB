def solution(board, aloc, bloc):
    # a가 이긴다고 가정
    def win_a(order, n):
        if order == 'a':
            # 이동시 b와의 거리, 가까워질 수 있는 이동 방향
            dist, direct= 25, []
            for r, c in [(1,0), (-1,0), (0,1), (0,-1)]:
                n_row, n_col = aloc[0] + r, aloc[1] + c
                if 0 <= n_row < R and 0 <= n_col < C and board[n_row][n_col]:
                    move_distance = 
                    if abs(n_row-bloc[0]) + abs(n_col-bloc[1]) < 
            

        pass
    def win_b(order, n):
        pass

    R, C = len(board), len(board[0])
    ans = 5 * 5

    return ans

print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))