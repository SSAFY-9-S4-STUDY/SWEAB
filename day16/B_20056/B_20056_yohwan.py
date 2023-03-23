import sys
sys.stdin = open("input.txt")

# 인풋 받기
# 받으면서 초기 파이어볼의 정보를 넣어줄 리스트 만들기
N, M, K = map(int, input().split())
where_a = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    where_a[r-1][c-1].append([m, s, d])

# 방향 설정 0 ~ 7
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# K번 동안 이동
for _ in range(K):
    # 이동 후 리스트를 받기 위해 새로 리스트 생성
    where_b = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 미안 코드가 좀 더러워용 ㅎㅎ
            # 파이어볼이 존재 한다면
            if where_a[i][j]:
                # 각각 파이어볼의 질량 속도 방향 체크해서 옮기기
                for k in range(len(where_a[i][j])):
                    m = where_a[i][j][k][0]
                    s = where_a[i][j][k][1]
                    d = where_a[i][j][k][2]
                    where_b[(i + dy[d] * s) % N][(j + dx[d] * s) % N].append([m, s, d])

    # 이동하고 합치고 나눠지는 과정
    where_a = where_b[:]
    even_d = [0, 2, 4, 6]
    odd_d = [1, 3, 5, 7]
    for i in range(N):
        for j in range(N):
            balls = len(where_a[i][j])
            new_m = 0
            new_s = 0
            new_d = 0
            # 한 곳에 모인 파이어볼이 2이하면 다음탐색
            if balls < 2:
                continue
            # 2개 이상이라면?
            for k in range(balls):
                new_m += where_a[i][j][k][0]
                new_s += where_a[i][j][k][1]
                new_d += where_a[i][j][k][2] % 2
            # 2개 이상인데 나눠진것들이 질량이 0이라면 다음탐색
            if new_m // 5 == 0:
                where_a[i][j] = []
                continue
            if new_d == balls or new_d == 0:
                nd = even_d
            else:
                nd = odd_d
            where_a[i][j] = []

            for d in nd:
                where_a[i][j].append([new_m // 5, new_s // balls, d])

# 답 도출
ans = 0
for i in range(N):
    for j in range(N):
        if where_a[i][j]:
            for k in range(len(where_a[i][j])):
                ans += where_a[i][j][k][0]

print(ans)






