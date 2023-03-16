# 좌로 밀착 : 열들의 그룹에서 맨 왼쪽에서부터 stack, 합쳐지면 오른쪽에 0 추가
# 우로 밀착 : 열들의 그룹에서 맨 오른쪽부터 stack, 합쳐지면 왼쪽에 0 추가
# 상-하 : 좌 우 를 행들의 그룹으로 바꿈

# 상하좌우 로 밀착
# 상 : 0~n, 하 : n~0, 좌 : 0~n, 우 : n~0

import pprint

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def all_case(arr):  # arr == table
    # 상하좌우 모든 case 탐색하기
    cases = [[] for _ in range(4)]
    idx = 0
    for d in delta:
        stack = [[] for _ in range(n)]
        tmp_table = [[0] * n for _ in range(n)]
        # 각 방향에 맞게 "좌표값"을 스택에 저장.
        if d == (0, 1):  # 상 으로 밀착
            for i in range(n):
                stack[i] = [(i, 0)]
        elif d == (0, -1):  # 하
            for i in range(n):
                stack[i] = [(i, n - 1)]
        elif d == (1, 0):  # 좌
            for i in range(n):
                stack[i] = [(0, i)]
        elif d == (-1, 0):  # 우
            for i in range(n):
                stack[i] = [(n - 1, i)]
        # print(f"initial = {stack}")

        for i in range(n):
            start = stack[i][0]
            # print(f"start = {start}")
            while stack[i]:
                now = stack[i].pop()
                flag = arr[now[1]][now[0]]
                nx, ny = now[0] + d[0], now[1] + d[1]
                if 0 <= nx < n and 0 <= ny < n and flag:
                    while 0 <= nx < n and 0 <= ny < n:
                        if arr[ny][nx] != 0:
                            if arr[ny][nx] == flag:
                                tmp = flag * 2
                                jump_x, jump_y = nx + d[0], ny + d[1]
                                if 0 <= jump_x < n and 0 <= jump_y < n:
                                    stack[i].append((jump_x, jump_y))
                                break
                            else:
                                tmp = flag
                                stack[i].append((nx, ny))
                                break
                        else:
                            nx, ny = nx + d[0], ny + d[1]
                    else:
                        tmp = flag
                elif flag:
                    tmp = flag
                elif 0 <= nx < n and 0 <= ny < n:
                    stack[i].append((nx, ny))
                    continue
                if flag:
                    for j in range(n):
                        # print(start[0] + j * d[0], start[1] + j * d[1])
                        if tmp_table[start[1] + j * d[1]][start[0] + j * d[0]] == 0:
                            tmp_table[start[1] + j * d[1]][start[0] + j * d[0]] = tmp
                            break

        cases[idx] = tmp_table
        idx += 1

    return cases


# now에서 - d를 한 곳을 거슬러 올라가 0이면 진행, 아니면 break하고 +d 해주고 거기에 값 저장
# 만약 now가 in start이면 멈추고 거기에 저장

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]


# 상하좌우 각각의 경우에 대해 탐색하는 반복문 만들기 == all_case(arr) 함수
# 위의 경우를 5번 반복하게 반복문으로 감싸기
# 5번 반복 진행 후 최대값 찾기

table = [table]  # 원래는 3중배열(list(이중배열 모음)) 인 것을 돌리는 반복문이기 때문에 한번 감싸줌

for _ in range(5):
    tmp_table = []
    for i in range(len(table)):
        a_table = all_case(table[i])
        for j in range(4):
            tmp_table.append(a_table[j])
    table = [copy[:] for copy in tmp_table]

result = 2
for i in range(len(table)):
    is_max = max(map(max, table[i]))
    if result < is_max:
        result = is_max

print(result)

"""
10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
128 32 0 0 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0


"""