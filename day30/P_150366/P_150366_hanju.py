def solution(commands):
    pointer = [[(row, col) for col in range(51)] for row in range(51)]
    table = [['EMPTY'] * 51  for j in range(51)]
    ans = []
    for command in commands:
        tmp = command.split()
        # 셀 병합
        if tmp[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, tmp[1:])
            row1, col1 = pointer[r1][c1]
            row2, col2 = pointer[r2][c2]
            # 같은 셀인 경우
            if row1 == row2 and col1 == col2:
                continue
            # 왼쪽 셀에 값이 있을 경우
            if table[row1][col1] != 'EMPTY':
                row1, col1, row2, col2 = row2, col2, row1, col1
            # 포인터들 수정
            for r in range(1,51):
                for c in range(1,51):
                    if pointer[r][c] == (row1, col1): pointer[r][c] = (row2, col2)
            table[row1][col1] = 'EMPTY'
        # 셀 병합 해제
        elif tmp[0] == 'UNMERGE':
            row, col = pointer[int(tmp[1])][int(tmp[2])]
            word = table[row][col]
            for r in range(1,51):
                for c in range(1,51):
                    if pointer[r][c] == (row,col): pointer[r][c] = (r, c)
            table[row][col], table[int(tmp[1])][int(tmp[2])] = 'EMPTY', word
        # 셀 출력
        elif tmp[0] == 'PRINT':
            row, col = pointer[int(tmp[1])][int(tmp[2])]
            ans.append(table[row][col])
        # 특정 단어 수정
        elif len(tmp) == 3:
            for r in range(1,51):
                for c in range(1,51):
                    if table[r][c] == tmp[1]: table[r][c] = tmp[2]
        # 특정 위치 수정
        else:
            row, col = pointer[int(tmp[1])][int(tmp[2])]
            table[row][col] = tmp[3]

    return ans

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", 
            "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", 
            "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", 
            "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", 
            "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
from pprint import pprint
pprint(solution(commands), width=500)

