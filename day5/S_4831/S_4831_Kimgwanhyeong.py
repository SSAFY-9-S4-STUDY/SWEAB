# 아이디어 : 

t = int(input())
for tc in range(1, t + 1):
    move, num, bus_stop = map(int, input().split())
    bus_stop_lst = list(map(int, input().split())) 

    # 충전 횟수를 변수에 할당해준다
    charge = 0

    position = 0

    while position < num:
        start = position
        position = position + move

        if position >= num:
            break

        if position in bus_stop_lst:
            charge += 1
        
        else:
            while position not in bus_stop_lst:
                position -= 1
                if position == start:
                    break

            if position == start:
                break    
            
            charge += 1
    if position == start:
        charge = 0
    print(f'#{tc} {charge}')