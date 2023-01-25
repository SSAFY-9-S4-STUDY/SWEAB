def calculator(list):
    max_num = max(list)
    idx = list.index(max_num)
    max_num = max_num * idx    
    for j in range(idx):
        max_num -= list[j]

    return (max_num,list[idx+1:])



T = int(input())
for i in range(T):
    N = int(input())
    prices = list(map(int,input().split()))

    result_max = 0
    while prices: 
        a, prices = calculator(prices) 
        result_max += a

    print(f'#{i+1} {result_max}')