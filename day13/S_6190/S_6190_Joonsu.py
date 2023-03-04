import sys
sys.stdin = open('input.txt', 'r')


def increasing(x):
    if x[-1] == 0:
        return -1

    for k in range(1, len(x)):
        if x[k-1] > x[k]:
            return -1
    else:
        return x


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = -1

    for i in range(N):
        for j in range(i+1, N):
            result = max(result, int(increasing(str(lst[i] * lst[j]))))

    print(f'#{test_case} {result}')