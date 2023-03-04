import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []

    for i in range(1, N+1):
        if i not in lst:
            result.append(i)

    print(f'#{test_case}', *result)