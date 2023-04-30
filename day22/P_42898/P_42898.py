def solution(m, n, puddles):
    route = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    route[1][1] = 1

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                continue
            else:
                route[j][i] = (route[j - 1][i] + route[j][i - 1]) % 1000000007
    return route[n][m]
# 결과는 다 통과이지만... 효율성에서 ㅠㅠ
# def puddle_table(p):
#     return [p[0] - 1, p[1] - 1]
#
#
# def solution(m, n, puddles):
#     route = [[0 for _ in range(m)] for _ in range(n)]
#     puddles = list(map(puddle_table, puddles))
#     # route에 초기설정표시
#     for p in puddles:
#         route[p[1]][p[0]] = -1
#
#     # 경계선에 1로 도배하기
#     for i in range(m):
#         if route[0][i] != -1:
#             route[0][i] = 1
#         else:
#             break
#
#     for j in range(n):
#         if route[j][0] != -1:
#             route[j][0] = 1
#         else:
#             break
#
#     # 탐색 시작
#     for j in range(1, n):
#         for i in range(1, m):
#             if route[j][i] == -1:
#                 continue
#             if route[j - 1][i] == -1:
#                 if route[j][i - 1] == -1:
#                     continue
#                 else:
#                     route[j][i] = route[j][i - 1]
#             else:
#                 if route[j][i - 1] == -1:
#                     route[j][i] = route[j - 1][i]
#                 else:
#                     route[j][i] = route[j - 1][i] + route[j][i - 1]
#     answer = route[n - 1][m - 1]
#
#     return answer