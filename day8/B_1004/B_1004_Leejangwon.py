import sys

def in_distance(a1, b1, a2, b2, r):
    distance = pow((pow(a2 - a1, 2) + pow(b2 - b1, 2)), (1/2))
    if distance <= r:
        return True
    else:
        return False

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cnt = 0
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().rstrip().split()))
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().rstrip().split())
        if (in_distance(x1, y1, cx, cy, r) or in_distance(x2, y2, cx, cy, r))\
            and in_distance(x1, y1, cx, cy, r) != in_distance(x2, y2, cx, cy, r) :
            cnt += 1
    print(cnt)
