T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] * A[j] <= ans:
                break
            num = A[i] * A[j]
            temp = num % 10
            num //= 10
            while num:
                if num % 10 > temp:
                    break
                temp = num % 10
                num //= 10
            else:
                ans = A[i] * A[j]

    print(f'#{tc} {ans}')

