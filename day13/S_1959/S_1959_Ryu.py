cases = int(input())
for x in range(1, cases + 1):
    a, b = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))

    long = lst_a if a >= b else lst_b
    long_num = max(a, b)
    short = lst_b if a >= b else lst_a
    short_num = min(a, b)

    max_num = 0
    for i in range(long_num - short_num + 1):
        temp = 0
        for j in range(short_num):
            temp += long[i + j] * short[j]

        if temp > max_num:
            max_num = temp

    print(f'#{x} {max_num}')