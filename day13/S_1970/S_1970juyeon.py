T = int(input())
money = [50000,10000,5000,1000,500,100,50,10]
for tc in range(1, T+1):
    N = int(input())
    payback = [0]*8
    for i in range(8):
        while N >= money[i]:
            N -= money[i]
            payback[i] += 1

    print(f'#{tc}')
    print(*payback)