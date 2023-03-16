N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 이걸 어떻게 하죠...
# 저 웁니다 엉엉
# 일단 올리고 집가서 다시해볼게요


def move(arr):
    # 아웅 배고파서 머리가 안돌아가요
    return


def dfs(cnt, arr):
    # 5번 움직이면 return으로 종료
    if cnt == 5:
        # 배열에서 가장 큰 값 찾기
        return
    dfs(cnt + 1, arr_up)
    dfs(cnt + 1, arr_down)
    dfs(cnt + 1, arr_left)
    dfs(cnt + 1, arr_right)

dfs(0, arr)
print()
