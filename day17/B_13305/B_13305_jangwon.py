N = int(input())

road = list(map(int, input().split()))

price = list(map(int, input().split()))

total_price = road[0] * price[0]

now_station = price[0]

for i in range(1, N - 1):
    if now_station > price[i]:
        now_station = price[i]

    total_price += now_station * road[i]

print(total_price)