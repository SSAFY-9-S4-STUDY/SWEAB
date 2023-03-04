T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{test_case}')

    for num in lst:
        print(N // num, end=' ')
        N = N % num
    print()