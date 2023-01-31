T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    
    while num % 11 == 0:
        e += 1
        num = num/11

    while num % 7 == 0:
        d += 1
        num = num/7

    while num % 5 == 0:
        c += 1
        num = num/5

    while num % 3 == 0:
        b += 1
        num = num/3

    while num % 2 == 0:
        a += 1
        num = num/2

    print(f'#{test_case} {a} {b} {c} {d} {e}')