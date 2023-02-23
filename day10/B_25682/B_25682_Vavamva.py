# n(y) * m(x) 보드를 k*k로
n, m, k = map(int, input().split())
board = [input() for _ in range(n)]

# factor 는 어떻게 잡아야 하는가..
# (m + 1 - k) * (n + 1 - k)

# 첫 케이스를 구하고, w / b 의 경우로 더해준 뒤,
# 각 경우에 대해 그 다음 줄의 마킹 숫자를 더하고 첫 줄은 빼며 진행

# 아이디어는 잘 받았지만.. 구현할 능력이 안되는 것 같습니다.. 던집니다욧!!!


arr_x = []
arr_y = []

# 왼쪽 위가 B인 경우
for i in range(n - k):
    count_y = 0
    count_x = 0
    for j in range(m - k):
        for a in range(k):
            for b in range(k):
                if (i + j) % 2:
                    if board[i][j] == 'B':
                        count_y += 1
                    if board[j][i] == 'B':
                        count_x += 1
                else:
                    if board[i][j] == 'W':
                        count_y += 1
                    if board[j][i] == 'W':
                        count_x += 1
    arr_y.append(count_y)  # index + 1 == 실제 순번
    arr_x.append(count_x)

sum_fix_y = 0
sum_fix_x = 0
for idx in range(k):
    sum_fix_y += arr_y[idx]
    sum_fix_x += arr_x[idx]

for i in range(n - k + 1):
    for j in range(m - k + 1):
        sum_fix_y
        sum_fix_x

# 왼쪽 위가 W 인 경우
for i in range(n):
    for i in range(n):
        count_y = []
        count_x = []
        count = []
        for j in range(m):
            if (i + j) % 2:
                if board[i][j] == 'W':
                    count.append(1)
                if board[j][i] == 'W':
                    count_x += 1
            else:
                if board[i][j] == 'B':
                    count_y += 1
                if board[j][i] == 'B':
                    count_x += 1
            arr_y.append(count_y)  # index + 1 == 실제 순번
            arr_x.append(count_x)