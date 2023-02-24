##### 느낀점 #####
# 개념을 모르고 문제를 푸니 빡세군용....#
# 그렇지만 모르는 개념을 활용한 문제는 제가 공부한 흔적을 남겨서 올릴게요!(늘 그랬지만!)

import sys
input_ = sys.stdin.readline().rstrip()

def balckandwhite(color):
    # 누적합을 하기 위한 한 칸씩 더 늘린 누적합 배열
    presum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            #
            if (i + j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] - presum[i][j] + value

    cnt = float('inf')
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            cnt = min(cnt, presum[i + K - 1][j + K - 1] - presum[i + K - 1][j - 1] - presum[i - 1][j + K - 1] + presum[i - 1][j - 1])

    return cnt


N, M, K = map(int, input_.split())
board = [list(input()) for _ in range(N)]
print(min(balckandwhite('B'), balckandwhite('W')))
