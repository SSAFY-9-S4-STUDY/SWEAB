def sum_of_product(A, B):
    maxi = -100 * N
    for i in range(M - N + 1):
        s = 0
        for j in range(N):
            s += A[j] * B[i+j]
        if maxi < s:
            maxi = s
    return maxi


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        print(f'#{tc} {sum_of_product(A, B)}')
    else:
        N, M = M, N
        print(f'#{tc} {sum_of_product(B, A)}')
