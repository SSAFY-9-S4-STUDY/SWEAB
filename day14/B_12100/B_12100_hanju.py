import sys
from itertools import product


# board를 입력받은 방향으로 밀어주는 함수
# 입력받은 방향으로 민 상태의 board를 반환
def slide(t, b):
    global max_num

    # t: 밀어주는 방향(0: right, 1: left, 2: down, 3: up)
    # s: 탐색 시작 인덱스, e: 탐색 끝 인덱스, d: 탐색 방향
    s, e, d = (0, N, 1) if t % 2 else (N-1, -1, -1)
    # b: board의 상태 방향이 2(down), 3(up)일 경우 전치행렬을 사용
    b = list(zip(*b)) if t // 2 else b

    
    rst = [[0] * N for _ in range(N)]  # 밀어준 결과를 입력할 변수
    for r in range(N):
        # stack: 입력 판단이 되지 않은 숫자, idx: 현재 행에서 숫자를 넣을 인덱스
        stack, idx = 0, s
        # r행의 열들을 탐색
        for c in range(s, e, d):
            tmp = b[r][c]
            if tmp:  # 만약 0이 아닌 숫자라면
                if not stack:  # stack이 비어있다면 stack을 채워줌
                    stack = tmp
                else:  # stack에 숫자가 있다면
                    if stack == tmp:  # 같다면 2배하여 rst에 입력
                        rst[r][idx] = 2 * stack
                    else:  # 아니라면 그대로 rst에 입력
                        rst[r][idx] = stack
                    # 같은 값이라면 stack을 비워주고, 아니라면 stack을 교체
                    stack = tmp * (not tmp == stack)
                    max_num = max(max_num, rst[r][idx]) # 입력값과 최대값을 비교
                    idx += d  # 숫자를 넣었으니 인덱스 값 변경
        if stack:  # 탐색이 끝난 후 stack에 숫자가 남아있다면 rst에 입력
            rst[r][idx] = stack

    # 방향이 2(down), 3(up)일 경우 전치행렬을 다시 원상태로 돌려줌
    return list(zip(*rst)) if t // 2 else rst


N = int(sys.stdin.readline())
board = [list(map(int, input().split())) for _ in range(N)]


max_num = max(sum(board,[]))  # 최대값을 저장할 변수
# 외부 라이브러리를 통해 이동 방향 순서(중복 순열)를 구현
# 4방향으로 5번 움직이니 총 1024 개의 case가 생김
for case in product(range(4), repeat=5):
    # 각 시뮬레이션마다 board_tmp를 처음 상태로 초기화
    board_tmp = board
    # 각 case의 최종 board 상태를 함수를 통해 도출
    for trial in case:
        board_tmp = slide(trial, board_tmp)

print(max_num)


