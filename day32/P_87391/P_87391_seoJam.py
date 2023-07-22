# quries를 역재생하며 후보군을 추림
# 이때 후보군은 무조건 사각형이므로 => 4개 변의 좌표를 갱신해가면서 시뮬레이션 실행
def solution(n, m, x, y, queries):
    q = len(queries)

    row_start = row_end = x     # 위, 아래
    col_left = col_right = y    # 좌, 우

    for i in range(q-1, -1, -1):
        command, dx = queries[i]

        # 한주꺼 보고 조건문 바꿈... 한방에 해결
        if col_right < col_left or row_end < row_start:
            return 0 

        if command == 0:
            # if col_left > 0 and col_left+dx > m-1:    # 후보군이 격자 밖으로 벗어난 경우(1)
            #     return 0
            col_left = 0 if col_left == 0 else col_left + dx
            col_right = min(m-1, col_right+dx)

        elif command == 1:
            # if col_right < m-1 and col_right-dx < 0:  # 후보군이 격자 밖으로 벗어난 경우(2)
            #     return 0
            col_left = max(col_left-dx, 0)
            col_right = m-1 if col_right == m-1 else col_right - dx

        elif command == 2:
            # if row_start > 0 and row_start+dx > n-1:  # 후보군이 격자 밖으로 벗어난 경우(3)
            #     return 0
            row_start = 0 if row_start == 0 else row_start + dx
            row_end = min(n-1, row_end+dx)

        else:
            # if row_end < n-1 and row_end-dx < 0:      # 후보군이 격자 밖으로 벗어난 경우(4)
            #     return 0
            row_start = max(row_start-dx, 0)
            row_end = n-1 if row_end == n-1 else row_end - dx

    answer = (row_end-row_start+1) * (col_right-col_left+1)

    return answer
