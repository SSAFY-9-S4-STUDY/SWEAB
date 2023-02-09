import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 초기값 받기
    str_list = [input() for _ in range(N)]

    # 각 문자를 리스트 내 요소로 받기
    arr = [[] for _ in range(N)]

    for i in range(N):
        for c in str_list[i]:
            arr[i].append(c)

    status = False

    # 행판단
    for raw in str_list:
        for x in raw.split('.'):
            if x:
                if len(x) >= 5:
                    status = True

    # 열판단
    temp = list(zip(*arr))
    new_arr = [''.join(cl) for cl in temp]

    for column in new_arr:
        for w in column.split('.'):
            if w:
                if len(w) >= 5:
                    status = True

    # 왼대각선판단
    left_diag = [[]for _ in range(2 * N - 1)]
    for k in range(2 * N - 1):
        if k <= N - 1:
            for y in range(k + 1):
                left_diag[k].append(arr[y][k - y])
        else:
            for y in range(k - N + 1, N):
                left_diag[k].append(arr[y][k - y])

    lnew_arr = [''.join(lcl) for lcl in left_diag]

    for ldiag in lnew_arr:
        for t in ldiag.split('.'):
            if t:
                if len(t) >= 5:
                    status = True



    # 오른대각선 판단
    right_diag = [[] for _ in range(2 * N - 1)]
    for k in range(-N+1, N):
        if k <= 0:
            for y in range(N - abs(k)):
                right_diag[k].append(arr[y][y-k])
        if k > 0:
            for y in range(N - abs(k)):
                right_diag[k].append(arr[k+y][y])

    rnew_arr = [''.join(rcl) for rcl in right_diag]

    for rdiag in rnew_arr:
        for z in rdiag.split('.'):
            if z:
                if len(z) >= 5:
                    status = True

    if status == True:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
