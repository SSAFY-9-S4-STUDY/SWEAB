from copy import deepcopy

###### 왜 틀렸는지 몰라서 구글링을 좀 했습니다#####
## pointer를 넣기 전 코드 중 일부
# if dir == 0:  # 오른쪽
#     for y in range(N, 0, -1):
#         for x in range(N, 0, -1):
#             ny, nx = y, x + 1
#             if 1 <= ny < N + 1 and 1 <= nx < N + 1:
#                 if board[ny][nx] == board[y][x]:
#                     board[ny][nx] *= 2
#                     board[y][x] = 0
#                 else:
#                     if board[ny][nx] == 0:
#                         board[ny][nx] = board[y][x]
#                         board[y][x] = 0


def moving(board, dir):
    if dir == 0:  # 오른쪽
        for i in range(N):
            pointer = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp

    elif dir == 1:  # 아래
        for j in range(N):
            pointer = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp

    elif dir == 2:  # 왼쪽
        for i in range(N):
            pointer = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp

    elif dir == 3:  # 위쪽
        for j in range(N):
            pointer = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j] = tmp

    return board

def find_max(board, depth):
    global ans
    # 4방향으로 이동하되 이동 후의 판을 그대로 두고 중간에만 이동할 거임.
    if depth == 5:
        for y in range(N ):
            for x in range(N):
                ans = max(ans, board[y][x])
        return

    for k in range(4):
        tmp = moving(deepcopy(board), k)
        find_max(tmp, depth + 1)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
find_max(arr, 0)
print(ans)

