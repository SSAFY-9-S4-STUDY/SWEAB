# 97개 맞았습니다... 3개 찾고 싶어요

import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for test_case in range(1, t+1):
    N = int(input())
    ground = [input() for _ in range(N)]
    
    # 결과를 변수에 할당
    result = 'NO'
    
    # 가로를 탐색
    for i in range(N):
        cnt_hor = 0
        for j in range(N):   # i 번째 행에서 가로로 탐색하며 o가 있으면 카운트를 늘리고 . 이 있으면 카운트를 초기화 해줌
            if ground[i][j] == 'o':
                cnt_hor += 1
                if cnt_hor >= 5:
                    result = 'YES'
                    break
            else:
                cnt_hor = 0
        if cnt_hor >= 5:
            break
    # 세로를 탐색
        cnt = 0
        for k in range(N):  # i 번째 열에서 세로로 탐색하여 o가 있으면 카운트를 늘림
            if ground[k][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
                    break
            else:
                cnt =0
        if cnt >= 5:
            break

    # \ 대각선을 탐색
    # \ 대각선의 경우 행과 열의 숫자를 뺀 값이 일정하다. 그 뺀 값의 범위가 -N+1부터 N-1까지이므로
    for i in range(-N+1, N):
        # 행의 초기값 설정
        j = 0
        cnt = 0
        while 0 <= j-i <= N-1:  # 인덱스가 0에서 N-1이므로 인덱스를 벗어나면 중단
            if ground[j][j-i] == 'o':
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
                    break
            else:
                cnt = 0
            j +=1
        if cnt >= 5:
            break

    # / 대각선을 탐색
    # / 대각선의 경우 행과 열의 값의 합이 일정하다.
    for i in range(0, 2*N+1):
        j = 0
        cnt = 0
        while 0 <= i-j <= N-1 :
            if ground[j][i-j] == 'o':
                cnt += 1
                if cnt >= 5:
                    result = 'YES'
                    break
            else:
                cnt = 0
            j += 1
        if cnt >= 5:
            break
    print(f'#{test_case} {result}')