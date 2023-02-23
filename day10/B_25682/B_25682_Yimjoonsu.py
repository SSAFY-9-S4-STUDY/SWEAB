import sys

def chess(color):
    arr = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j] - arr[i][j] + value
    count = sys.maxsize
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            count = min(count, arr[i+K-1][j+K-1] - arr[i+K-1][j-1]\
                        - arr[i-1][j+K-1] + arr[i-1][j-1])
    return count


N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(min(chess('B'), chess('W')))

# https://mgyo.tistory.com/773
# 안풀려서 참고했습니다....