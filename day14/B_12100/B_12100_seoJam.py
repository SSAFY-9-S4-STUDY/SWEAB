import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt")

def shake(arr, n):
    if n == 0:    # Right
        for i in range(N):
            for j in range(N-1, -1, -1):
                if arr[i][j]:
                    if not arr[i][j-1]:

    elif n == 1:  # Left
        pass
    elif n == 2:  # Down
        pass
    elif n == 3:  # Up
        pass
    return arr

def DFS(arr):
    global ans
    global cnt
    if cnt == 5:        # DFS 5번 하면 최댓값 출력 후 끝
        for i in range(N):
            for j in range(N):
                ans = max(ans, arr[i][j])
        return
    for n in range(4):  # 4방향으로 흔들기
        cnt += 1
        temp_arr = shake(arr, n)
        DFS(temp_arr)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = cnt = 0
DFS(arr)
print(ans)






