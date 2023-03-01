T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 약통을 받아주는 2차 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []  # 0번째 인덱스는 갯수, 이후 행과 열의 갯수를 카운트할 예정
    for j in range(N):
        for i in range(N):
            y = x = 0  # 여기에 0이 아닌 행렬의 행과 열의 크기를 받아줄 것.
            tmp_y = tmp_x = 0
            if arr[j][i] != 0:  # 0이 아니라고 보이는 순간 판단 시작!
                x += 1
                y += 1
                tmp_x = i       # 행과 열을 각각으로 판단해야 하기에 임시 변수에 할당
                tmp_y = j
                tmp_x += 1
                while arr[j][tmp_x] != 0:
                    x += 1
                    tmp_x += 1
                tmp_y += 1
                while arr[tmp_y][i] != 0:
                    y += 1
                    tmp_y += 1
                
                # 여기서부터는 판단한 곳들 모두 0으로 돌리기
                for ny in range(j, tmp_y): 
                    for nx in range(i, tmp_x):
                        arr[ny][nx] = 0
                lst.append([y, x])

    # 행렬 크기 순으로 그 후, 같을 때를 대비해서 행을 기준으로 정렬
    lst.sort(key=lambda t: (t[0] * t[1], t[0]))
    length = len(lst)

    print(f'#{test_case} {length}', *sum(lst, []))