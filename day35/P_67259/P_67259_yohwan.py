Max = 25 * 25 * 500
ans = Max

def solution(board):
    new_board = [[Max]* len(board) for _ in range(len(board))]
    
    def findans(x, y, n, cost, corner):
        global ans
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        if new_board[x][y] < cost:
            return
        else:
            new_board[x][y] = cost
        
        if (x, y) == (n-1, n-1):
            if cost < ans:
                ans = cost
            return
        
        board[x][y] = -1
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and board[x+dx[i]][y+dy[i]] == 0:
                if (x,y) == (0, 0) or (corner+i) % 2 == 0:
                    findans(x+dx[i], y+dy[i], n, cost+100, i)
                else:
                    findans(x+dx[i], y+dy[i], n, cost+600, i)
        
        board[x][y] = 0

    findans(0, 0, len(board), 0, 0)
    
    return ans