N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
tmp_p = price.pop(0)
for idx, d in enumerate(distance):
    ans += tmp_p * d
    if tmp_p > price[idx]:
        tmp_p = price[idx]

print(ans)