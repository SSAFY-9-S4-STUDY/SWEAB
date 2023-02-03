N ,M = map(int, input().split())
cards = list(map(int, input().split()))

max_value = 0
for i1 in range(N-2):
    for i2 in range(i1+1,N-1):
        for i3 in range(i2+1,N):
            tmp = cards[i1] + cards[i2] + cards[i3]
            if max_value < tmp <= M:
                max_value = tmp
                
print(max_value)





