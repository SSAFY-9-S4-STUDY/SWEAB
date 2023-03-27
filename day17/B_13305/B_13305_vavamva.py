# 주유소 문제

# 우리는 모든 주유소의 가격을 알고 있다.
# 하지만 시작 기름은 없음.

city_n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cheapest = 0
# travel = distance[0]
_min = cost[0]
for city in range(len(distance)):
    if _min > cost[city]:
        _min = cost[city]
    cheapest += _min * distance[city]

print(cheapest)