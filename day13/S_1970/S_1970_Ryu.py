cases = int(input())
for x in range(1, cases + 1):
    money = int(input())
    lst = [0] * 8
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        lst[i] = money // money_lst[i]
        money = money % money_lst[i]

    print(f'#{x}')
    print(*lst)

