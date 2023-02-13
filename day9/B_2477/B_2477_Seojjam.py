import sys
sys.stdin = open("input.txt")

# K: int -- 1m2의 넓이에 자라는 참외의 개수
# bound: [] -- 참외밭 경계
K = int(input())
bound = [[0, 0]]

# 동:1, 서:2, 남:3, 북:4
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

# 원래 위치: (0,0)
i = j = 0
for _ in range(6):
    # dir, dis: int -- 진행 방향, 거리
    # new_i, new_j: 진행 후 새 위치
    dir, dis = map(int, input().split())
    new_i, new_j = i + di[dir] * dis, j + dj[dir] * dis
    bound.append([new_i, new_j])
    i, j = new_i, new_j

