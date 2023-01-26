T = int(input())
for i in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    maximum = 0
    profit = 0

    for k in price[::-1]:
        if k > maximum:
            maximum = k
        else:
            profit += (maximum - k)

    print(f'#{i} {profit}')
    