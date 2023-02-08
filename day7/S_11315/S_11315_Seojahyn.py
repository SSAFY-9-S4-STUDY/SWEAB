import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N(5 ≤ N ≤ 20)

    omok = []
    for _ in range(N):
        omok.append(input())  # 오목판 받기

    N = len(omok)
    num = 0

    # 가로방향 검사
    for i in range(N):
        if 'ooooo' in omok[i]:
            num += 1

    # 세로방향 검사
    for j in range(N):
        for i in range(N):
            cnt = 0
            if 0 <= i < N and omok[i][j] == 'o':
                while 0 <= i < N and omok[i][j] == 'o':
                    i += 1
                    cnt += 1
            if cnt >= 5:
                num += 1

    # 대각방향 검사
    for i in range(N):
        cnt = 0
        if 0 <= i < N and omok[i][i] == 'o':
            while 0 <= i < N and omok[i][i] == 'o':
                i += 1
                cnt += 1
            if cnt >= 5:
                num += 1

    # 역대각방향 검사
    for i in range(N):
        cnt = 0
        if 0 <= i < N and omok[i][-1 - i] == 'o':
            while 0 <= i < N and omok[i][-1 - i] == 'o':
                i += 1
                cnt += 1
            if cnt >= 5:
                num += 1

    if num >= 1:
        print(f'#{tc} Yes')
    else: print(f'#{tc} No')

