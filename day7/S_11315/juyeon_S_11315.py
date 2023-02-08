T = int(input())
for tc in  range(1, T+1):
    res = 'NO'
    N = int(input())
    arr_str = [input() for _ in range(N)]

    # 1 가로 ooooo 탐색
    if res == 'NO':
            for i in range(N):
                for j in range(N-4):
                    for k in range(5):
                        if arr_str[i][j+k] != 'o':
                            break
                    else: res = 'YES'
    
    # 2 세로 ooooo 탐색
    if res == 'NO':
        for i in range(N-4):
                for j in range(N):
                    for k in range(5):
                        if arr_str[i+k][j] != 'o':
                            break
                    else: res = 'YES'

    # 3 왼쪽위 -> 오른쪽 아래 ooooo 탐색
    if res == 'NO':
        for i in range(N-4):

            for j in range(N-4):
                for k in range(5):
                    if arr_str[i+k][j+k] != 'o':
                        break
                else: res = 'YES'  

    # 4 오른쪽위 -> 왼쪽 아래 ooooo 탐색
    if res == 'NO':
        for i in range(N-4):

            for j in range(4, N):
                for k in range(5):
                    if arr_str[i+k][j-k] != 'o':
                        break
                else: res = 'YES'

 
    print(f'#{tc} {res}')