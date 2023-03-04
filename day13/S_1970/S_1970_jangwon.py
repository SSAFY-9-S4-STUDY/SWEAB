T = int(input())

for test_case in range(1, T + 1):
    money_lst = [0 for _ in range(8)]
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    raw = int(input())

    for i in range(8):
        while raw >= money[i]:
            money_lst[i] += 1
            raw -= money[i]
    print(f'#{test_case}')
    print(*money_lst)