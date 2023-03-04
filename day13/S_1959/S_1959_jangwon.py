T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))

    # 범위 선정
    K = abs(N - M)

    # 답을 받아주는 변수
    ans = 0

    # 움직일 배열 선정
    if N > M:  # B가 움직일 것
        for i in range(K + 1):
            tmp = 0
            for j in range(M):
                tmp += B_lst[j] * A_lst[j + i]
            if tmp > ans:
                ans = tmp
    else:
        for i in range(K + 1):
            tmp = 0
            for j in range(N):
                tmp += B_lst[j + i] * A_lst[j]
            if tmp > ans:
                ans = tmp
    print(f'#{test_case} {ans}')