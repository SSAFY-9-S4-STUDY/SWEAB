def solution(board):
    n = len(board)
    cost_board = [[maxsize for _ in range(n)] for _ in range(n)]
    for i in range(4):
        cost_board[i][0][0] = 0
    
    answer = 0
    return answer