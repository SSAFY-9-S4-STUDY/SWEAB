T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    as_a_list = [list(map(int, input().split())) for i in range(N)]

    flies = list()

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_num = 0
            for x in range(M):
                for y in range(M):
                    fly_num += as_a_list[i+x][j+y]
            flies.append(fly_num)
    print(f'#{test_case} {max(flies)}')