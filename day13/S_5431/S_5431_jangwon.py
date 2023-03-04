T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_lst = list(map(int, input().split()))
    print(f'#{test_case}', end=' ')
    for i in range(1, N + 1):
        if i not in num_lst:
            print(i, end=' ')
    print()
