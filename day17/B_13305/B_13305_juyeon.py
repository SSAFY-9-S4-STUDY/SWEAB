N = int(input())
dis = list(map(int,input().split()))
price = list(map(int,input().split()))

res = dis[0] * price[0]
m = price[0]
for i in range(1, N-1):
    if price[i] < m:
        m = price[i]
    res += m * dis[i]
print(res)