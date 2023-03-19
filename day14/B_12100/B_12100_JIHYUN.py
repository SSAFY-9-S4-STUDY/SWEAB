from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 이걸 어떻게 하죠...
# 저 웁니다 엉엉
# 일단 올리고 집가서 다시해볼게요
# 신박한 방법을 찾고 싶었는데 그냥 하드코딩 했습니다 키킼
# 저 답이 계속 틀리네요^^ ㅎㅎㅎ
# 디버깅 성공했다고 생각했는데 또 틀렸네용 ㅎㅎㅎ
# 우와 디버깅 성공 ㅠㅠㅠㅠㅠㅠㅠ


def move(arr, direction):
    # 위
    if direction == 0:
        for j in range(N):
            fill_index = 0
            combine = True      # True: 합쳐질 수 있다 == 합쳐진 적이 없다
            for i in range(N):
                if arr[i][j] and fill_index == 0:
                    arr[0][j] = arr[i][j]
                    fill_index += 1
                elif arr[i][j]:
                    if combine and arr[fill_index - 1][j] == arr[i][j]:
                        arr[fill_index - 1][j] *= 2
                        combine = False
                    else:
                        arr[fill_index][j] = arr[i][j]
                        fill_index += 1
                        combine = True
            else:   # 행을 다 돌면
                if fill_index == N:
                    continue
                for rest in range(fill_index, N):
                    arr[rest][j] = 0

    # 아래
    elif direction == 1:
        for j in range(N):
            fill_index = N - 1
            combine = True
            for i in range(N-1, -1, -1):
                if arr[i][j] and fill_index == N - 1:
                    arr[N - 1][j] = arr[i][j]
                    fill_index -= 1
                elif arr[i][j]:
                    if combine and arr[fill_index + 1][j] == arr[i][j]:
                        arr[fill_index + 1][j] *= 2
                        combine = False
                    else:
                        arr[fill_index][j] = arr[i][j]
                        fill_index -= 1
                        combine = True
            else:
                if fill_index == -1:
                    continue
                for rest in range(fill_index, -1, -1):
                    arr[rest][j] = 0

    # 왼쪽
    elif direction == 2:
        for i in range(N):
            fill_index = 0
            combine = True
            for j in range(N):
                if arr[i][j] and fill_index == 0:
                    arr[i][0]= arr[i][j]
                    fill_index += 1
                elif arr[i][j]:
                    if combine and arr[i][fill_index - 1] == arr[i][j]:
                        arr[i][fill_index - 1] *= 2
                        combine = False
                    else:
                        arr[i][fill_index] = arr[i][j]
                        fill_index += 1
                        combine = True
            else:
                if fill_index == N:
                    continue
                for rest in range(fill_index, N):
                    arr[i][rest] = 0

    # 오른쪽
    else:
        for i in range(N):
            fill_index = N - 1
            combine = True
            for j in range(N-1, -1, -1):
                if arr[i][j] and fill_index == N - 1:
                    arr[i][N - 1] = arr[i][j]
                    fill_index -= 1
                elif arr[i][j]:
                    if combine and arr[i][fill_index + 1] == arr[i][j]:
                        arr[i][fill_index + 1] *= 2
                        combine = False
                    else:
                        arr[i][fill_index] = arr[i][j]
                        fill_index -= 1
                        combine = True
            else:
                if fill_index == -1:
                    continue
                for rest in range(fill_index, -1, -1):
                    arr[i][rest] = 0
    return arr


def dfs(cnt, arr):
    # 5번 움직이면 return으로 종료
    global maxi
    if cnt == 5:
        for row in arr:
            maxi = max(max(row), maxi)
        return

    # 5번 아니면 상하좌우 방향으로 또 움직여
    cnt += 1
    dfs(cnt, move(deepcopy(arr), 0))  # 0: 위
    dfs(cnt, move(deepcopy(arr), 1))  # 1: 아래
    dfs(cnt, move(deepcopy(arr), 2))  # 2: 왼쪽
    dfs(cnt, move(deepcopy(arr), 3))  # 3: 오른쪽


maxi = 0
dfs(0, arr)
print(maxi)
