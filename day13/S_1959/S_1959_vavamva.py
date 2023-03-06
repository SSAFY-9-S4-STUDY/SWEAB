t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    if n > m:
        arr_1 = list(map(int, input().split()))
        arr_2 = list(map(int, input().split()))
    else:
        arr_2 = list(map(int, input().split()))
        arr_1 = list(map(int, input().split()))
        n, m = m, n

    max_v = 0
    for i in range(n - m + 1):
        tmp = 0
        for j in range(m):
            tmp += arr_1[i + j] * arr_2[j]

        if max_v < tmp:
            max_v = tmp

    print(f"#{tc} {max_v}")