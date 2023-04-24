def solution(board, skill):
    n = len(board)
    m = len(board[0])
    sum_arr = [[0]*(m+1) for _ in range(n+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        
        sum_arr[r1][c1] += degree
        sum_arr[r1][c2 + 1] -= degree
        sum_arr[r2 + 1][c1] -= degree
        sum_arr[r2 + 1][c2 + 1] += degree

    for i in range(n + 1):
        for j in range(1, m + 1):
            sum_arr[i][j] += sum_arr[i][j-1]

    for i in range(1, n + 1):
        for j in range(m + 1):
            sum_arr[i][j] += sum_arr[i-1][j]

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + sum_arr[i][j] > 0:
                answer += 1

    return answer
