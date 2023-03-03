import sys
sys.stdin = open('1959.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    max_sum = 0
    for i in range(M-N+1):
        tmp = 0
        for j in range(N):
            tmp += A[j] * B[i+j]
        max_sum = max(max_sum, tmp)

    print(f'#{test_case} {max_sum}')