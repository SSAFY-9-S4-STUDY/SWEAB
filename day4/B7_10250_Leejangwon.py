T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N % H != 0:
        Y = N % H
        X = N // H + 1
    else:
        Y = H
        X = N // H

    print(Y * 100 + X)