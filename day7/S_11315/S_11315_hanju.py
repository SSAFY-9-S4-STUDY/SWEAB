import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def is_five(lst):
    cnt = 0
    for i in lst:   
        if i == 'o':
            cnt += 1
            if cnt == 5:
                return True
        else:
            cnt = 0

    return True if cnt >= 5 else False

for test_case in  range(1, T+1):
    N = int(input())

    omok = [list(input()) for _ in range(N)] # 오목 일반 행렬
    omok_trans = list(zip(*omok))  # 오목 전치 행렬

    omok_cross1, omok_cross2 = [], []  # 대각선 판단을 위한 리스트
    for i in range((N-4)):
        if i == 0:
            omok_cross1.append([omok[j][j] for j in range(N)])
            omok_cross2.append([omok[j][N-1-j] for j in range(N)])
        else:
            omok_cross1.append([omok[i+j][j] for j in range(N-i)])
            omok_cross1.append([omok[j][i+j] for j in range(N-i)])
            omok_cross2.append([omok[j+i][N-1-j] for j in range(N-i)])
            omok_cross2.append([omok[j][N-1-j-i] for j in range(N-i)])

    answer = 'NO'
    for row in omok + omok_trans + omok_cross1 + omok_cross2:
        if is_five(row):
            answer = 'YES'
            break

    print(f'#{test_case} {answer}')