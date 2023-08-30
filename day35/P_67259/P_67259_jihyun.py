def solution(board):
    N = len(board)
    # 최대값으로 설정
    answer = 500 * N * N
    
    # 상하좌우
    directions = [(1, 0, -1), (1, 0, 1), (2, -1, 0), (2, 1, 0)]
    
    # dp 배열
    dp = [[answer] * N for _ in range(N)]
    
    def cost(i, j, tmp_cost, direc):
        nonlocal answer
        
        if dp[i][j] < tmp_cost:
            return
        dp[i][j] = tmp_cost
        
        # 종료조건
        if i == j == N - 1:
            answer = min(answer, tmp_cost)
            return
        
        # 다음칸으로 이동
        board[i][j] = 1
        for direction, di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                if direc == 0 or direc == direction:
                    cost(ni, nj, tmp_cost + 100, direction)
                else:
                    cost(ni, nj, tmp_cost + 600, direction)
        board[i][j] = 0 
    
    cost(0, 0, 0, 0)
    
    return answer


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))