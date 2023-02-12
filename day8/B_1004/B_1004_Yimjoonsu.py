T = int(input())

for test_case in range(1, T+1):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    n = int(input())
    for _ in range(n):
        dup = 1
        cx, cy, rad = map(int, input().split())
        d1 = (cx-x1)**2 + (cy-y1)**2
        d2 = (cx-x2)**2 + (cy-y2)**2

        if d1 < rad**2 :
            count += 1
            dup = 0

        if d2 < rad**2:
            if dup:
                count += 1
            else:
                count -= 1

    print(count)
