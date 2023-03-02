import sys
sys.stdin = open('1258.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]
    counted = [[0]*N for _ in range(N)]
    
    rc = []
    for r in range(N):
        for c in range(N):
            if not counted[r][c] and warehouse[r][c]:
                nr, nc = r, c
                while nr < N and warehouse[nr+1][c]:
                    nr += 1
                while nc < N and warehouse[r][nc+1]:
                    nc += 1
                for i in range(r, nr+1):
                    for j in range(c, nc+1):
                        counted[i][j] = 1
                rc.append([nr-r+1, nc-c+1])

    rc.sort(key=lambda x: (x[0]*x[1], x[0]))

    print(f'#{test_case} {len(rc)}', end = ' ')
    for i in rc:
        print(*i, end = ' ')
    print()


