def find_mat(i,j):
    global mat_info, area
    ni, nj = i, j
    while True:
        nj += 1
        if area[i][nj] == 0:
            cnt_y = nj - j
            break

    while True:
        ni += 1
        if area[ni][j] == 0:
            cnt_x = ni - i
            break
    mat_info.append([cnt_x, cnt_y])
    for k in range(i, ni):
        for l in range(j, nj):
            area[k][l] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    
    mat_num = 0
    mat_info = []
    for i in range(N):
        for j in range(N):
            if area[i][j]:
                find_mat(i,j)
                mat_num += 1
    
    mat_info.sort(key = lambda x: (x[0]*x[1], x[0]))
    res = sum(mat_info,[])
    print(f'#{tc} {mat_num}', *res)