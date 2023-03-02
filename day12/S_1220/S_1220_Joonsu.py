import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for j in range(N):
        check = False
        for i in range(N):
            if not check and arr[i][j] == 1:
                check = True
            if check and arr[i][j] == 2:
                check = False
                result += 1

    print(f'#{test_case} {result}')
