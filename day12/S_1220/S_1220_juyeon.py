for tc in range(1, 11):
    input()
    table = [input().split() for _ in range(100)]
    table_rev = list(zip(*table))
    
    cnt = 0
    for i in range(100):
        idx = False
        for j in range(100):
            if table_rev[i][j] == '1':
                idx = True
            if table_rev[i][j] == '2' and idx:
                cnt += 1
                idx = False
                
    print(f'#{tc} {cnt}')