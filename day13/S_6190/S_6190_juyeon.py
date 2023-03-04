def is_incre(x):
    global max_fin
    k = str(x)
    for i in range(1, len(k)):
        if int(k[i]) < int(k[i-1]):
            return
    max_fin = x

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    
    max_fin = -1
    for i in range(N-1):
        for j in range(i+1, N):
            temp = nums[i] * nums[j]
            if temp > max_fin:
                is_incre(temp)

    print(f'#{tc} {max_fin}')