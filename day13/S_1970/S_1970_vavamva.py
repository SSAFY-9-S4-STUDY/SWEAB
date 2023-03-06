# 쉬운 거스름돈

t = int(input())
for tc in range(1, t + 1):
    price = int(input())
    change = [0] * 8
    while price >= 50000:
        price -= 50000
        change[0] += 1
    while price >= 10000:
        price -= 10000
        change[1] += 1
    while price >= 5000:
        price -= 5000
        change[2] += 1
    while price >= 1000:
        price -= 1000
        change[3] += 1
    while price >= 500:
        price -= 500
        change[4] += 1
    while price >= 100:
        price -= 100
        change[5] += 1
    while price >= 50:
        price -= 50
        change[6] += 1
    while price >= 10:
        price -= 10
        change[7] += 1
    
    print(f"#{tc}")
    print(*change)