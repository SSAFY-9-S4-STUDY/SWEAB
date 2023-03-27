N = int(input())
roads = list(map(int, input().split()))
per_liter = list(map(int, input().split()))

# 끝 도시까지 가는 데 필요한 최소 비용을 변수 price에 할당
price = 0
# 기준이 되는 리터당 가격
gas = per_liter[0]

for i in range(N-1):
    if per_liter[i] < gas:
        gas = per_liter[i]
    price += gas * roads[i]

print(price)
