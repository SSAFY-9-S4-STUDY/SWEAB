# [1] B -> 1, W -> 0으로 치환
# [2] KxK 정사각형 내에 합계를 2가지 버전으로 구해줌
# [3] for문 돌려서 구역별 합산에서 KxK 정사각형 합계를 빼주기
# [4] 최솟값 출력

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, K = map(int, input().split())
chess = [list(input().rstrip()) for _ in range(N)]

# B -> 1, W -> 0으로 치환
for i in range(N):
    for j in range(M):
        if chess[i][j] == 'B':
            chess[i][j] = 1
        else:
            chess[i][j] = 0

# KxK 정사각형 합계
# : W가 더 많으면 idx 0으로, B가 더 많으면 idx 1로 빼기
k_sum = [K**2 // 2, K**2 // 2 + 1]

# 구역별 합계에서 KxK 정사각형 합계 빼주기



dis_sum = 0
for i in range(N - K + 1):
    for j in range(M - K + 1):
        dis_sum += chess[i][j]
dis_sum -



