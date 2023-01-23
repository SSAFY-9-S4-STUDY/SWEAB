t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())
    my_lst = [list(map(int, input().split())) for _ in range(n)]
    max_score = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for i_time in range(m):
                for j_time in range(m):
                    sum += my_lst[i + i_time][j + j_time]
            if max_score < sum:
                max_score = sum

    print(f'#{test_case}',max_score)