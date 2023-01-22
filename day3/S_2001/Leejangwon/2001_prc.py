T = int(input())

for q in range(T):
    a, b = input().split()
    N, M = int(a), int(b)
    fly_list = []

    for i in range(N):
        fly_list.append(input().split())

    sum_list = []
    for m in range(N):
        for n in range(N - M + 1):
            sum_list.append(eval('+'.join(fly_list[m][n:n+M])))
    
    sum_max = []
    for i in range((N-M + 1)**2):
        z = 0
        for t in range(M):
            z += sum_list[i + (N - M + 1) * t]
        sum_max.append(z)
        # sum_max.append(sum_list[i] + sum_list[i + N - M + 1])

    print(f'#{q + 1} {max(sum_max)}')