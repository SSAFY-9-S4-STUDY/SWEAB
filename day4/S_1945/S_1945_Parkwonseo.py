T = int(input())
for test_case in range(1, T + 1):
    # N == 2^a * 3^b * 5^c * 7^d * 11^e
    N = int(input())
        
    count_2, count_3, count_5, count_7, count_11 = 0, 0, 0, 0, 0
    """
    while N % 2 == 0:
        N = N // 2
        count_2 += 1

    while N % 3 == 0:
        N = N // 3
        count_3 += 1

    while N % 5 == 0:
        N = N // 5
        count_5 += 1

    while N % 7 == 0:
        N = N // 7
        count_7 += 1

    while N % 11 == 0:
        N = N // 11
        count_11 += 1
    
    print(f'#{test_case} {count_2} {count_3} {count_5} {count_7} {count_11}')
    """

    while N != 1:
        if N % 2 == 0:
            N = N // 2
            count_2 += 1

        if N % 3 == 0:
            N = N // 3
            count_3 += 1

        if N % 5 == 0:
            N = N // 5
            count_5 += 1

        if N % 7 == 0:
            N = N // 7
            count_7 += 1

        if N % 11 == 0:
            N = N // 11
            count_11 += 1

    print(f'#{test_case} {count_2} {count_3} {count_5} {count_7} {count_11}')

