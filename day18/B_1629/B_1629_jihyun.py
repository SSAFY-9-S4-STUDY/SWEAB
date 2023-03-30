def multi(a, b):
    if b == 1:
        return a % c
    div = multi(a, b//2)
    if b % 2:
        return (div * div * a) % c
    else:
        return (div * div) % c


a, b, c = map(int, input().split())
print(multi(a, b))