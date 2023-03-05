money = [5000, 1000, 500, 100, 50, 10, 5, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10

    ans = [0] * 8
    for idx, val in enumerate(money):
        if not N:
            break
        ans[idx] = N // val
        N %= val

    print(f'#{tc}')
    print(*ans)