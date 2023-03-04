T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    scores = sorted(list(map(int,input().split())))
    res = 0
    for i in range(K):
        res += scores[-1-i]
    print(f'#{tc} {res}')