T = int(input()) 
for line in range(1, T + 1):
    K, N, M = map(int, input().split())

    chargers = sorted(list(map(int, input().split())))
    
    find_it = 0
    station = 0
    count = 0
    i = 0
    while True:
        find_it = station + K - i
        i += 1
        if find_it >= N:
            break
        elif find_it == station:
            count = 0
            break
        elif find_it in chargers:
            station = find_it
            i = 0
            count += 1


    print(f'#{line} {count}')