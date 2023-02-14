import sys
input = sys.stdin.readline

while True:



# 1. 0, 0 좌표 저장 & 값을 1로 변경
#
# 1 - 1. 좌표의 행, 열, 대각, 역대각의 모든 값을 1로 변경
#
# 2. 1이 아닌 좌표 찾아서 저장 & 값을 1로 변경
#
# 2 - 1. 좌표의 행, 열, 대각, 역대각의 모든 값을 1로 변경
#
# 3. 같은 방법 반복 ...


N = int(input())
chess = [[0] * N for _ in range(N)]





