import sys

# 입력값 받기
N, M, K = map(int, sys.stdin.readline().split())
balls = []
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    balls.append((r-1, c-1, m, s, d))

# 인덱스를 통한 이동 방향 매칭
v = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1, -1)]
ball_split = [(1, 3, 5, 7), (0, 2, 4, 6)]

# K번만큼 시행
for _ in range(K):

    # 이동한 파이어볼의 정보들을 저장할 배열들
    m_lst = [[0]*N for _ in range(N)]
    s_lst = [[0]*N for _ in range(N)]
    d_arr = [[[] for _ in range(N)] for _ in range(N)]
    locations = []

    # 파이어볼을 이동시킴
    for r, c, m, s, d in balls:
        nr, nc = (r + v[d][0]*s) % N, (c + v[d][1]*s) % N
        if not d_arr[nr][nc]:
            locations.append((nr,nc))
        d_arr[nr][nc].append(d)
        m_lst[nr][nc] += m
        s_lst[nr][nc] += s

    # 이동한 파이어볼을 토대로 정보 갱신
    balls, ans = [], 0
    for r, c in locations:
        m, s = m_lst[r][c], s_lst[r][c]
        d_lst = d_arr[r][c]
        d_n = len(d_lst)
        # 탐색 위치에 파이어볼이 하나만 있을 때
        if d_n == 1:
            balls.append((r, c, m, s, d_lst[0]))
            ans += m
        # 탐색 위치에 파이어볼이 2개 이상일 때
        elif m > 4:
            nm, ns = m//5, s//d_n
            # 어느 방향으로 쪼개질지 결정
            mode = 1
            for i in range(d_n - 1):
                if d_lst[i] % 2 != d_lst[i+1] % 2:
                    mode = 0
                    break
            # 결정난 방향으로 쪼개진 파이어볼을 리스트에 넣어줌
            for d in ball_split[mode]:
                balls.append((r, c, nm, ns, d))
                ans += nm
                
print(ans)

    


