T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    ans = score[0:K]
    min_val = min(ans)
    for x in score[K:]:
        if min_val < x:
            ans.remove(min_val)
            ans.append(x)
            min_val = min(ans)

    print(f'#{tc} {sum(ans)}')