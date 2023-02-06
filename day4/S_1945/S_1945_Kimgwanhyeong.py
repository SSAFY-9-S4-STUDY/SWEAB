T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    a=0
    b=0
    c=0
    d=0
    e=0

    while not N % 2:
        a += 1
        N = N // 2

    while not N % 3:
        b += 1
        N = N // 3

    while not N % 5:
        c += 1
        N = N // 5

    while not N % 7:
        d += 1
        N = N // 7

    while not N % 11:
        e += 1
        N = N // 11

    print(f'#{test_case}', a, b, c, d, e,)