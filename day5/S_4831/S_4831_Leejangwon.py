N = int(input())

for i in range(1, N + 1):
    K, N, M = map(int,input().split())
    charg_stat = list(map(int, input().split()))

    # 현장 재현
    station = []

    for p in range(N + 1):
        if p in charg_stat:
            station.append(1)
        else:
            station.append(0)
    
    count = 0
    k = 0
    status = True
    
    while True:  
        t = 0
        if k + K >= N:
            break
        else:
            while station[k + K - t] != 1:
                t += 1
                if t >= K:
                    count = 0
                    status = False      
                    break
            if status == False:
                break

            count += 1       
            k = k + K - t
            
    print(f'#{i} {count}')