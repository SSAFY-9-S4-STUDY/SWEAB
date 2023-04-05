def solution(i,j, size):
    global cnt_zero,cnt_plus,cnt_minus
    if size == 1:
        if arr[i][j] == -1:
            cnt_minus += 1
        elif arr[i][j] == 0:
            cnt_zero += 1
        else:
            cnt_plus += 1
        return
    pivot = arr[i][j]
    check = 1
    for dx in range(size):
        for dy in range(size):
            if arr[i+dx][j+dy] != pivot:
                check = -1
                break
        if check==-1:
            break
    if check == -1:
        solution(i, j, size // 3)
        solution(i, j + size // 3, size // 3)
        solution(i, j + 2 * size // 3, size // 3)
        solution(i + size // 3, j, size // 3)
        solution(i + size // 3, j + size // 3, size // 3)
        solution(i + size // 3, j + 2 * size // 3, size // 3)
        solution(i + 2 * size // 3, j, size // 3)
        solution(i + 2 * size // 3, j + size // 3, size // 3)
        solution(i + 2 * size // 3, j + 2 * size // 3, size // 3)
    else:
        if pivot == -1:
            cnt_minus += 1
        elif pivot == 0:
            cnt_zero += 1
        else:
            cnt_plus += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_minus = cnt_zero = cnt_plus = 0
solution(0, 0, N)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)