import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):

    days = int(input())
    prices = list(map(int,input().split()))

    answer = 0

    while prices:
        day_to_sell = prices.index(max(prices))
        lst_tmp, max_price = prices[:day_to_sell], prices[day_to_sell]
        answer += sum([max_price-i for i in lst_tmp])
        prices = prices[day_to_sell+1:]

    print(f'#{test_case} {answer}')
