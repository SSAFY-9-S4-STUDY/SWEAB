T = 10

for test_case in range(1, T + 1):
    N = int(input())  # 정사각형 한 변 길이
    arr = [list(map(int, input().split())) for  _ in range(N)]

    my_stack = []
    cnt = 0
    for i in range(N):  # 열을 메인 즉, 중심으로 판단할 것
        for j in range(N):  # 행을 하나씩 판단할 것.
            if arr[j][i] == 1:
                my_stack.append(1)
            elif arr[j][i] == 2:
                if my_stack:  # stack 안에 1이 있을 때만 카운트를 1올려준다.
                    cnt += 1
                    my_stack.clear()
        my_stack.clear()  # 해당 열 판단이 끝나면 스택은 비우기 

    print(f'#{test_case} {cnt}')