import sys
sys.stdin = open('input.txt')

t=int(input())
for tc in range(1,t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    temp_list = []
    for i in range(N):
        for j in range(N):
            start_col = start_row = 0
            cnt_col = cnt_row = 0
            if arr[i][j] and visited[i][j]==0:
                start_col = j
                start_row = i
                temp = [0,0]
                for k in range(start_row,N):
                    if arr[k][start_col]:
                        visited[k][start_col] =1
                        cnt_row+=1
                    else:
                        temp[0] = cnt_row
                        break
                    for m in range(start_col,N):
                        if arr[k][m]:
                            visited[k][m] = 1
                            cnt_col+=1
                        else:
                            temp[1] = cnt_col
                            cnt_col = 0
                            break
                temp_list.append(temp)
    temp_list.sort(key = lambda x:(x[0]*x[1],x[0]))
    ans = sum(temp_list,[])
    print(f'#{tc} {len(temp_list)}',*ans)