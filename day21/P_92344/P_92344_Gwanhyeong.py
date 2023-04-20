# 처음 풀이 : 정확성 ok 효율성 not ok
def solution(board, skill):
    for char in skill:
        t, r1, c1, r2, c2, degree = char
        if t ==1:  # 파괴
            for y in range(r1, r2+1):
                for x in range(c1, c2+1):
                    board[y][x] -= degree
        else:   # 복원
            for y in range(r1, r2+1):
                for x in range(c1, c2+1):
                    board[y][x] += degree
    ans = 0
    for row in board:
        for num in row:
            if num > 0:
                ans += 1
    return ans

# 누적합을 이용한 풀이(w Google)
# 
def solution(board, skill):
    tmp = [[0] * (len(board) + 1) for _ in range(len(board)+1)]
    ans = 0
    # r1,c1 ~ r2,c2 에 누적합하기 위한 사전작업
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2+1] += -degree if type == 2 else degree
        tmp[r2+1][c1] += -degree if type == 2 else degree
        tmp[r2+1][c2+1] += degree if type == 2 else -degree

    # 행 기준 누적합
    for i in range(len(tmp) - 1):
        for j in range(len(tmp) - 1):
            tmp[i][j+1] += tmp[i][j]
    # 열 기준 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j] += tmp[i][j]

    # 누적합 해준 tmp 2차원 배열을 더해주기만 하면 된다. O(1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                ans += 1
    return ans