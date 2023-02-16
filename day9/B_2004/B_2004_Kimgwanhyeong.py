def cnt_n(num, comp):
    cnts = 0
    i = 1
    while comp ** i <= num:
        cnts += num // (comp ** i)
        i +=1
    return cnts


n, m = map(int, input().split())

cnt_fiv = cnt_n(n,5) - cnt_n(m,5) - cnt_n((n-m),5)
cnt_two = cnt_n(n,2) - cnt_n(m,2) - cnt_n((n-m),2)
print(min(cnt_two,cnt_fiv))