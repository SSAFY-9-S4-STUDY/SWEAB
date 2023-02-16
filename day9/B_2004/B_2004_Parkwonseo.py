def counting(num, x):
    ans = 0
    while num >= x:
        ans += num // x
        num = num // x
    return ans

n, m = map(int, input().split())

count_5 = counting(n, 5) - counting(m, 5) - counting(n - m, 5) 
count_2 = counting(n, 2) - counting(m, 2) - counting(n - m, 2) 
print(min(count_5,count_2))