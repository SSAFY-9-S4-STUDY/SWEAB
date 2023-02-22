import sys

# N: 세로 길이, M: 가로 길이, K: 구하려는 체스판 크기
N, M, K = map(int, sys.stdin.readline().split())

black = [[0 for c in range(M)] for r in range(N)]
white = [[0 for c in range(M)] for r in range(N)]


# 행과 열 누적합 구하기
dic = {'B': 0, 'W': 1 }  # 숫자로 변환을 위한 딕셔너리(0: 검정색, 1: 하얀색)
for r in range(N):
    tmp = list(sys.stdin.readline())
    black[r][0], white[r][0] = abs(r%2 - dic[tmp[0]]), abs((r+1)%2 - dic[tmp[0]])
    for c in range(1,M):
        black[r][c] = black[r][c-1] + abs((r+c)%2 - dic[tmp[c]])
        white[r][c] = white[r][c-1] + abs((r+c+1)%2 - dic[tmp[c]])

for r in range(1,N):
    for c in range(M):
        black[r][c] += black[r-1][c] 
        white[r][c] += white[r-1][c]


# 누적합을 고려하여 최솟값 구하기
total = min(black[K-1][K-1],white[K-1][K-1])
for r in range(K,N):
    total_b = black[r][K-1] - black[r-K][K-1]
    total_w = white[r][K-1] - white[r-K][K-1]
    total = min(total_b, total_w, total)

for c in range(K,M):
    total_b = black[K-1][c] - black[K-1][c-K]
    total_w = white[K-1][c] - white[K-1][c-K]
    total = min(total_b, total_w, total)

for r in range(K, N):
    for c in range(K, M):
            total_b = black[r][c] - black[r][c-K] - black[r-K][c] + black[r-K][c-K]
            total_w = white[r][c] - white[r][c-K] - white[r-K][c] + white[r-K][c-K]
            total = min(total_b, total_w, total)

print(total)



    





