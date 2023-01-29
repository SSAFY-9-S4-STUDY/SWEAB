T = int(input())

for i in range(1, T + 1):
    a, b, c, d, e = 0, 0, 0, 0, 0
    case = int(input())
    
    while case > 1:
        if case % 2 == 0:
            a += 1
            case = case // 2
            continue
        elif case % 3 == 0:
            b += 1
            case = case // 3
            continue
        elif case % 5 == 0:
            c += 1
            case = case // 5
            continue
        elif case % 7 == 0:
            d += 1
            case = case // 7
            continue
        elif case % 11 == 0:
            e += 1
            case = case // 11
            continue

    print(f'#{i} {a} {b} {c} {d} {e}')       


