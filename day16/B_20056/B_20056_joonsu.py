# https://bonbon-au-chocolat.tistory.com/3?category=1083048
# 안풀려서 참고했는데 틀렸다고 나와서 추후 수정하겠습니다..

N, M, K = map(int, input().split())
arr = [[list() for _ in range(N)] for _ in range(N)]
fireball = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while fireball:
        ri, ci, mi, si, di = fireball.pop()
        new_y = (ci-1 + dy[di] * si) % N
        new_x = (ri-1 + dx[di] * si) % N
        arr[new_x][new_y].append([mi, si, di])

    for i in range(N):
        for j in range(N):
            count = len(arr[i][j])
            if not count:
                continue

            if count == 1:
                fireball.append([i, j] + arr[i][j].pop())

            elif count > 1:
                sum_mass, sum_speed, state = 0, 0, 0
                while arr[i][j]:
                    mi, si, di = arr[i][j].pop()
                    sum_mass += mi
                    sum_speed += si
                    if di%2:
                        state += 1
                    else:
                        state = -1

                if not sum_mass //5:
                    continue

                if count == abs(state):
                    new_d = [0, 2, 4, 6]
                else:
                    new_d = [1, 3, 5, 7]

                for d in new_d:
                    fireball.append([ri, ci, sum_mass//5, sum_speed//count, d])

print(sum([i[2] for i in fireball]))