N = int(input())
ans1 = ans2 = N

num = 0

while True:
    num += 1
    a, b = divmod(ans1, 10)
    n = a + b
    m = b * 10 + n % 10
    if m == ans2:
        print(num)
        break
    else:
        ans1 = m