T = int(input())
for i in range(T):       
    H, W, N = map(int,input().split())
    yy= H if N%H == 0 else N%H
    xx = (N//H) if N%H == 0 else (N//H)+1
    zero = '0' if len(str(xx)) == 1 else  ''
    print(f'{yy}{zero}{xx}')