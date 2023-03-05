T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    done = list(map(int, input().split()))

    print(f'#{tc}', end=' ')
    for i in range(1, N+1):
        if i not in done:
            print(i, end=' ')
    print()
