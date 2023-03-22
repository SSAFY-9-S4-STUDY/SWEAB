import copy

delta = {
    0: (0, -1),
    1: (1, -1),
    2: (1, 0),
    3: (1, 1),
    4: (0, 1),
    5: (-1, 1),
    6: (-1, 0),
    7: (-1, -1),
}


def eject(arr):
    d = delta.get(arr[4])
    
    # for i in range(arr[3]):
    #     nx, ny = arr[1] + d[0], arr[0] + d[1]
    #     if 0 <= nx < n and 0 <= ny < n:
    #         continue
    #     elif 0 <= nx < n and ny < 0:
    #         ny = n - 1
    #     elif 0 <= nx < n and ny >= n:
    #         ny = 0
    #     elif 0 <= ny < n and nx < 0:
    #         nx = n - 1
    #     elif 0 <= ny < n and nx >= n:
    #         nx = 0
    #     elif nx < 0:

    nx = arr[1] + d[0] * arr[3]
    if 0 <= nx < n:
        pass
    elif nx < 0:
        while not 0 <= nx < n:
            nx += n
    else:
        while not 0 <= nx < n:
            nx -= n
    
    ny = arr[0] + d[1] * arr[3]    
    if 0 <= ny < n:
        pass
    elif ny < 0:
        while not 0 <= ny < n:
            ny += n
    else:
        while not 0 <= ny < n:
            ny -= n

    table[ny][nx] += 1
    return [ny, nx, arr[2], arr[3], arr[4]]
   


def meet(n_arr):
    lst = []
    # print(f"meet {(n_arr[0], n_arr[1]), n_arr[2] // 5}")

    if n_arr[2] // 5 > 0:

        if n_arr[4][1] == 'o' * table[n_arr[0]][n_arr[1]] or n_arr[4][1] == 'e' * table[n_arr[0]][n_arr[1]]:
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 0])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 2])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 4])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 6])
        else:
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 1])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 3])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 5])
            lst.append([n_arr[0], n_arr[1], n_arr[2] // 5, n_arr[3] // table[n_arr[0]][n_arr[1]], 7])

        return lst

    else:
        return None


n, m, k = map(int, input().split())

tmp_fire = []
for i in range(m):
    tmp_fire.append(list(map(int, input().split())))
    tmp_fire[i][0] -= 1
    tmp_fire[i][1] -= 1

arrival = []
for i in range(k):
    # print(f"#{i + 1}")
    # print(f"start {tmp_fire}")
    fire = copy.deepcopy(tmp_fire)
    table = [[0] * n for _ in range(n)]
    tmp_fire = []
    for ball in fire:
        arrival.append(eject(ball))  # table 업데이트, 도착지점에 ball 일단 둠
    # print(f"arrive {arrival}")
    arrival.sort(key=lambda x: (x[0], x[1]))
    while arrival:
        current = arrival[0]
        r = c = m = s = d = 0

        if table[current[0]][current[1]] > 1:
            d = [0, '']
            for _ in range(table[current[0]][current[1]]):
                current = arrival.pop(0)
                r = current[0]
                c = current[1]
                m += current[2]
                s += current[3]
                if current[4] % 2:
                    d[0] += current[4]
                    d[1] += 'o'
                else:
                    d[0] += current[4]
                    d[1] += 'e'

            # print(f"odd or even: {d[1]}")

            tmp = meet([r, c, m, s, d])
            if tmp:
                tmp_fire += tmp
            else:
                continue

        else:
            tmp_fire.append(arrival.pop(0))

    # print(f"last {tmp_fire}")

ans = 0
for i in range(len(tmp_fire)):
    ans += tmp_fire[i][2]

print(ans)

