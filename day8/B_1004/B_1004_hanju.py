import sys

T = int(sys.stdin.readline())
for _1 in range(T):

    x1, y1 ,x2, y2 = map(int,sys.stdin.readline().split())
    N = int(sys.stdin.readline())

    cnt = 0
    for _2 in range(N):
        cx, cy, r = map(int,sys.stdin.readline().split())
        d1, d2 = ((x1-cx)**2 + (y1-cy)**2), ((x2-cx)**2 + (y2-cy)**2)
        if (d1 < r**2 and d2 > r**2) or (d1 > r**2 and d2 < r**2):
            cnt +=1
        
    print(cnt)