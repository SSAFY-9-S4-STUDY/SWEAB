# 해결되지 않아서 구글 참고했습니다

import sys, copy
input = sys.stdin.readline

def move(dir):
    if dir == 0:
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[idx][j] = temp

    elif dir == 1:
        for j in range(N):
            idx = N - 1
            for i in range(N - 2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][j] = temp

    elif dir == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = temp

    else:
        for i in range(N):
            idx = N - 1
            for j in range(N - 2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = temp


def dfs(cnt):
    global arr, result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                result = max(result, arr[i][j])
        return

    temp_a = copy.deepcopy(arr)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        arr = copy.deepcopy(temp_a)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0)
print(result)