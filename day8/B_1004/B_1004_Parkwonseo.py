def in_or_out(x, y, arr, n):
    if (x - arr[n][0]) ** 2 + (y - arr[n][1]) ** 2 < arr[n][2] ** 2:
        return "in"
    else:
        return "out"


counting = []
t = int(input())
for tc in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    stars = []
    n = int(input())
    for i in range(n):
        stars.append(tuple(map(int, input().split())))

    count = 0
    
    for i in range(n):
        if in_or_out(x1, y1, stars, i) != in_or_out(x2, y2, stars, i):
            count += 1
    
    # print(count)

    counting.append(str(count))

print("\n".join(counting))