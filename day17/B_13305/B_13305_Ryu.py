import sys
input = sys.stdin.readline

N = int(input())
roads = [0] + list(map(int, input().split()))
cities = list(map(int, input().split()))

rlt = 0
oil_price = 1000000000
go = 0
for i in range(N):
    go += roads[i]
    if cities[i] < oil_price:
        rlt += oil_price * go
        go = 0
        oil_price = cities[i]
rlt += oil_price * go
print(rlt)