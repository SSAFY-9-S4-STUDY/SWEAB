import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for dir_idx in range(4):
                    new_x = j
                    new_y = i
                    count = 0
                    while 0 <= new_x < N and 0 <= new_y < N\
                        and arr[new_y][new_x] == 'o':
                        count += 1
                        new_x += dx[dir_idx]
                        new_y += dy[dir_idx]
                    if count >= 5:
                        result = 'YES'
    print(f'#{test_case} {result}')