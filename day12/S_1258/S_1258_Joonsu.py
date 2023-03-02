import sys
sys.stdin = open('input.txt', 'r')


def search(row, col):
    global X
    global Y
    dx = [0, 0, 1]
    dy = [1, -1, 0]
    arr[row][col] = 0
    for i in range(3):
        new_x = row + dx[i]
        new_y = col + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N\
            and arr[new_x][new_y] != 0:
            if new_x - x1 + 1 >= X:
                X = new_x - x1 + 1
            if new_y - y1 >= Y:
                Y = new_y - y1 + 1
            search(new_x, new_y)
    return X, Y


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    count = 0
    result_temp = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if arr[j][i] != 0:
                count += 1
                X = 0
                Y = 0
                x1 = j
                y1 = i
                result_temp.append(search(j, i))
    result = sorted(result_temp, key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{test_case}', count, end=' ')
    for i in result:
        print(*i, end=' ')
    print()
