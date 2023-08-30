def solution(key, lock):
    
    def check(new_board):
        n = len(new_board) // 3
        for i in range(n, n*2):
            for j in range(n, n*2):
                if new_board[i][j] != 1:
                    return False
        return True
    
    def rotate(original_board, type):
        n = len(original_board)
        result = [[0] * n for _ in range(n)]
        if type == 1:
            for r in range(n):
                for c in range(n):
                    result[c][n-r-1] = original_board[r][c]
        elif type == 2:
            for r in range(n):
                for c in range(n):
                    result[n-r-1][n-c-1] = original_board[r][c]
        elif type == 3:
            for r in range(n):
                for c in range(n):
                    result[n-c-1][r] = original_board[r][c]
        else:
            return original_board

        return result


    m = len(key)
    n = len(lock)
    new_lock = [[0 for _ in range(n*3)] for _ in range(n*3)]
    for r in range(n, n*2):
        for c in range(n, n*2):
            new_lock[r][c] = lock[r-n][c-n]

    for i in range(1, n*2):
        for j in range(1, n*2):
            # 열쇠 회전
            for d in range(4):
                rotation_key = rotate(key, d)
                # 열쇠 맞춰보기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += rotation_key[x][y]
                if check(new_lock):
                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= rotation_key[x][y]
    return False