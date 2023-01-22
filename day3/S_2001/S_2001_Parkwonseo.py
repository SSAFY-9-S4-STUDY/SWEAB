T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    area = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        area.append(tmp)

    def fly_killer(list1, m, a, b):
        rlt = 0
        for i in range(m):
            for j in range(m):
                rlt += list1[a + i][b + j]
        return rlt
    
    
    max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = fly_killer(area, M, i, j)
            if max < temp:
                max = temp

    print(f'#{test_case} {max}')
