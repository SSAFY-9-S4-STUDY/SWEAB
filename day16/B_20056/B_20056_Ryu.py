direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
fire_map = [[[] for _ in range(N)] for __ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_map[r - 1][c - 1].append([m, s, d])

for x in range(K):
    move_map = [[[] for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            while fire_map[i][j]:
                cur = fire_map[i][j].pop()
                move_map[(i + cur[1] * direction[cur[2]][0]) % N][(j + cur[1] * direction[cur[2]][1]) % N].append(cur)

    for i in range(N):
        for j in range(N):
            if len(move_map[i][j]) > 1:
                mt, st, dt = 0, 0, move_map[i][j][0][2] % 2
                swi = 0
                for m, s, d in move_map[i][j]:
                    mt += m
                    st += s
                    if dt != d % 2:
                        swi = 1
                mt //= 5
                st //= len(move_map[i][j])
                if mt > 0:
                    if swi == 0:
                        move_map[i][j] = [[mt, st, 0], [mt, st, 2], [mt, st, 4], [mt, st, 6]]
                    else:
                        move_map[i][j] = [[mt, st, 1], [mt, st, 3], [mt, st, 5], [mt, st, 7]]
                if mt == 0:
                    move_map[i][j] = []
    fire_map = [[move_map[i][j] for j in range(N)] for i in range(N)]

rlt = 0
for i in range(N):
    for j in range(N):
       for fire in fire_map[i][j]:
           rlt += fire[0]
print(rlt)