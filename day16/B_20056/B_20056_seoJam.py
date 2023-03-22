import sys
sys.stdin = open("input.txt")

if __name__ == '__main__':

    # dir: 방향 리스트
    dir = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

    # N:격자크기  M:볼 개수  K:이동횟수
    N, M, K = map(int, input().split())

    #fball: 파이어볼 리스트
    fball = []
    id = 0
    for _ in range(M):
        # r:행  c:열  m:질량  s:속도  d:방향
        r, c, m, s, d = map(int, input().split())
        fball.append([r, c, m, s, d])

    # arr: 질량만 나타낼 NxN 격자
    arr = list([0] * N for _ in range(N))

    cnt = 0
    while cnt <= K:
        cnt += 1
        # (방향 * 속도) 만큼 r, c에 더해주기
        for i in range(len(fball)):
            fball[i][0] += dir[fball[i][3]][0] * fball[i][4]  # 행 이동
            fball[i][1] += dir[fball[i][3]][1] * fball[i][4]  # 열 이동


            arr[fball[i][0]][fball[i][1]] += fball[i][3]      # 격자에 무게 저장


