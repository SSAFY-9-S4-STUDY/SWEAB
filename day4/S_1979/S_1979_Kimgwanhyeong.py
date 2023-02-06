t = int(input())
for test_case in range(1, t+1):
    n, k =map(int, input().split())
    ground = [list(map(int,input().split())) for _ in range(n)]

    rst = 0
    for row in range(n):
        row_count = 0
        for col in range(n):
            if ground[row][col]:
                row_count += 1
            else:
                if row_count == k:
                    rst += 1
                row_count = 0
        if row_count == k:
            rst += 1

            

    for col in range(n):
        col_count = 0 # column 바뀔 때마다 col_count 리셋
        for row in range(n):
            if ground[row][col]:
                col_count += 1
            else:
                if col_count == k:
                    rst += 1
                col_count = 0
        if col_count == k:
            rst += 1


    print(f'#{test_case} {rst}')