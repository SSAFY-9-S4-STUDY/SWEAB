cases = int(input())
for x in range(1, cases + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst_all = list(range(1, N + 1))

    for i in range(K):
        lst_all.remove(lst[i])

    print(f'#{x}', *lst_all)
