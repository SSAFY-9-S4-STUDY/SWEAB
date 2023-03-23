import sys
input = sys.stdin.readline
# 죄송.. 구글링 해도 잘 모르겠..어...
# 코드는 이해했는데 개념을 모르겠..어..
# 누가 설명 좀 ㅠㅠㅠㅠㅠ


def dp(weight, value, k, n):
    dp_arr = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if weight[i] <= j:
                dp_arr[i][j] = max(value[i]+dp_arr[i-1][j-weight[i]], dp_arr[i-1][j])
            else:
                dp_arr[i][j] = dp_arr[i-1][j]
    return dp_arr[n][k]


N, K = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
arr_t = list((zip(*arr)))
print(dp(arr_t[0], arr_t[1], K, N))


# 누가 볼지는 모르겠지만 내 dfs 풀이도 구경해줘잉 ><
# 날리기 아까워 ㅎㅎ
'''
def dfs(idx, include, tmp_val, tmp_w):
    global max_v
    if include:
        tmp_w += arr[idx][0]
        tmp_val += arr[idx][1]
        max_v = max(max_v, tmp_val)

    idx += 1
    if idx == N + 1 or tmp_w + arr[idx][0] > K:
        return

    dfs(idx, 1, tmp_val, tmp_w)
    dfs(idx, 0, tmp_val, tmp_w)


N, K = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

max_v = -1
dfs(0, 0, 0, 0)
print(max_v)
'''