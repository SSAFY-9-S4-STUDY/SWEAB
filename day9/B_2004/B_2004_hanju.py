def factor(n, f):
    rst, exp = 0, 1
    while f**exp <= n:
        rst += n//(f**exp)
        exp += 1
    return rst

n, m = map(int,input().split())

cnt_2 = factor(n,2) - factor(m,2) - factor(n-m, 2)
cnt_5 = factor(n,5) - factor(m,5) - factor(n-m, 5)

print(max(0,min(cnt_2, cnt_5)))