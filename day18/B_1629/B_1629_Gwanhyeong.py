def recursive(x, n, cut):
    if n == 1:
        return x
    if n % 2:
        y = recursive(x, (n-1)//2, cut)
        if y > cut:
            y = y % cut
        return y * y * x
    else:
        y = recursive(x, n//2, cut)
        if y > cut:
            y = y % cut
        return y * y


A, B, C = map(int, input().split())

ans = recursive(A, B, C)
print(ans % C)
