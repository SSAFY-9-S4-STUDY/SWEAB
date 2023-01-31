T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())

    count = 0
    
    puz = [input().replace(' ', '') for i in range(N)]

    # 행 판별  6
    for case in puz:
        rones = case.split('0')
        for t in rones:
            if t == '1' * K:
                count += 1
    
    # 열 판별 8
    for j in range(N):
        column = ''
        for case in puz:
            column += case[j]
        cones = column.split('0')
        for p in cones:
            if p == '1'*K:
                count += 1

    print(f'#{i} {count}')

    # # Set Matrix
    # puz = [list(map(int, input().split())) for i in range(N)]
    
    # for case in puz:
    #     if sum(case)
    #     for m in range(N - K + 1):
    #         if sum(case[m:m + K]) == K:
    #             count += 1