N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
min_p = price[0]

for i in range(N-1):
    if min_p > price[i]:
        min_p = price[i]
    result += min_p * distance[i]

print(result)