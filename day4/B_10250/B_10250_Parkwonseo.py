T = int(input())
for test_case in range(T):
    
    H, W, N = map(int, input().split())
    
    check_in = 0
    for room in range(1, W + 1):
        for floor in range(1, H + 1):
            check_in += 1
            
            if check_in == N:
                result = str(floor) + str(format(room, '02'))
                break
    
    print(result)            

    """준수님 아이디어
    room = N // H + 1
    floor = N % H
    if floor == 0:
        room -= 1
        floor = H
    print(100 * floor + room)
    """
