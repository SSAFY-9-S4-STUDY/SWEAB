import sys

def input():
    return sys.stdin.readline()

def how_far(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

T = int(input())  # 테스트케이스 : 2

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # SP, RP의 좌표
    N = int(input())  # N: int -- 행성의 개수
    cnt = 0  # 어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수

    for _ in range(N):
        cx, cy, r = map(int, input().split())
        # 행성과 출발/도착점 사이 거리를 각각 구해주고
        # if 거리 > 행성반지름 : pass
        # else 거리 <= 반지름 : cnt +1
        dis1 = how_far(x1, y1, cx, cy)
        dis2 = how_far(x2, y2, cx, cy)

        if dis1 > r and dis2 > r: continue
        elif dis1 < r < dis2: cnt += 1
        elif dis2 < r < dis1: cnt += 1

    print(cnt)