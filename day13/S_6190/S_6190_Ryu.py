cases = int(input())
for x in range(1, cases + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    rlt = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            temp = lst[i] * lst[j]

            prev = 0
            for k in str(temp):
                if prev > int(k):
                    break
                prev = int(k)
            else:
                if rlt < temp:
                    rlt = temp
    print(f'#{x} {rlt}')