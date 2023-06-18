from itertools import combinations, product

def solution(beginning, target):
    # 행과 열 개수 세기
    N, M = len(beginning), len(beginning[0])
    # 뒤집어야하는 좌표 구하기
    to_change = [[abs(target[r][c] - beginning[r][c]) for c in range(M)] for r in range(N)]
    # 행과 열을 선택할 수 있는 조합 딕셔너리에 저장
    row_comb = {i:list(combinations(range(N), i)) for i in range(N+1)}
    col_comb = {j:list(combinations(range(M), j)) for j in range(M+1)}
    # 바꿀 줄 개수에 따라 행과 열의 조합 선택
    for num_row, num_col in sorted(product(range(N+1),range(M+1),repeat=1),key=lambda x: sum(x)):
        # 선택한 행과 열을 바탕으로 배열 재구성
        for rows, cols in product(row_comb[num_row],col_comb[num_col],repeat=1):
            # 선택한 행과 열인지 아닌지 리스트로 정리
            row_info = [1 if r in rows else 0 for r in range(N)]
            col_info = [1 if c in cols else 0 for c in range(M)]
            # 리스트의 정보를 종합해 to_change와 비교
            for r, c in product(range(N), range(M), repeat=1):
                if to_change[r][c] != (row_info[r] + col_info[c]) % 2:
                    break
            # 모두 일치하면 행과 열 개수 총합을 반환
            else:
                return num_row + num_col
    # 불가능하다고 판단하여 -1을 반환
    return -1

beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
print(solution(beginning, target))