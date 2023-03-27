N = int(input())
road = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_p = 1000000000

ans = 0
for r, p in zip(road, prices[:-1]):
    min_p = min(min_p, p)
    ans += r * min_p

print(ans)