# 시간초과에서 328ms 찍은 지현이의 성장일기
# 지현아! # 멋있다!

import sys
input = sys.stdin.readline

direc = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1],
         4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

for _ in range(K):
    # counts의 key는 파이어볼이 있는 좌표 (튜플 형태)
    # counts의 value는 파이어볼이 있는 좌표의[파이어볼 수, 총 질량, 총속력, [각 방향들]](리스트 형태)
    counts = {}
    for r, c, m, s, d in arr:

        # 파이어볼의 다음 좌표
        di, dj = direc.get(d)
        r = (r + s * di) % N if (r + s * di) % N != 0 else N
        c = (c + s * dj) % N if (c + s * dj) % N != 0 else N

        # 해당 좌표에 이미 파이어볼이 있다면 질량, 속력 업데이트하고 현재 파이어볼 방향 추가
        if counts.get((r, c)):
            counts[(r, c)][0] += 1
            counts[(r, c)][1] += m
            counts[(r, c)][2] += s
            counts[(r, c)][3].append(d)
        # 해당 좌표에 파이어볼 없으면 key, value 추가
        else:
            counts[(r, c)] = [1, m, s, [d]]

    # arr 업데이트
    arr = []
    for key, value in counts.items():
        # 파이어볼 개수가 하나라면 다음 arr에 추가
        if value[0] == 1:
            arr.append([key[0], key[1], value[1], value[2], value[3][0]])
            continue

        # 4개로 나눠진 질량이 0이라면 아무고토 하지 않지
        new_mass = value[1] // 5
        if new_mass == 0:
            continue

        # 질량이 0이 아닐때 속력과 방향 구하고
        new_speed = value[2] // value[0]

        odd_even = value[3].pop(0) % 2
        for d in value[3]:
            if odd_even != d % 2:
                new_direction = [1, 3, 5, 7]
                break
        else:
            new_direction = [0, 2, 4, 6]

        # arr에 추가
        for d in new_direction:
            arr.append([key[0], key[1], new_mass, new_speed, d])

total_mass = 0
for r, c, m, s, d in arr:
    total_mass += m

print(total_mass)
