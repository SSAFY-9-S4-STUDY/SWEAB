T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [False] * (N+1)
    for num in arr:
        check[num] = True
    ans = []
    for i in range(1,N+1):
        if not check[i]:
            ans.append(i)
    print(f'#{tc}',*ans)