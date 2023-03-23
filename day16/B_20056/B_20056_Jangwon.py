N, M, K = map(int, input().split())  # 격자, 파이어볼 갯수, 명령 횟수

row = [0 for _ in range(M)]
column = [0 for _ in range(M)]
mass = [0 for _ in range(M)]
velocity = [0 for _ in range(M)]
direction = [0 for _ in range(M)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    row[i] = r
    column[i] = c
    mass[i] = m
    velocity[i] = s
    direction[i] = d

while K:
    for i in range(len(mass)):
        row[i] = (row[i] + dy[direction[i]] * velocity[i]) % N
        column[i] = (column[i] + dx[direction[i]] * velocity[i]) % N

    for a in range(len(mass) - 1):
        if not mass[a]:
            continue
        else:
            cnt = 1
            status = False
            odd_even = direction[a] % 2
            for b in range(a + 1, len(mass)):
                if row[a] == row[b] and column[a] == column[b]:
                    if not mass[b]:
                        continue
                    else:
                        cnt += 1
                        mass[a] += mass[b]
                        mass[b] = 0
                        velocity[a] += velocity[b]
                        velocity[b] = 0
                        odd_even += direction[b] % 2
                        status = True
        if status:
            mass[a] //= 5
            velocity[a] //= cnt
            if odd_even == 0 or odd_even == cnt:
                direction[a] = 0
                for z in range(1, 4):
                    row.append(row[a])
                    column.append(column[a])
                    mass.append(mass[a])
                    velocity.append(velocity[a])
                    direction.append(2 * z)

            else:
                direction[a] = 1
                for z in range(1, 4):
                    row.append(row[a])
                    column.append(column[a])
                    mass.append(mass[a])
                    velocity.append(velocity[a])
                    direction.append(2 * z + 1)

    p = 0
    while p != len(mass):
        if not mass[p]:
            row.pop(p)
            column.pop(p)
            mass.pop(p)
            direction.pop(p)
            velocity.pop(p)
        else:
            p += 1

    K -= 1

ans = sum(mass)
print(ans)