# # 가장 처음 생각했던 풀이랑 비슷하네용...
# # 여기는 없지만 종이로 생각했던 것은 다른 것만 찾아서 0과 1 중 갯수가 작은 것을 뒤집는다까지 생각했었음...
# 프로그래머스 다른 사람 풀이
def solution(beginning, target):
    answer = 0
    table = [[beginning[i][j] ^ target[i][j] for j in range(len(beginning[i]))] for i in range(len(beginning))]
    cnt = 0
    m = len(table)
    n = len(table[0])

    for i in range(1, m):
        if (table[i] != table[0]):
            cnt+=1
            if (list(map(lambda x: x ^ 1, table[i])) != table[0]):
                return -1

    answer = min((cnt) + sum(table[0]), (m - cnt) + (n - sum(table[0])))

    return answer


## 구글링해서 찾은 것... 근데 이 거랑 밑에 생각한 거랑 뭔 차이일까...?
# import math
#
#
# def fliprow(board, bits):
#     flipped = []
#     for i in range(len(board)):
#         # i번째 row를 뒤집어야 하면 뒤집은 리스트를 저장합니다.
#         if bits & (1 << i):
#             flipped.append([1 - x for x in board[i]])
#         else:
#             flipped.append(board[i])
#     return flipped
#
#
# def try_flipcol(board, target):
#     n_colflip = 0
#     # i번쨰 컬럼을 확인하는데
#     for i in range(len(board[0])):
#         # 경우의 수는 세가지입니다.
#         # 1. 안 뒤집어도 되는 경우
#         if [row[i] for row in board] == [t[i] for t in target]:
#             continue
#         # 2. 뒤집으면 같아지는 경우
#         elif [1 - row[i] for row in board] == [t[i] for t in target]:
#             n_colflip += 1
#         # 3. 어떻게 해도 같아질 수 없는 경우
#         else:
#             return -1
#
#     return n_colflip
#
#
# def solution(beginning, target):
#     # 뒤집어야 하는 row를 비트로 표현합니다.
#     # n개의 row가 있으면 0~2**n-1 까지 수로 나타내면 됩니다.
#     n = len(beginning)
#     ans = math.inf
#     for bits in range(2 ** n):
#         flipped = fliprow(beginning[:], bits)
#         n_colflip = try_flipcol(flipped, target)
#         if n_colflip == -1:
#             continue
#
#         n_rowflip = sum(bits & (1 << i) != 0 for i in range(n))
#         ans = min(n_rowflip + n_colflip, ans)
#
#     return ans if ans != math.inf else -1


# 처음 방법 ----- 실패...
# def solution(beginning, target):
#     from copy import deepcopy
#     answer = 0
#     tmp = deepcopy(beginning)
#     n = len(beginning)
#     # 1행에서 다른 경우
#     for k in range(n):
#         # 1행 판단
#         if beginning[0][k] != target[0][k]:
#             answer += 1
#             for j in range(n):
#                 tmp[j][k] = 0 if tmp[j][k] else 1
#         # 1열 판단
#         if beginning[k][0] != target[k][0]:
#             answer += 1
#             for i in range(n):
#                 tmp[k][i] = 0 if tmp[k][i] else 1
#
#     answer = min(answer, 2*n - answer)
#     return answer if target == tmp else -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
